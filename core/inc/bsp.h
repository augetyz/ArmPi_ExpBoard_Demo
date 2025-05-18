#ifndef BSP_H
#define BSP_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

void bsp_gpio_init(void);
void bsp_serial_init(void);
void bsp_deinit(void);
int bsp_serial_write(uint8_t idx, const uint8_t* buf, size_t len);
int bsp_serial_read(uint8_t idx, uint8_t* buf, size_t len, int timeout_ms);
int bsp_serial_input_waiting(uint8_t idx, unsigned int* count);
int bsp_serial_output_waiting(uint8_t idx, unsigned int* count);
bool KeyRead(uint8_t key_index);
void LedSet(uint8_t led_index, bool value);


#endif /* BSP_H */
