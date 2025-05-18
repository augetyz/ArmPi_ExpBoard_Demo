
/* timer.c */
#include "timer.h"
#include <stdlib.h>
#include <string.h>
#include <errno.h>

int timer_start(long interval_us, timer_callback_t callback, timer_t* timerid)
{
    if (interval_us <= 0 || callback == NULL || timerid == NULL)
    {
        errno = EINVAL;
        return -1;
    }

    struct sigevent sev;
    memset(&sev, 0, sizeof(sev));
    sev.sigev_notify = SIGEV_THREAD;
    sev.sigev_value.sival_ptr = timerid;
    sev.sigev_notify_function = callback;
    sev.sigev_notify_attributes = NULL;  // 默认线程属性

    // 创建定时器
    if (timer_create(CLOCK_REALTIME, &sev, timerid) == -1)
    {
        return -1;
    }

    // 设置首次触发和周期
    struct itimerspec its;
    its.it_value.tv_sec = interval_us / 1000000;
    its.it_value.tv_nsec = (interval_us % 1000000) * 1000;
    its.it_interval = its.it_value;  // 周期性

    if (timer_settime(*timerid, 0, &its, NULL) == -1)
    {
        timer_delete(*timerid);
        return -1;
    }

    return 0;
}

int timer_stop(timer_t timerid)
{
    if (timer_delete(timerid) == -1)
    {
        return -1;
    }
    return 0;
}