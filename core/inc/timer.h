/* timer.h */
#ifndef TIMER_H
#define TIMER_H

#include <time.h>
#include <signal.h>


/**
 * 定义回调函数类型，参数为定时器传递的值
 */
typedef void (*timer_callback_t)(union sigval sv);

/**
 * 创建并启动一个周期性定时器
 * @param interval_ms 定时周期，单位毫秒
 * @param callback 回调函数，在每次定时到期时调用
 * @param timerid 输出参数，返回创建的定时器ID
 * @return 0 成功，-1 失败
 */
int timer_start(long interval_us, timer_callback_t callback, timer_t* timerid);

/**
 * 停止并删除一个定时器
 * @param timerid 需要删除的定时器ID
 * @return 0 成功，-1 失败
 */
int timer_stop(timer_t timerid);


#endif /* TIMER_H */
