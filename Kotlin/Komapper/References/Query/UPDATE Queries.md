# UPDATE Queries

UPDATE 查询是通过调用 `QueryDsl.update` 和后续函数构造的。

## single

若要更新单个实体，请调用以下 `single` 函数：

```kotlin
val address: Address = ..
val query: Query<Address> = QueryDsl.update(a).single(address)
/*
update ADDRESS set STREET = ?, VERSION = ? + 1 where ADDRESS_ID = ? and VERSION = ?
*/
```

执行上述查询时，返回值是表示更新数据的新实体。

## batch

批量更新多个实体

## include

若要仅包含要在单次或批量运行中更新的特定属性，请提前调用该 `include` 函数：

## exclude

若要排除在单次或批处理运行中更新特定属性，请提前调用该 `exclude` 函数：

## set

要将值设置为特定属性，请将 lambda 表达式传递给 `set` 函数。在 lambda 表达式中，可以使用以下 `eq` 函数将值设置为属性：

```kotlin
val query: Query<Long> = QueryDsl.update(a).set {
  a.street eq "STREET 16"
}.where {
  a.addressId eq 1
}
/*
update ADDRESS as t0_ set STREET = ? where t0_.ADDRESS_ID = ?
*/
```

若要仅在值不为 null 时设置值，请使用以下 `eqIfNotNull` 函数：

执行上述查询时，返回值为更新的行数。

## where

若要更新符合特定条件的行，请调用以下 `where` 函数：

默认情况下，如果缺少 WHERE 子句，则会引发异常。若要有意允许更新所有行，请调用该 `options` 函数并将 `allowMissingWhereClause` 属性设置为 true：

执行上述查询时，返回值为更新的行数。

## returning

下面是在 `single` 函数之后调用函数 `returning` 的示例：

```kotlin
val address: Address = ..
val query: Query<Address?> = QueryDsl.update(a).single(address).returning()
/*
update ADDRESS set STREET = ?, VERSION = ? + 1 where ADDRESS_ID = ? and VERSION = ? returning ADDRESS_ID, STREET, VERSION
*/
```

可以通过在 `returning` 函数中指定属性来限制要检索的列：

```kotlin
val query: Query<Int?> = QueryDsl.update(a).single(address).returning(a.addressId)
/*
update ADDRESS set STREET = ?, VERSION = ? + 1 where ADDRESS_ID = ? and VERSION = ? returning ADDRESS_ID
*/
val query: Query<Pair<Int?, String?>?> = QueryDsl.update(a).single(address).returning(a.addressId, a.street)
/*
update ADDRESS set STREET = ?, VERSION = ? + 1 where ADDRESS_ID = ? and VERSION = ? returning ADDRESS_ID, STREET
*/
val query: Query<Triple<Int?, String?, Int?>?> = QueryDsl.update(a).single(address).returning(a.addressId, a.street, a.version)
/*
update ADDRESS set STREET = ?, VERSION = ? + 1 where ADDRESS_ID = ? and VERSION = ? returning ADDRESS_ID, STREET, VERSION
*/
```

## options

allowMissingWhereClause
是否允许空的 WHERE 子句。缺省值为 `false` 。

escapeSequence escapeSequence（逃逸序列）
为 LIKE 谓词指定的转义序列。默认值是 `null` 指示使用 Dialect 值。

batchSize 批大小

 缺省值为 `null` 。

disableOptimisticLock
是否禁用乐观锁定。缺省值为 `false` 。如果此值为 `true` ，则 WHERE 子句中不包含版本号。

queryTimeoutSeconds
查询超时（以秒为单位）。默认值指示 `null` 应使用驱动程序值。

suppressLogging
是否禁止 SQL 日志输出。缺省值为 `false` 。

suppressOptimisticLockException
如果尝试获取乐观锁失败，是否抑制抛出。 `OptimisticLockException` 缺省值为 `false` 。