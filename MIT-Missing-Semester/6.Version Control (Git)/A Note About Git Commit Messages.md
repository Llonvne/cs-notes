# A Note About Git Commit Messages

[origin](https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)

我想花点时间详细说明如何构成格式良好的提交消息。我认为提交消息格式化的最佳实践是让 Git 变得伟大的小细节之一。

```
Capitalized, short (50 chars or less) summary

More detailed explanatory text, if necessary.  Wrap it to about 72
characters or so.  In some contexts, the first line is treated as the
subject of an email and the rest of the text as the body.  The blank
line separating the summary from the body is critical (unless you omit
the body entirely); tools like rebase can get confused if you run the
two together.

Write your commit message in the imperative: "Fix bug" and not "Fixed bug"
or "Fixes bug."  This convention matches up with commit messages generated
by commands like git merge and git revert.

Further paragraphs come after blank lines.

- Bullet points are okay, too

- Typically a hyphen or asterisk is used for the bullet, followed by a
  single space, with blank lines in between, but conventions vary here

- Use a hanging indent
```

让我们从一些为什么将提交消息包装到 72 列是一件好事开始.

`git log` 不会对提交消息进行任何特殊的包装。使用默认分页器 `less -S` ，这意味着您的段落远离屏幕边缘，导致难以阅读。在 80 列的终端上，如果我们减去左侧缩进的 4 列和右侧对称的 4 列，则剩下 72 列。

`git format-patch --stdout` 使用消息作为消息正文，将一系列提交转换为一系列电子邮件。良好的电子邮件网络礼仪要求我们对纯文本电子邮件进行包装，以便在 80 列终端中为几层嵌套回复指示器留出空间，而不会溢出。 （当前的rails.git工作流程不包括电子邮件，但谁知道未来会带来什么。）