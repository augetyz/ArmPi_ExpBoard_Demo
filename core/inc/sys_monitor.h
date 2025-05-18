#ifndef SYS_MONITOR_H
#define SYS_MONITOR_H
#include <unistd.h>
#include <stdbool.h>
void get_cpu_temperature();
void get_cpu_usage();
void get_memory_usage();
void get_disk_usage();
void get_uptime();
void get_network_info();
void get_network_speed();

// 返回平均 CPU 占用率（0–100）
float sysmon_get_cpu_usage(void);

// 返回内存使用率（0–100）
float sysmon_get_memory_usage(void);

// 获取网速，单位 KB/s
void  sysmon_get_net_speed(const char* iface, float* down_kbps, float* up_kbps);

// 返回 CPU 温度（°C）
float sysmon_get_cpu_temperature(void);

// 获取磁盘使用率（0–100）和总大小（GB）
void  sysmon_get_disk_usage(float* usage_percent, float* total_gb);

// 检查接口是否 up，返回 true/false
bool  sysmon_iface_up(const char* iface);

// 获取接口 IPv4 地址字符串，buf 至少 32 字节
bool  sysmon_get_ip(const char* iface, char* buf, size_t buf_len);
#endif
