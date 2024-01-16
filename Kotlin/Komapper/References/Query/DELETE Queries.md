# DELETE Queries

DELETE 查询是通过调用 `QueryDsl.delete` 和后续函数构造的。

## single

若要删除单个实体，请调用以下 `single` 函数：

```kotlin
val address: Address = ..
val query: Query<Unit> = QueryDsl.delete(a).single(address)
/*
delete from ADDRESS as t0_ where t0_.ADDRESS_ID = ? and t0_.VERSION = ?
*/
```

## batch

**pass**

## all

**pass**

## where

若要删除与特定条件匹配的行，请调用以下 `where` 函数：

```kotlin
val query: Query<Long> = QueryDsl.delete(a).where { a.addressId eq 15 }
/*
delete from ADDRESS as t0_ where t0_.ADDRESS_ID = ?
*/
```

默认情况下，如果缺少 WHERE 子句，则会引发异常。若要有意允许删除所有行，请调用该 `options` 函数并将 `allowMissingWhereClause` 属性设置为 true：

## returning

**pass**

## options

**pass**