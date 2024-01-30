# Your Commits “Atomic”

当初开始使用源代码控制（无论是Git、SVN、TFS还是其他）时，经常会出现一个问题：“我应该提交什么，以及提交的频率是多少？”我的回答是尽可能将更改保持小而“原子化”。我将在下面进行更详细的解释。

## Atomic Commits 原子提交

An “atomic” change revolves around one task or one fix.
一个“原子”变化围绕着一个任务或一个修复。

最近我收到了一封电子邮件，里面列出了一份我正在开发的网页应用程序**需要进行的布局变更和错误修复**。所有这些变更都非常简单。对此的**一种方法是直接进行所有的变更/修复**，提交到代码库，然后就完成了。然而，如果**这个错误修复引入了另一个错误**，或者实际上并没有解决问题，那该怎么办呢？

一般最佳做法是撤销您最近的提交，进行适当的修复，然后重新提交。然而，如果您这样做，您将丢失所有的布局更改（这些更改正常工作），并且您将需要额外的工作来重新应用布局更改。此外，创建另一个提交来“修复错误修复”也不是一个好的方法。

相反，将错误修复作为一个更改提交，将布局更改作为另一个更改提交。这样，您可以轻松地撤销错误修复而不影响布局更改。我甚至会建议将每个布局更改也分别提交，因为这样可以更容易地在运行时更改布局，或者撤销一个简单的颜色更改而不影响其他相关更新。

### Atomic Approach 原子方法

- Commit each fix or task as a separate change
  将每个修复或任务作为单独的更改提交

- Only commit when a block of work is complete
  只有在完成一块工作时才提交
- Commit each layout change separately
  逐个提交每个布局更改

- Joint commit for layout file, code behind file, and additional resources
  布局文件、代码后台文件和额外资源的联合提交

### Benefits 好处

- Easy to roll back without affecting other changes
  易于回滚，不影响其他更改
- Easy to make other changes on the fly
  随时进行其他更改很容易
- Easy to merge features to other branches