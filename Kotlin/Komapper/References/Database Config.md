# Database Config

可以指定 DatabaseConfig 来自定义 Database 实例的行为。

```kotlin
val connectionFactory: ConnectionFactory = ..
val dialect: R2dbcDialect = ..
val config: R2dbcDatabaseConfig = object: DefaultR2dbcDatabaseConfig(connectionFactory, dialect) {
  // you can override properties here
}
val db = R2dbcDatabase(config)
```

## Properties

### clockProvider

提供 `clockProvider` 用于在实体类属性上设置时间戳的 `Clock` 对象。

## executionOptions

* **batchSize**:使用 INSERT、UPDATE 和 DELETE 进行批量更新的批处理大小。缺省值为 `null` 。如果即使在查询选项中也未指定批大小， `10` 则使用批大小。

`maxRows,fetchSize,queryTimeoutSeconds,suppressLogging`

**More on Komapper/Database Config /executionOptions**

### logger

**pass**

### loggerFacade

**pass**

### statementInspector

**pass**

### templateStatementBuilder

**pass**