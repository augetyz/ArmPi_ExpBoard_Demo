#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <unistd.h>
#include <signal.h>
#include <time.h>
#include <sys/types.h>
#include <sys/time.h>

#include "bsp.h"
#include "ws2812.h"
#include "timer.h"
#include "driver_st7789_basic.h"
#include "sys_monitor.h"
#include "lvgl.h"
#include "lv_port_disp.h"
#include "lv_demo_benchmark.h"
#include "gui_guider.h"
#include "events_init.h"

lv_ui guider_ui;
static lv_timer_t* status_timer;
void lvgl_tick(void* data)
{
    lv_tick_inc(1);
    lv_task_handler();
    video_play(&guider_ui);
    lv_timer_handler();
}
static void update_status_cb(lv_timer_t* timer);
int main(int argc, char* argv[])
{
    /**************** 变量定义 ****************/
    timer_t t1;
    bool value;
    /*************** 设备初始化 ***************/
    bsp_gpio_init();
    bsp_serial_init();
    ws2812_init(3);
    st7789_basic_init();
    st7789_basic_clear();
    sleep(1);
    timer_start(1000, lvgl_tick, &t1);

    /**************** 逻辑代码 ****************/
    ws2812_SetRGB(2, rgb(0x0D, 0x0E, 0x00));
    ws2812_SetRGB(1, rgb(0x00, 0x0F, 0x0F));
    ws2812_SetRGB(0, rgb(0x0D, 0x00, 0x0E));

    st7789_basic_clear();
    st7789_basic_string(20, 20, "Hello world", 12, 0X03E0, ST7789_FONT_16);

    lv_init();                   /* lvgl系统初始化 */
    lv_port_disp_init();         /* lvgl显示接口初始化,放在lv_init()的后面 */
    // lv_demo_stress();
    // lv_demo_benchmark();
    sleep(1);
    setup_ui(&guider_ui);
    events_init(&guider_ui);
    status_timer = lv_timer_create(update_status_cb, 1000, &guider_ui);
    while (1)
    {
        if (KeyRead(1) == 0)
        {
            printf("Key1 pressed\n");
        }
        if (KeyRead(2) == 0)
        {
            printf("Key2 pressed\n");
        }
        usleep(10 * 1000);
    }
    bsp_deinit();
    ws2812_deinit();
    st7789_basic_deinit();
    return 0;
}
/* 每秒调用一次，更新所有状态 */
static void update_status_cb(lv_timer_t* timer)
{
    lv_ui* ui = (lv_ui*)timer->user_data;

    // 1. 网络状态 & 图标
    bool eth_up = sysmon_iface_up("eth0");
    bool wifi_up = sysmon_iface_up("wlan0");
    if (eth_up == 1 || wifi_up == 1)
    {
        // 已连接
        lv_obj_clear_flag(guider_ui.screen_WIfi_connected, LV_OBJ_FLAG_HIDDEN);
        lv_obj_add_flag(guider_ui.screen_Wifi_disconnected, LV_OBJ_FLAG_HIDDEN);
    }
    else
    {
        // 未连接
        lv_obj_clear_flag(guider_ui.screen_Wifi_disconnected, LV_OBJ_FLAG_HIDDEN);
        lv_obj_add_flag(guider_ui.screen_WIfi_connected, LV_OBJ_FLAG_HIDDEN);
    }
    // 如果同时有两个接口，会在下面切换 IP 显示

    // 2. CPU 占用 & arc1/label_1
    float cpu = sysmon_get_cpu_usage();
    lv_arc_set_value(ui->screen_arc_1, (int)cpu);
    char buf1[32];
    snprintf(buf1, sizeof(buf1), "%.1f%%\nCPU", cpu);
    lv_label_set_text(ui->screen_label_1, buf1);

    // 3. 内存占用 & arc2/label_2
    float mem = sysmon_get_memory_usage();
    lv_arc_set_value(ui->screen_arc_2, (int)mem);
    char buf2[32];
    snprintf(buf2, sizeof(buf2), "%.1f%%\nRAM", mem);
    lv_label_set_text(ui->screen_label_2, buf2);

    // 4. 网速 label_3/upload, label_4/download
    float down, up;
    // 你可以根据实际优先接口决定是 eth0 还是 wlan0
    sysmon_get_net_speed(eth_up ? "eth0" : "wlan0", &down, &up);
    char buf3[32], buf4[32];
    snprintf(buf3, sizeof(buf3), "%.1f KB/s", up);
    snprintf(buf4, sizeof(buf4), "%.1f KB/s", down);
    lv_label_set_text(ui->screen_label_3, buf3);
    lv_label_set_text(ui->screen_label_4, buf4);

    // 5. 温度 label_5
    float tmp = sysmon_get_cpu_temperature();
    char buf5[32];
    snprintf(buf5, sizeof(buf5), "%.1fC", tmp);
    lv_label_set_text(ui->screen_label_5, buf5);

    // 6. 磁盘大小 & 使用率 label_6/bar_1
    float disk_pct, disk_total;
    sysmon_get_disk_usage(&disk_pct, &disk_total);
    char buf6[32];
    int a = disk_total * disk_pct / 100.0f;
    int b = disk_total;
    snprintf(buf6, sizeof(buf6), "%d/%dGB", a, b);
    lv_label_set_text(ui->screen_label_6, buf6);
    lv_bar_set_value(ui->screen_bar_1, (int)disk_pct, LV_ANIM_ON);

    // 7. IP 地址显示
    static bool show_eth = true;
    char ipbuf[32] = { 0 };
    if (eth_up && wifi_up)
    {
        // 两个都连，则每次切换显示
        show_eth = !show_eth;
        if (show_eth && sysmon_get_ip("eth0", ipbuf, sizeof(ipbuf)))
            lv_label_set_text(ui->screen_label_7, ipbuf);
        else if (!show_eth && sysmon_get_ip("wlan0", ipbuf, sizeof(ipbuf)))
            lv_label_set_text(ui->screen_label_7, ipbuf);
    }
    else if (eth_up)
    {
        if (sysmon_get_ip("eth0", ipbuf, sizeof(ipbuf)))
            lv_label_set_text(ui->screen_label_7, ipbuf);
    }
    else if (wifi_up)
    {
        if (sysmon_get_ip("wlan0", ipbuf, sizeof(ipbuf)))
            lv_label_set_text(ui->screen_label_7, ipbuf);
    }
    else
    {
        lv_label_set_text(ui->screen_label_7, "No Net");
    }
}