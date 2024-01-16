# INSERT Queries

INSERT 查询是通过调用 `QueryDsl.insert` 和后续函数构造的。

## single

若要添加单个实体，请调用以下 `single` 函数：

```kotlin
val address: Address = Address(16, "STREET 16", 0)
val query: Query<Address> = QueryDsl.insert(a).single(address)
/*
insert into ADDRESS (ADDRESS_ID, STREET, VERSION) values (?, ?, ?)
*/
```

执行上述查询时，返回值是表示添加数据的新实体。

## multiple

若要在一个语句中添加多个实体，请调用该 `multiple` 函数：

```kotlin
val query: Query<List<Address>> = QueryDsl.insert(a).multiple(
    Address(16, "STREET 16", 0),
    Address(17, "STREET 17", 0),
    Address(18, "STREET 18", 0)
)
/*
insert into ADDRESS (ADDRESS_ID, STREET, VERSION) values (?, ?, ?), (?, ?, ?), (?, ?, ?)
*/
```

执行上述查询时，返回值是表示添加数据的新实体列表。

## batch

若要在批处理中添加多个实体，请调用该 `batch` 函数。

```kotlin
val query: Query<List<Address>> = QueryDsl.insert(a).batch(
    Address(16, "STREET 16", 0),
    Address(17, "STREET 17", 0),
    Address(18, "STREET 18", 0)
)
/*
insert into ADDRESS (ADDRESS_ID, STREET, VERSION) values (?, ?, ?)
insert into ADDRESS (ADDRESS_ID, STREET, VERSION) values (?, ?, ?)
insert into ADDRESS (ADDRESS_ID, STREET, VERSION) values (?, ?, ?)
*/
```

执行上述查询时，返回值是表示添加数据的新实体列表。

## onDuplicateKeyIgnore

调用该 `onDuplicateKeyIgnore` 函数以在出现重复键时忽略错误。可以在 `onDuplicateKeyIgnore` 函数中指定要检查重复项的键。如果未指定，则使用主键。

### executeAndGet

如果在 `onDuplicateKeyIgnore` 函数之后调用函数 `executeAndGet` ，则返回值是表示添加数据的实体。如果密钥是重复的， `null` 则返回。

### single/multiple/batch

如果在 `onDuplicateKeyIgnore` 函数之后调用函数 `single/multiple/batch` ，则返回值是特定于驱动程序的。

## onDuplicateKeyUpdate

调用该 `onDuplicateKeyUpdate` 函数以在键重复时更新目标行。可以在 `onDuplicateKeyUpdate` 函数中指定要检查重复项的键。如果未指定，则使用主键。

乐观锁定不会应用于要更新的行。

### set

调用函数 `onDuplicateKeyUpdate` 后，可以调用该 `set` 函数为要更新的列设置特定值：

```kotlin
val department: Department = ..
val query = QueryDsl.insert(d).onDuplicateKeyUpdate().set { excluded ->
    d.departmentName eq "PLANNING2"
    d.location eq concat(d.location, concat("_", excluded.location))
}.single(department)
```

该 `set` 函数接受参数为 `excluded` 的 lambda 表达式。表示 `excluded` 要添加的实体的元模型。因此，使用 excluded 允许根据要添加的数据进行更新。

### where

调用函数后，可以调用函数 `onDuplicateKeyUpdate` `where` 设置搜索条件：

## dangerouslyOnDuplicateKeyUpdate/dangerouslyOnDuplicateKey

**pass**

## values

要为每个属性设置一个值并添加一行，请将 lambda 表达式传递给该 `values` 函数。在 lambda 表达式中，可以使用以下 `eq` 函数将值设置为属性：

```kotlin
val query: Query<Pair<Long, Int?>> = QueryDsl.insert(a).values {
  a.addressId eq 19
  a.street eq "STREET 16"
  a.version eq 0
}
/*
insert into ADDRESS (ADDRESS_ID, STREET, VERSION) values (?, ?, ?)
*/
```

若要仅在值不为 null 时设置值，请使用以下 `eqIfNotNull` 函数：

```kotlin
val query: Query<Pair<Long, Int?>> = QueryDsl.insert(a).values {
    a.addressId eq 19
    a.street eqIfNotNull street
    a.version eq 0
}
```

执行上述查询时，返回值为 `Pair` 添加的行数和生成的 ID。仅当`@KomapperAutoIncrement` 或 `@KomapperSequence` 在映射定义中批注时  ，才会返回 ID。

## select 选择

若要添加搜索结果，请调用该 `select` 函数。

```kotlin
val aa = Meta.address.clone(table = "ADDRESS_ARCHIVE")
val query: Query<Long, List<Int>> = QueryDsl.insert(aa).select {
  QueryDsl.from(a).where { a.addressId between 1..5 }
}
/*
insert into ADDRESS_ARCHIVE (ADDRESS_ID, STREET, VERSION) select t1_.ADDRESS_ID, t1_.STREET, t1_.VERSION from ADDRESS as t1_ where t1_.ADDRESS_ID between ? and ?
*/
```

执行上述查询时，返回值为添加的行数和生成的 ID 列表的 Pair。仅当在实体类映射定义中批注时 `@KomapperAutoIncrement` ，才会生成 ID。

## returning

通过在以下函数之后调用该 `returning` 函数，可以检索添加或更新的值：

- single 
- multiple 
- values 

可以通过在 `returning` 函数中指定属性来限制要检索的列：

```kotlin
val query: Query<Int?> = QueryDsl.insert(a).single(address).returning(a.addressId)
/*
insert into ADDRESS (ADDRESS_ID, STREET, VERSION) values (?, ?, ?) returning ADDRESS_ID
*/
val query: Query<Pair<Int?, String?>> = QueryDsl.insert(a).single(address).returning(a.addressId, a.street)
/*
insert into ADDRESS (ADDRESS_ID, STREET, VERSION) values (?, ?, ?) returning ADDRESS_ID, STREET
*/
val query: Query<Triple<Int?, String?, Int?>> = QueryDsl.insert(a).single(address).returning(a.addressId, a.street, a.version)
/*
insert into ADDRESS (ADDRESS_ID, STREET, VERSION) values (?, ?, ?) returning ADDRESS_ID, STREET, VERSION
*/
```

该 `returning` 函数仅在以下方言中受支持：

- H2
- MariaDB MariaDB数据库
- Oracle Database Oracle 数据库
- PostgreSQL PostgreSQL数据库
- SQL Server SQL 服务器

## options

batchSize 

缺省值为 `null` 。

disableSequenceAssignment
是否禁用将序列生成的值分配给 ID。缺省值为 `false` 。

queryTimeoutSeconds
查询超时（以秒为单位）。默认值指示 `null` 应使用驱动程序值。

returnGeneratedKeys 返回GeneratedKeys
是否返回自动递增的 ID 值。缺省值为 `true` 。

suppressLogging
是否禁止 SQL 日志输出。缺省值为 `false` 。