## makefile的规则

```makefile
target ... : prerequisites ...
    recipe
    ...
    ...
```

- target

  可以是一个object file（目标文件），也可以是一个可执行文件，还可以是一个标签（label）。对于标签这种特性，在后续的“伪目标”章节中会有叙述。

- prerequisites

  生成该target所依赖的文件和/或target。

- recipe

  该target要执行的命令（任意的shell命令）。

这是一个文件的依赖关系，也就是说，target这一个或多个的目标文件依赖于prerequisites中的文件，其生成规则定义在command中。说白一点就是说:

```
prerequisites中如果有一个以上的文件比target文件要新的话，recipe所定义的命令就会被执行。
```

反斜杠（ `\` ）是换行符的意思。这样比较便于makefile的阅读。

我们可以把这个内容保存在名字为“makefile”或“Makefile”的文件中，然后在该目录下直接输入命令 `make` 就可以生成执行文件edit。

make并不管命令是怎么工作的，他只管执行所定义的命令。make会比较targets文件和prerequisites文件的修改日期，如果prerequisites文件的日期要比targets文件的日期要新，或者target不存在的话，那么，make就会执行后续定义的命令。

## make是如何工作的[¶](https://seisman.github.io/how-to-write-makefile/introduction.html#make)

在默认的方式下，也就是我们只输入 `make` 命令。那么，

1. make会在当前目录下找名字叫“Makefile”或“makefile”的文件。
2. 如果找到，它会找文件中的第一个目标文件（target）
3. 如果第一个目标文件（target）不存在，或是edit所依赖的后面的文件的文件修改时间要比第一个目标文件（target）新，那么，他就会执行后面所定义的命令来生成第一个目标文件（target）。
4. 如果第一个目标文件（target）所依赖的文件也不存在，那么make会在当前文件中找目标为文件的依赖性，如果找到则再根据那一个规则生成依赖文件。（这有点像一个堆栈的过程）

## makefile中使用变量

为了makefile的易维护，在makefile中我们可以使用变量。makefile的变量也就是一个字符串，理解成C语言中的宏可能会更好。

```
objects = main.o kbd.o command.o display.o \
     insert.o search.o files.o utils.o
```

我们就可以很方便地在我们的makefile中以 `$(objects)` 的方式来使用这个变量了

```
objects = main.o kbd.o command.o display.o \
    insert.o search.o files.o utils.o

edit : $(objects)
    cc -o edit $(objects)
```

## 让make自动推导

只要make看到一个 `.o` 文件，它就会自动的把 `.c` 文件加在依赖关系中，如果make找到一个`whatever.o` ，那么 `whatever.c` 就会是 `whatever.o` 的依赖文件。并且 `cc -c whatever.c` 也会被推导出来，于是，我们的makefile再也不用写得这么复杂。我们的新makefile又出炉了。

## 清空目录的规则[¶](https://seisman.github.io/how-to-write-makefile/introduction.html#id6)

每个Makefile中都应该写一个清空目标文件（ `.o` ）和可执行文件的规则，这不仅便于重编译，也很利于保持文件的清洁。这是一个“修养”（呵呵，还记得我的《编程修养》吗）。一般的风格都是：

```
clean:
    rm edit $(objects)
```

更为稳健的做法是：

```
.PHONY : clean
clean :
    -rm edit $(objects)
```

前面说过， `.PHONY` 表示 `clean` 是一个“伪目标”。而在 `rm` 命令前面加了一个小减号的意思就是，也许某些文件出现问题，但不要管，继续做后面的事。当然， `clean` 的规则不要放在文件的开头，不然，这就会变成make的默认目标，相信谁也不愿意这样。不成文的规矩是——“clean从来都是放在文件的最后”。

## Makefile里有什么？[¶](https://seisman.github.io/how-to-write-makefile/introduction.html#id7)

Makefile里主要包含了五个东西：显式规则、隐式规则、变量定义、指令和注释。

1. 显式规则。显式规则说明了如何生成一个或多个目标文件。这是由Makefile的书写者明显指出要生成的文件、文件的依赖文件和生成的命令。
2. 隐式规则。由于我们的make有自动推导的功能，所以隐式规则可以让我们比较简略地书写Makefile，这是由make所支持的。
3. 变量的定义。在Makefile中我们要定义一系列的变量，变量一般都是字符串，这个有点像你C语言中的宏，当Makefile被执行时，其中的变量都会被扩展到相应的引用位置上。
4. 指令。其包括了三个部分，一个是在一个Makefile中引用另一个Makefile，就像C语言中的include一样；另一个是指根据某些情况指定Makefile中的有效部分，就像C语言中的预编译#if一样；还有就是定义一个多行的命令。有关这一部分的内容，我会在后续的部分中讲述。
5. 注释。Makefile中只有行注释，和UNIX的Shell脚本一样，其注释是用 `#` 字符，这个就像C/C++中的 `//` 一样。如果你要在你的Makefile中使用 `#` 字符，可以用反斜杠进行转义，如： `\#` 。

最后，还值得一提的是，在Makefile中的命令，必须要以 `Tab` 键开始。

## Makefile的文件名[¶](https://seisman.github.io/how-to-write-makefile/introduction.html#id8)

默认的情况下，make命令会在当前目录下按顺序寻找文件名为 `GNUmakefile` 、 `makefile` 和`Makefile` 的文件。在这三个文件名中，最好使用 `Makefile` 这个文件名，因为这个文件名在排序上靠近其它比较重要的文件，比如 `README`。最好不要用 `GNUmakefile`，因为这个文件名只能由GNU `make` ，其它版本的 `make` 无法识别，但是基本上来说，大多数的 `make` 都支持 `makefile` 和 `Makefile` 这两种默认文件名。

当然，你可以使用别的文件名来书写Makefile，比如：“Make.Solaris”，“Make.Linux”等，如果要指定特定的Makefile，你可以使用make的 `-f` 或 `--file` 参数，如： `make -f Make.Solaris` 或 `make--file Make.Linux` 。如果你使用多条 `-f` 或 `--file` 参数，你可以指定多个makefile。

## 包含其它Makefile[¶](https://seisman.github.io/how-to-write-makefile/introduction.html#id9)

在Makefile使用 `include` 指令可以把别的Makefile包含进来，这很像C语言的 `#include` ，被包含的文件会原模原样的放在当前文件的包含位置。 `include` 的语法是：

```
include <filenames>...
```

`<filenames>` 可以是当前操作系统Shell的文件模式（可以包含路径和通配符）。

make命令开始时，会找寻 `include` 所指出的其它Makefile，并把其内容安置在当前的位置。就好像C/C++的 `#include` 指令一样。如果文件都没有指定绝对路径或是相对路径的话，make会在当前目录下首先寻找，如果当前目录下没有找到，那么，make还会在下面的几个目录下找：

1. 如果make执行时，有 `-I` 或 `--include-dir` 参数，那么make就会在这个参数所指定的目录下去寻找。
2. 接下来按顺序寻找目录 `<prefix>/include` （一般是 `/usr/local/bin` ）、 `/usr/gnu/include` 、 `/usr/local/include` 、 `/usr/include` 。

环境变量 `.INCLUDE_DIRS` 包含当前 make 会寻找的目录列表。你应当避免使用命令行参数 `-I` 来寻找以上这些默认目录，否则会使得 `make` “忘掉”所有已经设定的包含目录，包括默认目录。

## 环境变量MAKEFILES[¶](https://seisman.github.io/how-to-write-makefile/introduction.html#makefiles)

如果你的当前环境中定义了环境变量 `MAKEFILES` ，那么make会把这个变量中的值做一个类似于`include` 的动作。这个变量中的值是其它的Makefile，用空格分隔。只是，它和 `include` 不同的是，从这个环境变量中引入的Makefile的“默认目标”(the default goal)不会起作用，如果环境变量中定义的文件发现错误，make也会不理。

## make的工作方式[¶](https://seisman.github.io/how-to-write-makefile/introduction.html#id10)

GNU的make工作时的执行步骤如下：（想来其它的make也是类似）

1. 读入所有的Makefile。
2. 读入被include的其它Makefile。
3. 初始化文件中的变量。
4. 推导隐式规则，并分析所有规则。
5. 为所有的目标文件创建依赖关系链。
6. 根据依赖关系，决定哪些目标要重新生成。
7. 执行生成命令。