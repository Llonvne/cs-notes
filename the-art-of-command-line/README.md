# [the-art-of-command-line](https://github.com/jlevy/the-art-of-command-line/tree/master)

- 在 Bash 中，可以通过按 **Tab** 键实现自动补全参数，使用 **ctrl-r** 搜索命令行历史记录（按下按键之后，输入关键字便可以搜索，重复按下 **ctrl-r** 会向后查找匹配项，按下 **Enter** 键会执行当前匹配的命令，而按下右方向键会将匹配项放入当前行中，不会直接执行，以便做出修改）。

- 在 Bash 中，可以按下 **ctrl-w** 删除你键入的最后一个单词，**ctrl-u** 可以删除行内光标所在位置之前的内容，**alt-b** 和 **alt-f** 可以以单词为单位移动光标，**ctrl-a** 可以将光标移至行首，**ctrl-e** 可以将光标移至行尾，**ctrl-k** 可以删除光标至行尾的所有内容，**ctrl-l** 可以清屏。键入 `man readline` 可以查看 Bash 中的默认快捷键。内容有很多，例如 **alt-.** 循环地移向前一个参数，而 **alt-*** 可以展开通配符。

- 键入 `history` 查看命令行历史记录，再用 `!n`（`n` 是命令编号）就可以再次执行。其中有许多缩写，最有用的大概就是 `!$`， 它用于指代上次键入的参数，而 `!!` 可以指代上次键入的命令了（参考 man 页面中的“HISTORY EXPANSION”）。不过这些功能，你也可以通过快捷键 **ctrl-r** 和 **alt-.** 来实现。
- 回到前一个工作路径：`cd -`。

- 使用 `pgrep` 和 `pkill` 根据名字查找进程或发送信号（`-f` 参数通常有用）。
- 使用 `nohup` 或 `disown` 使一个后台进程持续运行。

- 使用 `netstat -lntp` 或 `ss -plat` 检查哪些进程在监听端口（默认是检查 TCP 端口; 添加参数 `-u` 则检查 UDP 端口）或者 `lsof -iTCP -sTCP:LISTEN -P -n` (这也可以在 OS X 上运行)。

- 在 Bash 脚本中，子 shell（使用括号 `(...)`）是一种组织参数的便捷方式。一个常见的例子是临时地移动工作路径，代码如下：
- 使用括号扩展（`{`...`}`）来减少输入相似文本，并自动化文本组合。这在某些情况下会很有用，例如 `mv foo.{txt,pdf} some-dir`（同时移动两个文件），`cp somefile{,.bak}`（会被扩展成 `cp somefile somefile.bak`）或者 `mkdir -p test-{a,b,c}/subtest-{1,2,3}`（会被扩展成所有可能的组合，并创建一个目录树）。

- 编写脚本时，你可能会想要把代码都放在大括号里。缺少右括号的话，代码就会因为语法错误而无法执行。如果你的脚本是要放在网上分享供他人使用的，这样的写法就体现出它的好处了，因为这样可以防止下载不完全代码被执行。

- 使用 [`percol`](https://github.com/mooz/percol) 或者 [`fzf`](https://github.com/junegunn/fzf) 可以交互式地从另一个命令输出中选取值。
- 使用 `fpp`（[PathPicker](https://github.com/facebook/PathPicker)）可以与基于另一个命令(例如 `git`）输出的文件交互。
- 将 web 服务器上当前目录下所有的文件（以及子目录）暴露给你所处网络的所有用户，使用： `python -m SimpleHTTPServer 7777` （使用端口 7777 和 Python 2）或`python -m http.server 7777` （使用端口 7777 和 Python 3）。

- 以其他用户的身份执行命令，使用 `sudo`。默认以 root 用户的身份执行；使用 `-u` 来指定其他用户。使用 `-i` 来以该用户登录（需要输入_你自己的_密码）。
- 将 shell 切换为其他用户，使用 `su username` 或者 `su - username`。加入 `-` 会使得切换后的环境与使用该用户登录后的环境相同。省略用户名则默认为 root。切换到哪个用户，就需要输入_哪个用户的_密码。

## 文件及数据处理

- 使用 [`ag`](https://github.com/ggreer/the_silver_searcher) 在源代码或数据文件里检索（`grep -r` 同样可以做到，但相比之下 `ag` 更加先进）。
- 将 HTML 转为文本：`lynx -dump -stdin`。

- 当你要处理棘手的 XML 时候，`xmlstarlet` 算是上古时代流传下来的神器。

- 使用 [`jq`](http://stedolan.github.io/jq/) 处理 JSON。
- 使用 [`shyaml`](https://github.com/0k/shyaml) 处理 YAML。
- 要处理 Excel 或 CSV 文件的话，[csvkit](https://github.com/onyxfish/csvkit) 提供了 `in2csv`，`csvcut`，`csvjoin`，`csvgrep` 等方便易用的工具。
- 当你要处理 Amazon S3 相关的工作的时候，[`s3cmd`](https://github.com/s3tools/s3cmd) 是一个很方便的工具而 [`s4cmd`](https://github.com/bloomreach/s4cmd) 的效率更高。Amazon 官方提供的 [`aws`](https://github.com/aws/aws-cli) 以及 [`saws`](https://github.com/donnemartin/saws) 是其他 AWS 相关工作的基础，值得学习。
- 了解如何使用 `sort` 和 `uniq`，包括 uniq 的 `-u` 参数和 `-d` 参数，具体内容在后文单行脚本节中。另外可以了解一下 `comm`。

- 了解如何使用 `cut`，`paste` 和 `join` 来更改文件。很多人都会使用 `cut`，但遗忘了 `join`。
- 了解如何运用 `wc` 去计算新行数（`-l`），字符数（`-m`），单词数（`-w`）以及字节数（`-c`）。
- 了解如何使用 `tee` 将标准输入复制到文件甚至标准输出，例如 `ls -al | tee file.txt`。
- 要进行一些复杂的计算，比如分组、逆序和一些其他的统计分析，可以考虑使用 [`datamash`](https://www.gnu.org/software/datamash/)。
- 了解如何使用 `awk` 和 `sed` 来进行简单的数据处理。 参阅 [One-liners](https://github.com/jlevy/the-art-of-command-line/blob/master/README-zh.md#one-liners) 获取示例。

- 使用 [`repren`](https://github.com/jlevy/repren) 来批量重命名文件，或是在多个文件中搜索替换内容。（有些时候 `rename` 命令也可以批量重命名，但要注意，它在不同 Linux 发行版中的功能并不完全一样。）

```
      # 将文件、目录和内容全部重命名 foo -> bar:
      repren --full --preserve-case --from foo --to bar .
      # 还原所有备份文件 whatever.bak -> whatever:
      repren --renames --from '(.*)\.bak' --to '\1' *.bak
      # 用 rename 实现上述功能（若可用）:
      rename 's/\.bak$//' *.bak
```

- 若要在复制文件时获取当前进度，可使用 `pv`，[`pycp`](https://github.com/dmerejkowsky/pycp)，[`progress`](https://github.com/Xfennec/progress)，`rsync --progress`。若所执行的复制为block块拷贝，可以使用 `dd status=progress`。
- 对于二进制文件，使用 `hd`，`hexdump` 或者 `xxd` 使其以十六进制显示，使用 `bvi`，`hexedit` 或者 `biew` 来进行二进制编辑。

- 同样对于二进制文件，`strings`（包括 `grep` 等工具）可以帮助在二进制文件中查找特定比特。
- 制作二进制差分文件（Delta 压缩），使用 `xdelta3`。

- 使用 `zless`、`zmore`、`zcat` 和 `zgrep` 对压缩过的文件进行操作。
- `curl` 和 `curl -I` 可以被轻松地应用于 web 调试中，它们的好兄弟 `wget` 也是如此，或者也可以试试更潮的 [`httpie`](https://github.com/jkbrzt/httpie)。

- 获取 CPU 和硬盘的使用状态，通常使用使用 `top`（`htop` 更佳），`iostat` 和 `iotop`。而 `iostat -mxz 15` 可以让你获悉 CPU 和每个硬盘分区的基本信息和性能表现。
- 使用 `netstat` 和 `ss` 查看网络连接的细节。
- `dstat` 在你想要对系统的现状有一个粗略的认识时是非常有用的。然而若要对系统有一个深度的总体认识，使用 [`glances`](https://github.com/nicolargo/glances)，它会在一个终端窗口中向你提供一些系统级的数据。
- 若要了解内存状态，运行并理解 `free` 和 `vmstat` 的输出。值得留意的是“cached”的值，它指的是 Linux 内核用来作为文件缓存的内存大小，而与空闲内存无关。
- Java 系统调试则是一件截然不同的事，一个可以用于 Oracle 的 JVM 或其他 JVM 上的调试的技巧是你可以运行 `kill -3 <pid>` 同时一个完整的栈轨迹和堆概述（包括 GC 的细节）会被保存到标准错误或是日志文件。JDK 中的 `jps`，`jstat`，`jstack`，`jmap` 很有用。[SJK tools](https://github.com/aragozin/jvm-tools) 更高级。

- 使用 [`mtr`](http://www.bitwizard.nl/mtr/) 去跟踪路由，用于确定网络问题。

- 用 [`ncdu`](https://dev.yorhel.nl/ncdu) 来查看磁盘使用情况，它比寻常的命令，如 `du -sh *`，更节省时间。

- `ab` 工具（Apache 中自带）可以简单粗暴地检查 web 服务器的性能。对于更复杂的负载测试，使用 `siege`。

- 学会使用 `/proc`。它在调试正在出现的问题的时候有时会效果惊人。比如：`/proc/cpuinfo`，`/proc/meminfo`，`/proc/cmdline`，`/proc/xxx/cwd`，`/proc/xxx/exe`，`/proc/xxx/fd/`，`/proc/xxx/smaps`（这里的 `xxx` 表示进程的 id 或 pid）。

- 当调试一些之前出现的问题的时候，[`sar`](http://sebastien.godard.pagesperso-orange.fr/) 非常有用。它展示了 cpu、内存以及网络等的历史数据。

- 查看你当前使用的系统，使用 `uname`，`uname -a`（Unix／kernel 信息）或者 `lsb_release -a`（Linux 发行版信息）。

- ## 单行脚本

- 如果你想在文件树上查看大小/日期，这可能看起来像递归版的 `ls -l` 但比 `ls -lR` 更易于理解：

```
find . -type f -ls
```

## 仅限 OS X 系统

- 用 `brew` （Homebrew）或者 `port` （MacPorts）进行包管理。这些可以用来在 OS X 系统上安装以上的大多数命令。
- 用 `pbcopy` 复制任何命令的输出到桌面应用，用 `pbpaste` 粘贴输入。
- 若要在 OS X 终端中将 Option 键视为 alt 键（例如在上面介绍的 **alt-b**、**alt-f** 等命令中用到），打开 偏好设置 -> 描述文件 -> 键盘 并勾选“使用 Option 键作为 Meta 键”。
- 用 `open` 或者 `open -a /Applications/Whatever.app` 使用桌面应用打开文件。
- Spotlight：用 `mdfind` 搜索文件，用 `mdls` 列出元数据（例如照片的 EXIF 信息）。
- 注意 OS X 系统是基于 BSD UNIX 的，许多命令（例如 `ps`，`ls`，`tail`，`awk`，`sed`）都和 Linux 中有微妙的不同（ Linux 很大程度上受到了 System V-style Unix 和 GNU 工具影响）。你可以通过标题为 "BSD General Commands Manual" 的 man 页面发现这些不同。在有些情况下 GNU 版本的命令也可能被安装（例如 `gawk` 和 `gsed` 对应 GNU 中的 awk 和 sed ）。如果要写跨平台的 Bash 脚本，避免使用这些命令（例如，考虑 Python 或者 `perl` ）或者经过仔细的测试。
- 用 `sw_vers` 获取 OS X 的版本信息。

