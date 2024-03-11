# Terminal Colors 终端颜色

**[colors](https://github.com/termstandard/colors)**

关于终端颜色存在普遍的混淆。这是我们目前拥有的：

- Plain ASCII 普通ASCII
- ANSI escape codes: 16 color codes with bold/italic and background
  ANSI转义码：16种颜色代码，包括粗体/斜体和背景
- 256 color palette: 216 colors + 16 ANSI + 24 gray (colors are 24-bit)
  256色调色板：216种颜色+16种ANSI颜色+24种灰色（颜色为24位）
- 24-bit truecolor: "888" colors (aka 16 million)
  24位真彩色： "888"种颜色（也称为1600万）

256色调色板在启动时配置，是一个由颜色组成的666立方体，每个颜色都定义为24位（888 RGB）颜色。

这意味着当前的支持只能在终端中显示256种不同的颜色，而"真彩色"意味着您可以同时显示1600万种不同的颜色。

真彩色转义代码不使用调色板，它们直接指定颜色。

