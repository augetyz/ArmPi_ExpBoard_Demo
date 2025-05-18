#ifndef WS2812_H
#define WS2812_H

#include "driver_ws2812b_interface.h"

#define rgb(r,g,b) (uint32_t)((r<<16)+(g<<8)+(b))
/**
 * @defgroup ws2812b_example_driver ws2812b example driver function
 * @brief    ws2812b example driver modules
 * @ingroup  ws2812b_driver
 * @{
 */

 /**
  * @brief  basic example init
  * @return status code
  *         - 0 success
  *         - 1 init failed
  * @note   none
  */
uint8_t ws2812_init(uint8_t num);

/**
 * @brief  basic example deinit
 * @return status code
 *         - 0 success
 *         - 1 deinit failed
 * @note   none
 */
uint8_t ws2812_deinit(void);

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
uint8_t ws2812_write(uint32_t* rgb, uint32_t len, uint8_t* temp, uint32_t temp_len);
uint8_t ws2812_SetRGB(uint32_t index, uint32_t rgb);

#endif