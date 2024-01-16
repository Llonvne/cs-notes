# Query Introduction

查询构造和执行是分开的。QueryDsl 负责构造查询，Database 负责执行查询。

```kotlin
// construct a query
val query: Query<List<Address>> = QueryDsl.from(a)
// execute the query
val result: List<Address> = db.runQuery { query }
```