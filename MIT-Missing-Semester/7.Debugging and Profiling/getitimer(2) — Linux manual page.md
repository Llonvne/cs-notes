# getitimer(2) — Linux manual page

```
getitimer，setitimer - 获取或设置间隔计时器的值
```

## SYNOPSIS     [top](https://man7.org/linux/man-pages/man2/setitimer.2.html#top_of_page) 概要

```
 #include <sys/time.h>
       int getitimer(int which, struct itimerval *curr_value);
       int setitimer(int which, const struct itimerval *restrict new_value,
                     struct itimerval *_Nullable restrict old_value);
```

```
获取计时器的值，设置计时器的值
```

## DESCRIPTION

```
这些系统调用提供对间隔定时器的访问，即最初在将来某个时间点到期，并且（可选地）在此之后以固定间隔到期。当定时器到期时，为调用进程生成一个信号，并将定时器重置为指定的间隔（如果间隔不为零）。
```

```
提供了三种类型的定时器，通过which参数指定，每种类型的定时器都针对不同的时钟进行计数，并在定时器到期时生成不同的信号
```

```
ITIMER_REAL
ITIMER_REAL这个计时器以实际（即挂钟）时间倒计时。每次到期时，会生成一个SIGALRM信号。
```

```
ITIMER_VIRTUAL
ITIMER_VIRTUAL这个计时器根据进程消耗的用户模式CPU时间进行倒计时。（该测量包括进程中所有线程消耗的CPU时间。）每次到期时，会生成一个SIGVTALRM信号。
```

```
ITIMER_PROF
ITIMER_PROF这个计时器根据进程消耗的总CPU时间（包括用户和系统）进行倒计时。（该测量包括进程中所有线程消耗的CPU时间。）每次到期时，都会生成一个SIGPROF信号。
与ITIMER_VIRTUAL结合使用，该计时器可用于分析进程消耗的用户和系统CPU时间。
```

