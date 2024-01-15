# Komapper

*WARNING: 该页面与 Komapper 摘抄，部分翻译使用微软翻译*

[Komapper Website](https://www.komapper.org)

**an ORM library for server-side Kotlin**

## Features

* ### Code generation at compile-time

Komapper 使用 Kotlin 符号处理 API 在编译时将元模型（表和列信息）生成为 Kotlin 源代码。

* ### Immutable and composable queries

Komapper 的查询几乎是不可变的。因此，它们可以安全地组合，而无需担心与状态共享相关的问题。

* ### Support for Kotlin value classes