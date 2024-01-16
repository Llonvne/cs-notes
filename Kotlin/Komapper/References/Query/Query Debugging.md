# Query Debugging

您可以查看从 生成的 `Query` SQL，而无需连接到数据库。

## dryRun

在 上 `Query` 调用函数 `dryRun` 可以查看 SQL 和绑定到查询的参数：

```kotlin
val query: Query<List<Address>> = QueryDsl.from(a).where { a.addressId eq 1 }
val result: DryRunResult = query.dryRun()
println(result)
```

上述代码的输出结果如下（为了可读性，插入了换行符）：

```sh
DryRunResult(
  sql=select t0_.ADDRESS_ID, t0_.STREET, t0_.VERSION from ADDRESS as t0_ where t0_.ADDRESS_ID = ?, 
  sqlWithArgs=select t0_.ADDRESS_ID, t0_.STREET, t0_.VERSION from ADDRESS as t0_ where t0_.ADDRESS_ID = 1, 
  args=[Value(any=1, klass=class kotlin.Int)], 
  throwable=null, 
  description=This data was generated using DryRunDatabaseConfig. To get more correct information, specify the actual DatabaseConfig instance.
)
```

sql
从查询生成的 SQL。绑定变量用 `?` 表示。如果发生异常，则表示异常消息而不是 SQL。

sqlWithArgs
具有从查询生成的参数的 SQL。绑定变量将替换为参数的字符串表示形式。如果发生异常，则表示异常消息而不是 SQL。

args 参数
参数值/类型对。

throwable 
在 SQL 生成期间引发异常。如果未引发异常，则 `null` .

description 描述
实例 `DryRunResult` 的说明。

### Using Dialect

如果要考虑方言获得结果，请传递一个 `DatabaseConfig` 实例。

```kotlin
val database: JdbcDatabase = ...
val query: Query<List<Address>> = QueryDsl.from(a).where { a.addressId eq 1 }
val result: DryRunResult = query.dryRun(database.config)
println(result)
```

或者调用 `dryRun` `Database` 实例的函数。

```kotlin
val database: JdbcDatabase = ...
val query: Query<List<Address>> = QueryDsl.from(a).where { a.addressId eq 1 }
val result: DryRunResult = database.dryRun(query)
println(result)
```