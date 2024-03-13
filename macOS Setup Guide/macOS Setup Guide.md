# [macOS Setup Guide](https://sourabhbajaj.com/mac-setup)

# Using Homebrew

要更新Homebrew的公式目录，请运行：

```sh
brew update
```

查看是否需要更新任何公式

```sh
brew outdated
```

Homebrew在您的系统上保留了旧版本的公式，以防您想要回滚到旧版本。这很少是必要的，所以您可以进行一些清理来摆脱这些旧版本。

```sh
brew cleanup
```

如果你想查看Homebrew会删除哪些公式但又不实际删除它们，你可以运行：

```sh
brew cleanup --dry-run
```

查看已安装的内容（及其版本号）：

```sh
brew list --versions
```

要获取有关公式的更多信息，请运行：

```sh
brew info <formula>
```

# Homebrew-Cask

# FZF

将这些函数中的任何一个添加到您的shell配置文件中，并应用更改以尝试它们。或者，如果您只想尝试而不保存它，请将函数粘贴到您的终端中。

```sh
# fd - cd to selected directory
fd() {
  local dir
  dir=$(find ${1:-.} -path '*/\.*' -prune \
                  -o -type d -print 2> /dev/null | fzf +m) &&
  cd "$dir"
}
# fh - search in your command history and execute selected command
fh() {
  eval $( ([ -n "$ZSH_NAME" ] && fc -l 1 || history) | fzf +s --tac | sed 's/ *[0-9]* *//')
}
```

### Pyenv method Pyenv方法

您现在可以开始使用 `pyenv` 。要列出所有可用的Python版本，包括Anaconda、Jython、PyPy和Stackless，请使用：

```sh
pyenv install --list
```

使用 `global` 命令在所有shell中设置全局版本的Python。例如，如果你更喜欢2.7.12而不是3.5.2：

```sh
pyenv global 2.7.12 3.5.2
pyenv rehash
```

首选版本优先。所有已安装的Python版本可以在 `~/.pyenv/versions` 中找到。或者，您可以运行：

```console
$ pyenv versions
  system (set by /Users/your_account/.pyenv/version)
* 2.7.12
* 3.5.2
这显示了当前活动版本旁边的一个星号 `*` 。
```

# Virtualenv 虚拟环境

如果您在名为 `my-project` 的目录中有一个项目，可以通过运行以下命令来为该项目设置 `virtualenv` :

```sh
cd my-project/
virtualenv venv
```

如果您在名为 `my-project` 的目录中有一个项目，可以通过运行以下命令来为该项目设置 `virtualenv` :

```sh
cd my-project/
virtualenv venv
```

这些命令在您的项目中创建一个 `venv/` 目录，其中安装了所有的依赖项。但是您需要先激活它（在您正在处理项目的每个终端实例中）。

```sh
source venv/bin/activate
```

您应该在终端提示符的开头看到一个 `(venv)` ，表示您正在 `virtualenv` 中工作。现在，当您安装类似这样的东西时：

```sh
pip install <package>
```

它将安装在 `venv/` 文件夹中，不会与其他项目冲突。
要离开虚拟环境，请运行：

```sh
deactivate
```

# SDKMAN

# Useful Docker Commands 有用的Docker命令

从Dockerfile构建镜像。

```sh
docker build [DOCKERFILE PATH]
```

### Useful flags 有用的旗帜

- `--file -f` Path where to find the Dockerfile
  Dockerfile 的路径
- `--force-rm` Always remove intermediate containers
  始终删除中间容器
- `--no-cache` Do not use cache when building the image
  构建图像时不要使用缓存
- `--rm` Remove intermediate containers after a successful build (this is `true`) by default
  默认情况下，在成功构建后删除中间容器
- `--tag -t` Name and optionally a tag in the ‘name:tag’ format
  名称和可选的标签，格式为“名称:标签”

## [`docker exec`](https://docs.docker.com/engine/reference/commandline/exec/)

Execute a command inside a **running** container.
在运行中的容器内执行一个命令。

```sh
docker exec [CONTAINER ID]
```

### Example 例子

```sh
docker exec [CONTAINER ID] touch /tmp/exec_works
```

### Useful flags 有用的旗帜

- `--detach -d` Detached mode: run command in the background
  后台模式：在后台运行命令
- `-it` This will not make the container you started shut down immediately, as it will create a pseudo-TTY session (`-t`) and keep STDIN open (`-i`)
  这不会立即关闭您启动的容器，因为它会创建一个伪TTY会话（ `-t` ）并保持STDIN打开（ `-i` ）

## [`docker images`](https://docs.docker.com/engine/reference/commandline/images/)

List all downloaded/created images.
列出所有已下载/创建的图像。

```sh
docker images
```

### Useful flags 有用的旗帜

- `-q` Only show numeric IDs
  仅显示数字ID

## [`docker logs`](https://docs.docker.com/engine/reference/commandline/logs/)

Gets logs from container.
从容器获取日志。

```sh
docker logs [CONTAINER ID]
```

### Useful flags 有用的旗帜

- `--details` Log extra details
  记录额外细节
- `--follow -f` Follow log output. Do not stop when end of file is reached, but rather wait for additional data to be appended to the input.
  跟随日志输出。当到达文件末尾时不停止，而是等待输入中追加的额外数据。
- `--timestamps -t` Show timestamps
  显示时间戳

## [`docker ps`](https://docs.docker.com/engine/reference/commandline/ps/)

Shows information about all running containers.
显示有关所有正在运行的容器的信息。

```sh
docker ps
```

### Useful flags 有用的旗帜

- `--all -a` Show all containers (default shows just running)
  显示所有容器（默认只显示正在运行的）

- `--filter -f` Filter output based on conditions provided, `docker ps -f="name="example"`
  根据提供的条件筛选输出

- `--quiet -q` Only display numeric IDs
  仅显示数字ID

  ## [`docker run`](https://docs.docker.com/engine/reference/commandline/run/)

创建并启动一个容器的操作。可以用于执行单个命令，也可以启动一个长时间运行的容器。

Example: 例子：

```sh
docker run -it ubuntu:latest /bin/bash
```

This will start a ubuntu container with the entrypoint `/bin/bash`. Note that if you do not have the `ubuntu` image downloaded it will download it before running it.
这将启动一个带有入口点 `/bin/bash` 的Ubuntu容器。请注意，如果您没有下载 `ubuntu` 镜像，它将在运行之前下载。

### Useful flags 有用的旗帜

- `-it` This will not make the container you started shut down immediately, as it will create a pseudo-TTY session (`-t`) and keep STDIN open (`-i`)
  这不会立即关闭您启动的容器，因为它会创建一个伪TTY会话（ `-t` ）并保持STDIN打开（ `-i` ）
- `--rm` Automatically remove the container when it exit. Otherwise it will be stored and visible running `docker ps -a`.
  自动在容器退出时移除它。否则它将被存储并显示为运行中。
- `--detach -d` Run container in background and print container ID
  在后台运行容器并打印容器ID
- `--volume -v` Bind mount a volume. Useful for accessing folders on your local disk inside your docker container, like configuration files or storage that should be persisted (database, logs etc.).
  绑定挂载卷。用于在Docker容器内访问本地磁盘上的文件夹，例如配置文件或应该持久化的存储（数据库、日志等）。

# LaTeX
