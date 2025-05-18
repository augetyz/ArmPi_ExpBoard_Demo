/* sys_monitor.c: 系统监控接口实现 */
#include "sys_monitor.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/statvfs.h>
#include <sys/types.h>
#include <sys/ioctl.h>
#include <net/if.h>
#include <ifaddrs.h>
#include <arpa/inet.h>
#include <time.h>

// 用于计算网速的静态变量
static unsigned long long prev_rx_bytes = 0;
static unsigned long long prev_tx_bytes = 0;
static struct timespec prev_ts = { 0, 0 };

// Helper: 读取 /proc/stat 中的总 CPU 时间和空闲时间
static int read_cpu_times(unsigned long long* total, unsigned long long* idle)
{
    FILE* fp = fopen("/proc/stat", "r");
    if (!fp) return -1;
    char buf[256];
    if (!fgets(buf, sizeof(buf), fp)) { fclose(fp); return -1; }
    fclose(fp);
    unsigned long long user, nice, system, idle_t, iowait, irq, softirq, steal;
    int n = sscanf(buf, "cpu  %llu %llu %llu %llu %llu %llu %llu %llu",
        &user, &nice, &system, &idle_t, &iowait, &irq, &softirq, &steal);
    if (n < 4) return -1;
    *idle = idle_t + (n > 4 ? iowait : 0);
    *total = user + nice + system + *idle + (n > 5 ? irq + softirq + steal : 0);
    return 0;
}

float sysmon_get_cpu_usage(void)
{
    static unsigned long long last_total = 0, last_idle = 0;
    unsigned long long total, idle;
    if (read_cpu_times(&total, &idle) < 0) return 0.0f;
    unsigned long long diff_total = total - last_total;
    unsigned long long diff_idle = idle - last_idle;
    float usage = 0.0f;
    if (diff_total > 0)
        usage = (float)(diff_total - diff_idle) * 100.0f / (float)diff_total;
    last_total = total;
    last_idle = idle;
    return usage;
}

float sysmon_get_memory_usage(void)
{
    FILE* fp = fopen("/proc/meminfo", "r");
    if (!fp) return 0.0f;

    char key[64];
    unsigned long memTotal = 0;
    unsigned long memAvailable = 0;
    unsigned long memFree = 0;
    unsigned long value;

    // 逐行读取 key 和 value
    while (fscanf(fp, "%63s %lu kB\n", key, &value) == 2)
    {
        if (strcmp(key, "MemTotal:") == 0)
        {
            memTotal = value;
        }
        else if (strcmp(key, "MemAvailable:") == 0)
        {
            memAvailable = value;
        }
        else if (strcmp(key, "MemFree:") == 0)
        {
            memFree = value;
        }

        // 如果已经拿到了总内存，并且 (可用或空闲) 中至少一个，就可以结束循环
        if (memTotal && (memAvailable || memFree)) break;
    }
    fclose(fp);

    if (memTotal == 0) return 0.0f;

    // 优先使用 MemAvailable，否则退回到 MemFree
    unsigned long avail = memAvailable ? memAvailable : memFree;

    // 计算使用率
    float usage = (float)(memTotal - avail) * 100.0f / (float)memTotal;
    return usage;
}

void sysmon_get_net_speed(const char* iface, float* down_kbps, float* up_kbps)
{
    char path[128];
    unsigned long long rx_bytes = 0, tx_bytes = 0;
    FILE* fp;
    // 读取接收字节
    snprintf(path, sizeof(path), "/sys/class/net/%s/statistics/rx_bytes", iface);
    fp = fopen(path, "r");
    if (fp) { fscanf(fp, "%llu", &rx_bytes); fclose(fp); }
    // 读取发送字节
    snprintf(path, sizeof(path), "/sys/class/net/%s/statistics/tx_bytes", iface);
    fp = fopen(path, "r");
    if (fp) { fscanf(fp, "%llu", &tx_bytes); fclose(fp); }
    struct timespec now;
    clock_gettime(CLOCK_MONOTONIC, &now);
    if (prev_ts.tv_sec == 0)
    {
        prev_ts = now;
        prev_rx_bytes = rx_bytes;
        prev_tx_bytes = tx_bytes;
        *down_kbps = 0.0f;
        *up_kbps = 0.0f;
    }
    else
    {
        double elapsed = (now.tv_sec - prev_ts.tv_sec) + (now.tv_nsec - prev_ts.tv_nsec) / 1e9;
        if (elapsed <= 0) elapsed = 1.0;
        *down_kbps = (rx_bytes - prev_rx_bytes) / 1024.0f / elapsed;
        *up_kbps = (tx_bytes - prev_tx_bytes) / 1024.0f / elapsed;
        prev_ts = now;
        prev_rx_bytes = rx_bytes;
        prev_tx_bytes = tx_bytes;
    }
}

float sysmon_get_cpu_temperature(void)
{
    // 读取第一个可用的温度传感
    const char* temp_paths[] = {
        "/sys/class/thermal/thermal_zone0/temp",
        "/sys/class/hwmon/hwmon0/temp1_input",
        NULL
    };
    for (int i = 0; temp_paths[i]; i++)
    {
        FILE* fp = fopen(temp_paths[i], "r");
        if (fp)
        {
            long mC;
            if (fscanf(fp, "%ld", &mC) == 1)
            {
                fclose(fp);
                return mC / 1000.0f;
            }
            fclose(fp);
        }
    }
    return 0.0f;
}

void sysmon_get_disk_usage(float* usage_percent, float* total_gb)
{
    struct statvfs st;
    if (statvfs("/", &st) < 0)
    {
        *usage_percent = 0.0f;
        *total_gb = 0.0f;
        return;
    }
    unsigned long long total = st.f_blocks * st.f_frsize;
    unsigned long long avail = st.f_bavail * st.f_frsize;
    unsigned long long used = total - avail;
    *total_gb = total / (1024.0f * 1024.0f * 1024.0f);
    *usage_percent = (float)used * 100.0f / (float)total;
}

bool sysmon_iface_up(const char* iface)
{
    char path[128], flag;
    snprintf(path, sizeof(path), "/sys/class/net/%s/operstate", iface);
    FILE* fp = fopen(path, "r");
    if (!fp) return false;
    flag = fgetc(fp);
    fclose(fp);
    return (flag == 'u');  // "up" 的首字母
}

bool sysmon_get_ip(const char* iface, char* buf, size_t buf_len)
{
    struct ifaddrs* ifaddr, * ifa;
    if (getifaddrs(&ifaddr) == -1) return false;
    bool found = false;
    for (ifa = ifaddr; ifa; ifa = ifa->ifa_next)
    {
        if (ifa->ifa_addr == NULL) continue;
        if (strcmp(ifa->ifa_name, iface) == 0 && ifa->ifa_addr->sa_family == AF_INET)
        {
            struct sockaddr_in* sa = (struct sockaddr_in*)ifa->ifa_addr;
            inet_ntop(AF_INET, &sa->sin_addr, buf, buf_len);
            found = true;
            break;
        }
    }
    freeifaddrs(ifaddr);
    return found;
}
