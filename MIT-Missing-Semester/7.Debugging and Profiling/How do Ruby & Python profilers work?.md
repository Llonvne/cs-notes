# How do Ruby & Python profilers work?

那就是“你如何编写一个分析器？”

我们只关注CPU分析器（而不是内存/堆分析器）。我将解释一些编写分析器的基本通用方法，给出一些代码示例，并介绍一些流行的Ruby和Python分析器的工作原理。

### 2 kinds of profilers

有两种基本类型的CPU分析器 - 采样分析器和跟踪分析器。

追踪分析器记录程序的每个函数调用，并在最后打印出报告。采样分析器采用更统计的方法 - 它们每隔几毫秒记录程序的堆栈，然后报告结果。

### The profilers 分析人员

这是我们将在本文中讨论的分析工具的摘要（来自这个要点）。稍后我会解释表格中的术语（ `setitimer` ， `rb_add_event_hook` ， `ptrace` ）。有趣的是，所有的分析工具都是使用一套相当小的基本功能实现的。

### 几乎所有这些分析工具都存在于您的进程内部

有一件非常重要的事情 - 除了 `pyflame` 之外，所有这些分析器都在你的Python/Ruby进程内运行。如果你在一个Python/Ruby程序内部，你通常很容易访问它的堆栈。

大多数这些分析器都是为了性能而编写的C扩展，所以它们有些不同，但是Ruby/Python程序的C扩展也可以很容易地访问调用堆栈。

### 追踪分析器的工作原理

`rblineprof` ， `ruby-prof` ， `line_profiler` 和 `cProfile` 。它们的工作原理基本相同。它们都记录所有函数调用，并且都是以C扩展的形式编写，以减少开销。

它们是如何工作的？嗯，Ruby和Python都允许您指定一个回调函数，在发生各种解释器事件（如“调用函数”或“执行一行代码”）时运行。当回调被调用时，它会记录堆栈以供以后分析。

在Python中，您可以使用 `PyEval_SetTrace` 或 `PyEval_SetProfile` 来设置回调函数。这在Python文档的“性能分析和跟踪”部分有详细说明。文档中说：“ `PyEval_SetTrace` 与 `PyEval_SetProfile` 类似，只是跟踪函数会接收行号事件。”

The code: 代码：

- `line_profiler` sets up its callback using `PyEval_SetTrace`: see [line_profiler.pyx line 157](https://github.com/rkern/line_profiler/blob/4e3ce5957932806da86cbe27c75470c105d51acf/_line_profiler.pyx#L157-L158)
  `line_profiler` 使用 `PyEval_SetTrace` 设置了它的回调函数：参见line_profiler.pyx的第157行。
- `cProfile` sets up its callback using `PyEval_SetProfile`: see [_lsprof.c line 693](https://github.com/python/cpython/blob/1b7c11ff0ee3efafbf5b38c3c6f37de5d63efb81/Modules/_lsprof.c#L693) (cProfile is [implemented using lsprof](https://github.com/python/cpython/blob/1b7c11ff0ee3efafbf5b38c3c6f37de5d63efb81/Lib/cProfile.py#L9))
  使用 `PyEval_SetProfile` 设置回调函数：参见_lsprof.c的第693行（cProfile是使用lsprof实现的）

在Ruby中，你可以使用 `rb_add_event_hook` 来设置一个回调函数。我找不到任何关于这个的文档，但是下面是它的调用方式。

```
rb_add_event_hook(prof_event_hook,
      RUBY_EVENT_CALL | RUBY_EVENT_RETURN |
      RUBY_EVENT_C_CALL | RUBY_EVENT_C_RETURN |
      RUBY_EVENT_LINE, self);
```

### Disadvantages of tracing profilers 追踪分析器的缺点

追踪分析器以这种方式实现的主要缺点是，它们为每个函数调用/执行的代码行引入了固定的开销。这可能导致您做出错误的决策！例如，如果您有两个实现某个功能的方法 - 一个有很多函数调用，一个没有，但它们花费的时间相同，那么在进行分析时，有很多函数调用的方法会显得更慢。

为了测试一下，我创建了一个名为 `test.py` 的小文件，其中包含以下内容，并比较了 `python -mcProfile test.py` 和 `python test.py` 的运行时间。 `python test.py` 运行时间约为0.6秒，而 `python -mcProfile test.py` 运行时间约为1秒。因此，对于这个特殊的病态示例， `cProfile` 引入了额外的约60%的开销。

```python
def recur(n):
    if n == 0:
        return
    recur(n-1)

for i in range(5000):
    recur(700)
```

> 大多数程序在高度递归的情况下（如斐波那契数列测试）运行速度大约会慢两倍，而高度递归的程序则会慢三倍。

### How sampling profilers mostly work: setitimer 如何大多数采样分析器工作：setitimer

大多数Ruby和Python的采样分析器是使用 `setitimer` 系统调用实现的。那是什么？

假设你想每秒获取程序堆栈的快照50次。一种方法是：

* 请Linux内核每20毫秒向您发送一个信号（使用 `setitimer` 系统调用）

* 注册一个信号处理程序，每次收到信号时记录堆栈。
* 当你完成分析时，请请求Linux停止向你发送信号并打印输出！

If you want to see a practical example of `setitimer` being used to implement a sampling profiler, I think [stacksampler.py](https://github.com/nylas/nylas-perftools/blob/2e9f72ee74587e0dea5ba4826cd60a093c8869f0/stacksampler.py) is the best example – it’s a useful, working, profiler, and it’s only about 100 lines of Python. So cool!
如果你想看一个使用 `setitimer` 来实现采样分析器的实际例子，我认为stacksampler.py是最好的例子 - 它是一个有用的、可工作的分析器，而且只有大约100行的Python代码。太酷了！

One important thing about `setitimer` is that you need to decide **how to count time**. Do you want 20ms of real “wall clock” time? 20ms of user CPU time? 20 ms of user + system CPU time? If you look closely at the call sites above you’ll notice that these profilers actually make different choices about how to `setitimer` – sometimes it’s configurable, and sometimes it’s not. The [setitimer man page](http://man7.org/linux/man-pages/man2/setitimer.2.html) is short and worth reading to understand all the options.
关于 `setitimer` 的一个重要事项是你需要决定如何计算时间。你想要20毫秒的真实的“挂钟”时间吗？20毫秒的用户CPU时间？20毫秒的用户+系统CPU时间？如果你仔细观察上面的调用点，你会注意到这些性能分析器实际上在如何 `setitimer`上做出了不同的选择 - 有时它是可配置的，有时它是不可配置的。setitimer手册很简短，值得阅读以了解所有选项。

> setitimer基于的性能分析器的一个有趣的缺点是定时器会引发信号！信号有时会中断系统调用！系统调用有时需要几毫秒！如果采样太频繁，你的程序可能会一直重试相同的系统调用！
>
> When you're profiling a view that uses `subprocess.Popen()`, it might livelock:
> 当您对使用 `subprocess.Popen()` 的视图进行分析时，可能会出现活锁：
>
> - the `clone()` syscall (used to implement `os.fork()` under the hood) may take 2-3 milliseconds on my machine (as measured by `strace -T` while the flamegraph was off)
>   `clone()` 系统调用（在底层实现 `os.fork()` ）在我的机器上可能需要2-3毫秒（由 `strace -T` 在火焰图关闭时测量）
> - a SIGALRM arrives every 1 ms and interrupts the `clone()`
>   每1毫秒就会收到一个SIGALRM信号并中断 `clone()`
> - `clone()` returns -EINTR `clone()` 返回 -EINTR
> - the signal handler runs
>   信号处理程序运行
> - `clone()` is then restarted
>   然后重新启动
> - go to step 1
>   前往第一步



### 不使用setitimer的采样分析器

- `pyinstrument` uses `PyEval_SetProfile` (so it’s sort of a tracing profiler in a way), but it doesn’t always collect stack samples when its tracing callback is called. Here’s [the code that chooses when to sample a stack trace](https://github.com/joerick/pyinstrument/blob/15b94a63693837b97daea60e717ae835f77b7635/pyinstrument/profiler.py#L41-L45) See [this blog post](http://joerick.me/posts/2017/12/15/pyinstrument-20/) for more on that decision. (basically: `setitimer` only lets you profile the main thread in Python)
  `pyinstrument` 使用 `PyEval_SetProfile` （所以在某种程度上它是一种追踪分析器），但它并不总是在调用追踪回调时收集堆栈样本。以下是选择何时采样堆栈跟踪的代码。有关该决策的更多信息，请参阅此博文。（基本上：在Python中， `setitimer` 只允许您对主线程进行分析）
- `pyflame` profiles Python code from outside of the process using the `ptrace`system call. It basically just does a loop where it grabs samples, sleeps, and repeats. Here’s the [call to sleep](https://github.com/uber/pyflame/blob/4a9c3dea4939261b0c1becb77ec700426aa1f2fb/src/prober.cc#L403).
  使用系统调用 `ptrace` ，从进程外部对Python代码进行分析。基本上只是一个循环，它获取样本，休眠，然后重复。这是休眠的调用。
- `python-flamegraph` takes a similar approach where it starts a new thread in your Python process and basically grabs stack traces, sleeps, and repeats. Here’s the [call to sleep](https://github.com/evanhempel/python-flamegraph/blob/6b70f9068cb987a2b1942fbf048fc88a7a644c40/flamegraph/flamegraph.py#L73).
  `python-flamegraph` 采用类似的方法，在Python进程中启动一个新线程，基本上获取堆栈跟踪，休眠并重复。这是调用sleep的地方。

