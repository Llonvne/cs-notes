# Databases

要使用 Komapper 访问数据库，需要 `JdbcDatabase` or `R2dbcDatabase` 的实例。在这里，这些实例统称为数据库实例。

## Instantiation

* ### 使用 R2DBC 时

  * URL

  ```kotlin
  val db: R2dbcDatabase = R2dbcDatabase("r2dbc:h2:mem:///example;DB_CLOSE_DELAY=-1")
  ```

## Usage

### Transaction Control

事务由 `withTransaction` Database 实例的功能控制。事务逻辑作为 lambda 表达式传递给 `withTransaction` 函数。

```kotlin
db.withTransaction {
    ...
}
```

### Query Execution

通过调用 Database 实例的 `runQuery` 函数来执行查询。

```kotlin
val a = Meta.address
val query: Query<List<Address>> = QueryDsl.from(a)
val result: List<Address> = db.runQuery(query)
```

当 Database 实例为`R2dbcDatabase`且查询类型为  `org.komapper.core.dsl.query.FlowQuery` 时，可以执行该 `flowQuery` 函数。

```kotlin
val a = Meta.address
val query: FlowQuery<Address> = QueryDsl.from(a)
val flow: Flow<Address> = db.flowQuery(query)
```

仅当收集 `flow` 实例时，才会进行数据库访问。

### Low-level API execution

要直接使用 R2DBC API，请调用 `db.config.session.useConnection()` get `io.r2dbc.spi.Connection` .
