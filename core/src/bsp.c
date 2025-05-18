#include "gpio.h"
#include "serial.h"
#include "ws2812.h"
#include "driver_st7789_basic.h"
#include "lvgl.h"
#include "lv_port_disp.h"
#include "main.h"
#include "bsp.h"
#include <stdlib.h>
#define BSP_SERIAL_MAX    2

static gpio_t* Key1_GPIO, * Key2_GPIO, * LED1_GPIO, * LED2_GPIO;
static serial_t* serial1, * serial2, * serial_sbus;
static serial_t* serials[BSP_SERIAL_MAX];
static const char* serial_paths[BSP_SERIAL_MAX] = {
    // "/dev/ttyS2",
    "/dev/ttyS4",
    "/dev/ttyS7"
};
void bsp_gpio_init(void)
{
    LED1_GPIO = gpio_new();
    LED2_GPIO = gpio_new();
    Key1_GPIO = gpio_new();
    Key2_GPIO = gpio_new();

    if (gpio_open(LED1_GPIO, "/dev/gpiochip4", 12, GPIO_DIR_OUT) < 0)
    {
        fprintf(stderr, "gpio_open(): %s\n", gpio_errmsg(LED1_GPIO));
        exit(1);
    }
    if (gpio_open(LED2_GPIO, "/dev/gpiochip1", 5, GPIO_DIR_OUT) < 0)
    {
        fprintf(stderr, "gpio_open(): %s\n", gpio_errmsg(LED2_GPIO));
        exit(1);
    }
    if (gpio_open(Key1_GPIO, "/dev/gpiochip1", 8, GPIO_DIR_IN) < 0)
    {
        fprintf(stderr, "gpio_open(): %s\n", gpio_errmsg(Key1_GPIO));
        exit(1);
    }
    if (gpio_open(Key2_GPIO, "/dev/gpiochip1", 4, GPIO_DIR_IN) < 0)
    {
        fprintf(stderr, "gpio_open(): %s\n", gpio_errmsg(Key2_GPIO));
        exit(1);
    }
}
void bsp_serial_init(void)
{
    for (int i = 0; i < BSP_SERIAL_MAX; i++)
    {
        serials[i] = serial_new();
        if (!serials[i])
        {
            fprintf(stderr, "serial_new() failed for index %d\n", i);
            exit(1);
        }
        if (serial_open(serials[i], serial_paths[i], 115200) < 0)
        {
            fprintf(stderr, "serial_open(%s): %s\n",
                serial_paths[i],
                serial_errmsg(serials[i]));
            exit(1);
        }
    }
}

void bsp_deinit(void)
{
    gpio_close(LED1_GPIO);gpio_close(LED2_GPIO);gpio_close(Key1_GPIO);gpio_close(Key2_GPIO);
    gpio_free(LED1_GPIO);gpio_free(LED2_GPIO);gpio_free(Key1_GPIO);gpio_free(Key2_GPIO);
    for (int i = 0; i < BSP_SERIAL_MAX; i++)
    {
        if (serials[i])
        {
            serial_close(serials[i]);
            serial_free(serials[i]);
            serials[i] = NULL;
        }
    }
}
bool KeyRead(uint8_t key_index)
{
    gpio_t* Key_GPIO = NULL;
    bool value = 0;
    if (key_index == 1)
    {
        Key_GPIO = Key1_GPIO;
    }
    else if (key_index == 2)
    {
        Key_GPIO = Key2_GPIO;
    }
    else
    {
        return false;
    }
    if (gpio_read(Key_GPIO, &value) < 0)
    {
        fprintf(stderr, "gpio_read(): %s\n", gpio_errmsg(Key_GPIO));
        return false;
    }
    return value;
}
void LedSet(uint8_t led_index, bool value)
{
    gpio_t* Led_GPIO = NULL;
    if (led_index == 1)
    {
        Led_GPIO = LED1_GPIO;
    }
    else if (led_index == 2)
    {
        Led_GPIO = LED2_GPIO;
    }
    else
    {
        return;
    }
    gpio_write(Led_GPIO, value);
}

int bsp_serial_write(uint8_t idx, const uint8_t* buf, size_t len)
{
    if (idx >= BSP_SERIAL_MAX)
    {
        return SERIAL_ERROR_ARG;
    }
    return serial_write(serials[idx], buf, len);
}

int bsp_serial_read(uint8_t idx, uint8_t* buf, size_t len, int timeout_ms)
{
    if (idx >= BSP_SERIAL_MAX)
    {
        return SERIAL_ERROR_ARG;
    }
    return serial_read(serials[idx], buf, len, timeout_ms);
}

int bsp_serial_output_waiting(uint8_t idx, unsigned int* count)
{
    if (idx >= BSP_SERIAL_MAX || !count)
    {
        return SERIAL_ERROR_ARG;
    }
    return serial_output_waiting(serials[idx], count);
}

int bsp_serial_input_waiting(uint8_t idx, unsigned int* count)
{
    if (idx >= BSP_SERIAL_MAX || !count)
    {
        return SERIAL_ERROR_ARG;
    }
    return serial_input_waiting(serials[idx], count);
}


