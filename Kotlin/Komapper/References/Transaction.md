# Transaction

Komapper 为事务管理提供了高级 API。

>当 Komapper 与 Spring Framework 或 Quarkus 结合使用时，此 API 可与 Spring Framework 和 Quarkus 事务管理器配合使用。

### Beginning and ending transactions

```kotlin
db.withTransaction {
    ..
}
```

该 `withTransaction` 函数接受事务属性和事务属性'：

```kotlin
db.withTransaction(
  transactionAttribute = TransactionAttribute.REQUIRES_NEW, 
  transactionProperty = TransactionProperty.IsolationLevel.SERIALIZABLE) {
    ..
}
```

## Transactional flows 事务流

仅 `R2dbcDatabase` 提供构造事务流的 `flowTransaction` 函数：

```kotlin
val db = R2dbcDatabase("r2dbc:h2:mem:///example;DB_CLOSE_DELAY=-1")

val transactionalFlow: Flow<Address> = db.flowTransaction {
    val a = Meta.address
    val address = db.runQuery {
        QueryDsl.from(a).where { a.addressId eq 15 }.first()
    }
    db.runQuery { 
        QueryDsl.update(a).single(address.copy(street = "TOKYO")) 
    }
    val addressFlow = db.flowQuery { 
        QueryDsl.from(a).orderBy(a.addressId)
    }
    emitAll(addressFlow)
}

// Transaction is executed
val list = transactionalFlow.toList()
```

在上面的示例中，对 `flowTransaction` 函数的调用仅构造一个流。当收集 时 `transactionalFlow` ，事务将首次执行。