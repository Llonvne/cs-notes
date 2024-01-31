# Oh Shit, Git!?!

[origin](Oh Shit, Git!?!)

## [Oh shit, I did something terribly wrong, please tell me git has a magic time machine!?! 哦，该死，我做了一件非常错误的事情，请告诉我git有一个神奇的时光机吗？！？](https://ohshitgit.com/#magic-time-machine)

```git
git reflog
# you will see a list of every thing you've
# done in git, across all branches!
# each one has an index HEAD@{index}
# find the one before you broke everything
git reset HEAD@{index}
# magic time machine
```

您可以使用此功能来恢复意外删除的内容，或者仅仅是删除一些破坏了存储库的内容，或者在糟糕的合并后恢复，或者仅仅是回到事情实际上正常工作的时候。我经常使用它。非常感谢建议添加此功能的众多人士！

## [Oh shit, I committed and immediately realized I need to make one small change! 哦，该死，我提交了，立刻意识到我需要做一个小改变！](https://ohshitgit.com/#change-last-commit)

```git
# make your change
git add . # or add individual files
git commit --amend --no-edit
# now your last commit contains that change!
# WARNING: never amend public commits
```

如果我提交后运行测试/检查工具，通常会发生这种情况...我在等号后面没有加空格。你也可以将更改作为新的提交，然后使用 `rebase -i` 来将它们合并在一起，但这样要快上百万倍。

*警告：您绝不能修改已推送到公共/共享分支的提交！只能修改仅存在于您本地副本中的提交，否则您将会遇到麻烦。*

## [Oh shit, I need to change the message on my last commit! 哦，该死，我需要修改我上次提交的消息！](https://ohshitgit.com/#change-last-commit-message)

```git
git commit --amend
# follow prompts to change the commit message
```

Stupid commit message formatting requirements.
愚蠢的提交信息格式要求。

## [Oh shit, I accidentally committed something to master that should have been on a brand new branch! 哦，该死，我不小心把一些东西提交到了主分支，本应该放在一个全新的分支上！](https://ohshitgit.com/#accidental-commit-master)

```git
# create a new branch from the current state of master
git branch some-new-branch-name
# remove the last commit from the master branch
git reset HEAD~ --hard
git checkout some-new-branch-name
# your commit lives in this branch now :)
```

注意：如果您已经将提交推送到公共/共享分支，则此方法不起作用，如果您之前尝试了其他方法，您可能需要 `git reset HEAD@{number-of-commits-back}` 而不是 `HEAD~` 。无限的悲伤。此外，很多很多人提出了一个我自己不知道的很棒的方法来缩短这个过程。谢谢大家！

## [Oh shit, I accidentally committed to the wrong branch! 哦，该死，我不小心提交到了错误的分支！](https://ohshitgit.com/#accidental-commit-wrong-branch)

```git
# undo the last commit, but leave the changes available
git reset HEAD~ --soft
git stash
# move to the correct branch
git checkout name-of-the-correct-branch
git stash pop
git add . # or add individual files
git commit -m "your message here";
# now your changes are on the correct branch
```

很多人也建议在这种情况下使用 `cherry-pick` ，所以你可以选择对你来说最有意义的那个！

```git
git checkout name-of-the-correct-branch
# grab the last commit to master
git cherry-pick master
# delete it from master
git checkout master
git reset HEAD~ --hard
```

## [Oh shit, I tried to run a diff but nothing happened?! 哦，该死，我尝试运行一个差异但什么都没发生？！](https://ohshitgit.com/#dude-wheres-my-diff)

如果你知道你对文件进行了更改，但 `diff` 为空，那么你可能将文件 `add` 到了暂存区，你需要使用一个特殊的标志。

```git
git diff --staged
```

文件归类为¯\_(ツ)_/¯（是的，我知道这是一个特性，而不是一个错误，但第一次遇到时真是令人困惑和不明显！）

## [Oh shit, I need to undo a commit from like 5 commits ago! 哦，该死，我需要撤销一个像是5个提交之前的提交！](https://ohshitgit.com/#undo-a-commit)

```git
# find the commit you need to undo
git log
# use the arrow keys to scroll up and down in history
# once you've found your commit, save the hash
git revert [saved hash]
# git will create a new commit that undoes that commit
# follow prompts to edit the commit message
# or just save and commit
```

原来你不需要追踪并复制粘贴旧文件内容到现有文件中以撤销更改！如果你提交了一个错误，你可以一次性用 `revert` 撤销提交。

你也可以还原单个文件而不是整个提交！但当然，按照真正的git风格，这是一组完全不同的该死的命令...

## [Oh shit, I need to undo my changes to a file! 哦，该死，我需要撤销对文件的更改！](https://ohshitgit.com/#undo-a-file)

```git
# find a hash for a commit before the file was changed
git log
# use the arrow keys to scroll up and down in history
# once you've found your commit, save the hash
git checkout [saved hash] -- path/to/file
# the old version of the file will be in your index
git commit -m "Wow, you don't have to copy-paste to undo"
```

当我终于弄明白这个问题时，它是巨大的。巨大。巨大。但说真的，在哪个该死的星球上， `checkout --` 怎么可能是撤销文件的最佳方式呢？:对着林纳斯·托瓦兹摇拳头:

## [Fuck this noise, I give up. 操这个噪音，我放弃了。](https://ohshitgit.com/#fuck-this-noise)

```git
cd ..
sudo rm -r fucking-git-repo-dir
git clone https://some.github.url/fucking-git-repo-dir.git
cd fucking-git-repo-dir
```

真的，如果你的分支非常糟糕，以至于你需要以一种“git认可”的方式重置你的仓库状态与远程仓库相同，请尝试以下操作，但请注意这些是破坏性和不可恢复的操作！

```git
# get the lastest state of origin
git fetch origin
git checkout master
git reset --hard origin/master
# delete untracked files and directories
git clean -d --force
# repeat checkout/reset/clean for each borked branch
```