# System call

[origin](https://en.wikipedia.org/wiki/System_call)

在计算机中，系统调用（通常缩写为syscall）是计算机程序向执行它的操作系统请求服务的编程方式。这可能包括与硬件相关的服务（例如访问硬盘驱动器或访问设备的摄像头），创建和执行新进程，以及与内核服务（如进程调度）的通信。系统调用提供了进程和操作系统之间的重要接口。

在大多数系统中，系统调用只能由用户空间进程发起，而在一些系统中，例如OS/360及其后续版本，特权系统代码也会发起系统调用。

大多数现代处理器的架构，除了一些嵌入式系统外，都涉及安全模型。例如，环模型指定了多个特权级别，软件可以在这些级别下执行：程序通常被限制在自己的地址空间中，以防止其访问或修改其他正在运行的程序或操作系统本身，并且通常被阻止直接操作硬件设备（例如帧缓冲区或网络设备）。

然而，许多应用程序需要访问这些组件，因此操作系统提供系统调用来提供明确定义的、安全的操作实现。操作系统在最高特权级别下执行，并允许应用程序通过系统调用请求服务，这些调用通常通过中断发起。中断会自动将CPU置于某个提升的特权级别，然后将控制权传递给内核，内核确定是否应该授予调用程序所请求的服务。如果服务被授予，内核执行一组特定的指令，调用程序无法直接控制，将特权级别返回给调用程序，并将控制权返回给调用程序。

## The library as an intermediary 图书馆作为中介

通常，系统会提供一个位于普通程序和操作系统之间的库或API。在类Unix系统中，这个API通常是C库（如glibc）的一部分，它提供了对系统调用的包装函数，这些包装函数的名称通常与它们调用的系统调用相同。在Windows NT中，这个API是Native API的一部分，位于ntdll.dll库中；这是一个未记录的API，被常规Windows API的实现所使用，并直接被Windows上的一些系统程序使用。库的包装函数使用普通的函数调用约定（在汇编级别上的子程序调用）来使用系统调用，并使系统调用更加模块化。在这里，包装函数的主要功能是将所有要传递给系统调用的参数放置在适当的处理器寄存器中（可能还包括调用堆栈），并为内核设置一个唯一的系统调用号码。通过这种方式，位于操作系统和应用程序之间的库增加了可移植性。

调用库函数本身不会导致切换到内核模式，通常是一个普通的子程序调用（例如，在某些指令集架构（ISA）中使用“CALL”汇编指令）。实际的系统调用会将控制权转移到内核（比库调用更依赖于具体实现和平台）。例如，在类Unix系统中， `fork` 和 `execve` 是C库函数，它们执行调用 `fork` 和 `exec` 系统调用的指令。在应用程序代码中直接进行系统调用更加复杂，可能需要使用嵌入式汇编代码（在C和C++中），并且需要了解系统调用操作的低级二进制接口，这可能会随着时间的推移而发生变化，因此不会成为应用程序二进制接口的一部分；库函数的目的是将这些抽象出来。

## Examples and tools 示例和工具

在Unix、类Unix和其他符合POSIX标准的操作系统上，常见的系统调用有 `open` 、 `read` 、 `write` 、 `close` 、 `wait` 、 `exec` 、 `fork` 、 `exit` 和 `kill` 。许多现代操作系统有数百个系统调用。例如，Linux和OpenBSD各自有超过300个不同的调用， [[2\]](https://en.wikipedia.org/wiki/System_call#cite_note-4) [[3\]](https://en.wikipedia.org/wiki/System_call#cite_note-5) NetBSD接近500个， [[4\]](https://en.wikipedia.org/wiki/System_call#cite_note-6) FreeBSD超过500个， [[5\]](https://en.wikipedia.org/wiki/System_call#cite_note-7) Windows接近2000个，分为win32k（图形）和ntdll（核心）系统调用 [[6\]](https://en.wikipedia.org/wiki/System_call#cite_note-8) ，而Plan 9有51个。 [[7\]](https://en.wikipedia.org/wiki/System_call#cite_note-9)

工具如strace、ftrace和truss允许一个进程从开始执行并报告该进程调用的所有系统调用，或者可以附加到一个已经运行的进程并拦截该进程进行的任何系统调用，前提是该操作不违反用户的权限。该程序的这种特殊能力通常也是通过ptrace系统调用或procfs文件上的系统调用来实现的。

## Typical implementations 典型的实施方式

实施系统调用需要从用户空间转移到内核空间，这涉及某种特定于体系结构的功能。实现这一点的典型方法是使用软件中断或陷阱。中断将控制权转移到操作系统内核，因此软件只需设置一些寄存器以获取所需的系统调用号，并执行软件中断。

## Categories of system calls 系统调用的分类

系统调用大致可以分为六个主要类别：

1. Process control 过程控制
   - create process (for example, `fork` on Unix-like systems, or `NtCreateProcess` in the [Windows NT](https://en.wikipedia.org/wiki/Windows_NT) [Native API](https://en.wikipedia.org/wiki/Native_API))
     创建进程（例如，在类Unix系统上的 `fork` ，或在Windows NT原生API中的 `NtCreateProcess` ）
   - [terminate process 终止进程](https://en.wikipedia.org/wiki/Kill_(command))
   - [load](https://en.wikipedia.org/wiki/Loader_(computing)), [execute](https://en.wikipedia.org/wiki/Exec_(operating_system)) 加载，执行
   - get/set process attributes
     获取/设置进程属性
   - [wait](https://en.wikipedia.org/wiki/Wait_(operating_system)) for time, wait event, [signal](https://en.wikipedia.org/wiki/Signal_(computing)) event
     等待时间，等待事件，信号事件
   - [allocate](https://en.wikipedia.org/wiki/Dynamic_memory_allocation) and [free](https://en.wikipedia.org/wiki/Garbage_collection_(computer_science)) memory
     分配和释放内存
2. File management 文件管理
   - create file, delete file
     创建文件，删除文件
   - open, close 打开，关闭
   - read, write, reposition 阅读，写作，重新定位
   - get/set file attributes 获取/设置文件属性
3. Device management 设备管理
   - request device, release device
     请求设备，释放设备
   - read, write, reposition 阅读，写作，重新定位
   - get/set device attributes
     获取/设置设备属性
   - logically attach or detach devices
     逻辑地连接或断开设备
4. Information maintenance 信息维护
   - get/set total system information (including time, date, computer name, enterprise etc.)
     获取/设置总系统信息（包括时间、日期、计算机名称、企业等）。
   - get/set process, file, or device metadata (including author, opener, creation time and date, etc.)
     获取/设置进程、文件或设备的元数据（包括作者、打开者、创建时间和日期等）。
5. Communication 通信
   - create, delete communication connection
     创建，删除通信连接
   - send, receive messages 发送，接收消息
   - transfer status information
     传输状态信息
   - attach or detach remote devices
     连接或断开远程设备
6. Protection 保护
   - get/set file permissions 获取/设置文件权限

## Processor mode and context switching 处理器模式和上下文切换

大多数类Unix系统中的系统调用在内核模式下进行处理，这是通过将处理器执行模式更改为更高特权的模式来实现的，但不需要进行进程上下文切换-尽管会发生特权上下文切换。硬件根据处理器状态寄存器以执行模式的方式来看待世界，而进程是操作系统提供的一种抽象。系统调用通常不需要切换到另一个进程的上下文，而是在调用它的进程的上下文中进行处理。