# [pdb-tutorial](https://github.com/spiside/pdb-tutorial)

With a debugger, you can:
使用调试器，您可以：

- Explore the state of a running program
  探索正在运行的程序的状态
- Test implementation code before applying it
  在应用之前测试实施代码
- Follow the program's execution logic
  按照程序的执行逻辑进行操作

首先，我们需要导入 `pdb` 模块，然后调用其中的一个方法在程序中添加一个调试断点。通常的做法是在你想要停下来的那一行同时添加导入和调用方法。这是你需要包含的完整语句：

```
import pdb; pdb.set_trace()
```

Starting from version 3.7: The built-in function `breakpoint()` can be used instead of using `import pdb; pdb.set_trace()`
从版本3.7开始：可以使用内置函数 `breakpoint()` 来替代使用 `import pdb; pdb.set_trace()` 。

```
breakpoint()
```

## The 5 `pdb` commands that will leave you "speechless"

从文档中直接提取，这是五个命令，一旦你学会了它们，你就会不知道没有它们你是如何生活的。

1. `l(ist)` - Displays 11 lines around the current line or continue the previous listing.
   `l(ist)` - 显示当前行周围的11行或继续上一个列表。
2. `s(tep)` - Execute the current line, stop at the first possible occasion.
   `s(tep)` - 执行当前行，在第一个可能的机会停止。
3. `n(ext)` - Continue execution until the next line in the current function is reached or it returns.
   \- 继续执行，直到当前函数中的下一行被执行或者函数返回。
4. `b(reak)` - Set a breakpoint (depending on the argument provided).
   `b(reak)` - 设置一个断点（根据提供的参数）。
5. `r(eturn)` - Continue execution until the current function returns.
   \- 继续执行，直到当前函数返回。

注意每个关键字的最后部分都有括号。括号表示在使用命令提示符时，单词的其余部分是可选的。这样可以节省打字的时间，但一个重要的注意事项是，如果你有一个变量名，比如 `l` 或 `n` ，那么 `pdb` 命令会优先执行。也就是说，假设你的程序中有一个名为 `c` 的变量，你想知道 `c` 的值。如果你在 `pdb` 中输入 `c` ，实际上你将执行 `c(ontinue)` 关键字，该关键字只有在遇到断点时才会停止执行程序！

NNB: 另一个有用的工具是以下内容: `h(elp) - Without argument, print the list of available commands. With a command as an argument, print help about that command.`

### 1. l(ist) a.k.a. I'm too lazy to open the file containing the source code 1. 列表，也就是说我懒得打开包含源代码的文件

注意：在Python 3.2及以上版本中，您可以键入 `ll` （长列表），它会显示当前函数或帧的源代码。我经常使用这个而不是 `l` ，因为知道自己在哪个函数中比知道当前位置周围的任意11行代码更有用。

### 2. `s(tep)` a.k.a let's see what this method does... 2. 看看这个方法做了什么...

### 3. `n(ext)` a.k.a I hope this current line doesn't throw an exception 3. `n(ext)` 又名我希望当前行不会抛出异常

注意： `n(ext)` 允许您跳过函数调用，而 `s(tep)` 允许您单步执行函数调用并在被调用函数的第一行暂停。

### 4. `b(reak)` a.k.a I don't want to type `n` anymore 4. `b(reak)` 又名我不想再输入 `n`

我们希望在 `for` 循环之后设置一个断点，以便我们可以继续浏览 `run()` 方法。让我们在 `:34` 上停止，因为它具有输入函数，无论如何它都会中断并等待用户输入。为此，我们可以键入 `b 34` ，然后键入 `continue` 到断点。

我们还可以通过调用不带任何参数的 `break` 来查看我们设置的断点。

要清除断点，可以使用 `cl(ear)` 命令，后跟断点编号，断点编号可在上述输出的最左列中找到。现在让我们通过调用 `clear` 命令后跟 1 来清除断点。

注意：如果不向 `clear` 命令提供任何参数，您也可以清除所有断点。

### 5. `r(eturn)` 又名我想退出这个函数

### `!` （爆炸）命令

bang 命令 ( `!` ) 让 `pdb` 知道以下语句将是 Python 命令而不是 `pdb` 命令。这在带有 `c` 变量的 `run()` 方法中很有帮助。正如我在教程开头提到的，在 `pdb` 中调用 `c` 将发出 `continue` 命令。在 `pdb` REPL 中导航，停在 `runner.py` 文件中的 `:26` 处，从该点开始，您可以在 `c` 前面加上 `!` 命令看看会发生什么。

```pdb
 (Pdb) !c
 0
```

### The `commands` command `commands` 命令

```
commands [bpnumber]
        (com) ...
        (com) end
        (Pdb)

        Specify a list of commands for breakpoint number bpnumber.
```

`commands` 将在遇到指定的断点编号时运行您指定的 python 代码或 pdb 命令。启动 `commands` 块后，提示符将更改为 `(com)` 。您在此处编写的代码/命令的功能就好像您在到达该断点后在 `(Pdb)` 提示符处键入它们一样。写入 `end` 将终止命令，提示符从 `(com)` 变回 `(Pdb)` 。当我需要监视循环内的某些变量时，我发现这非常有用，因为我不需要重复打印变量的值。让我们看一个例子。确保位于终端中项目的根目录并输入以下内容：

`commands` 将在遇到指定的断点编号时运行您指定的 python 代码或 pdb 命令。启动 `commands` 块后，提示符将更改为 `(com)` 。您在此处编写的代码/命令的功能就好像您在到达该断点后在 `(Pdb)` 提示符处键入它们一样。写入 `end` 将终止命令，提示符从 `(com)` 变回 `(Pdb)` 。当我需要监视循环内的某些变量时，我发现这非常有用，因为我不需要重复打印变量的值。让我们看一个例子。确保位于终端中项目的根目录并输入以下内容：

### `pdb` Post Mortem `pdb` 事后分析

虽然这两种方法可能看起来相同，但 `post_mortem() and pm()` 的不同之处在于它们给出的回溯。我通常在 `except` 块中使用 `post_mortem()` 。不过，我们将介绍 `pm()` 方法，因为我发现它更强大一些。让我们尝试看看这在实践中是如何运作的。

在异常时，从 `pdb` 模块调用 `pm()` 方法，看看会发生什么。

看那个！我们从上次抛出异常的位置恢复并放置在 `pdb` 提示符中。从这里，我们可以检查程序崩溃之前的状态，这将有助于您的调查。

注意：您还可以使用 `python -m pdb main.py` 和 `continue` 启动 `main.py` 脚本，直到引发异常。 Python会在未捕获的异常处自动进入 `post_mortem` 模式。
