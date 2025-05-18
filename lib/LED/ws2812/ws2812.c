#include "ws2812.h"

static ws2812b_handle_t gs_handle;        /**< ws2812b handle */
static uint32_t* rgb_buffer = NULL;
static uint8_t* point_buffer = NULL;
static uint8_t ws2812Num = 0; // ws2812灯珠数量

/**
 * @brief  basic example init
 * @return status code
 *         - 0 success
 *         - 1 init failed
 * @note   none
 */
uint8_t ws2812_init(uint8_t num)
{
    uint8_t res;

    /* link interface function */
    DRIVER_WS2812B_LINK_INIT(&gs_handle, ws2812b_handle_t);
    DRIVER_WS2812B_LINK_SPI_10MHZ_INIT(&gs_handle, ws2812b_interface_spi_10mhz_init);
    DRIVER_WS2812B_LINK_SPI_DEINIT(&gs_handle, ws2812b_interface_spi_deinit);
    DRIVER_WS2812B_LINK_SPI_WRITE_COMMAND(&gs_handle, ws2812b_interface_spi_write_cmd);
    DRIVER_WS2812B_LINK_DELAY_MS(&gs_handle, ws2812b_interface_delay_ms);
    DRIVER_WS2812B_LINK_DEBUG_PRINT(&gs_handle, ws2812b_interface_debug_print);

    /* ws2812b initialization */
    res = ws2812b_init(&gs_handle);
    if (res != 0)
    {
        ws2812b_interface_debug_print("ws2812b: init failed.\n");

        return 1;
    }
    rgb_buffer = (uint32_t*)malloc(num * sizeof(uint32_t));
    if (rgb_buffer == NULL)
    {
        return 1; // 内存分配失败
    }

    point_buffer = (uint8_t*)malloc(num * 64 * sizeof(uint8_t));
    if (point_buffer == NULL)
    {
        free(rgb_buffer); // 确保不泄露已分配的内存
        rgb_buffer = NULL;
        return 1;
    }
    ws2812Num = num;
    return 0;
}

/**
 * @brief     basic example write
 * @param[in] *rgb points to a rgb color buffer
 * @param[in] len is the rgb length
 * @param[in] *temp points to a temp buffer
 * @param[in] temp_len is the temp buffer length
 * @return    status code
 *            - 0 success
 *            - 1 write failed
 * @note      none
 */
uint8_t ws2812_write(uint32_t* rgb, uint32_t len, uint8_t* temp, uint32_t temp_len)
{
    if (ws2812b_write(&gs_handle, rgb, len, temp, temp_len) != 0)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

/**
 * @brief  basic example deinit
 * @return status code
 *         - 0 success
 *         - 1 deinit failed
 * @note   none
 */
uint8_t ws2812_deinit(void)
{
    if (ws2812b_deinit(&gs_handle) != 0)
    {
        return 1;
    }
    else
    {
        if (rgb_buffer != NULL)
        {
            free(rgb_buffer);
            rgb_buffer = NULL;
        }
        if (point_buffer != NULL)
        {
            free(point_buffer);
            point_buffer = NULL;
        }
        return 0;
    }
}

uint8_t ws2812_SetRGB(uint32_t index, uint32_t rgb)
{
    if (index >= ws2812Num)
    {
        return 1; // 索引越界
    }
    if (rgb_buffer != NULL)
    {
        rgb_buffer[index] = rgb;
        ws2812_write(rgb_buffer, ws2812Num, point_buffer, ws2812Num * 64);
        return 0;
    }
    else
    {
        return 1; // 内存未分配或其他错误
    }
}
