# Query Composition

查询支持组合。

## Composition functions

在 Komapper 中，查询由以下一个或两个类表示。

```
org.komapper.core.dsl.query.Query<T>
```

A query that returns the value of type `T`
返回 type `T` 值的查询

```
org.komapper.core.dsl.query.FlowQuery<T>
```

返回 type `kotlinx.coroutines.flow.Flow<T>` 值的查询

其中，仅 `Query<T>` 支持合成。以下各节介绍可在 上 `Query<T>` 执行的复合功能。

### andThen

这些 `andThen` 函数构造一个一起运行并返回最后一个结果的查询：

```kotlin
val q1: Query<Address> = QueryDsl.insert(a).single(Address(16, "STREET 16", 0))
val q2: Query<Address> = QueryDsl.insert(a).single(Address(17, "STREET 17", 0))
val q3: Query<List<Address>> = QueryDsl.from(a).where { a.addressId inList listOf(16, 17) }
val query: Query<List<Address>> = q1.andThen(q2).andThen(q3)
val list: List<Address> = db.runQuery { query }
/*
insert into ADDRESS (ADDRESS_ID, STREET, VERSION) values (?, ?, ?)
insert into ADDRESS (ADDRESS_ID, STREET, VERSION) values (?, ?, ?)
select t0_.ADDRESS_ID, t0_.STREET, t0_.VERSION from ADDRESS as t0_ where t0_.ADDRESS_ID in (?, ?)
*/
```

### map

该 `map` 函数构造一个查询，用于对查询结果进行更改

*该更改并不会同步到数据库*

### zip

该函数构造一个查询，该 `zip` 查询以 `Pair` .

```kotlin
val q1 = QueryDsl.insert(a).single(Address(16, "STREET 16", 0))
val q2 = QueryDsl.from(a)
val query: Query<Pair<Address, List<Address>>> = q1.zip(q2)
/*
insert into ADDRESS (ADDRESS_ID, STREET, VERSION) values (?, ?, ?)
select t0_.ADDRESS_ID, t0_.STREET, t0_.VERSION from ADDRESS as t0_
*/
```

### flatMap

该函数构造一个查询，该 `flatMap` 查询使用第一个查询的结果执行第二个查询，并返回第二个查询的结果。

```kotlin
val q1: Query<Address> = QueryDsl.insert(a).single(Address(16, "STREET 16", 0)) // 1st query
val query: Query<List<Employee>> = q1.flatMap { newAddress ->
    QueryDsl.from(e).where { e.addressId less newAddress.addressId } // 2nd query
}
val list: List<Employee> = db.runQuery { query }
/*
insert into ADDRESS (ADDRESS_ID, STREET, VERSION) values (?, ?, ?)
select t0_.EMPLOYEE_ID, t0_.EMPLOYEE_NO, t0_.EMPLOYEE_NAME, t0_.MANAGER_ID, t0_.HIREDATE, t0_.SALARY, t0_.DEPARTMENT_ID, t0_.ADDRESS_ID, t0_.VERSION from EMPLOYEE as t0_ where t0_.ADDRESS_ID < ?
*/
```

### flatZip

该函数构造一个查询，该 `flatZip` 查询使用第一个查询的结果执行第二个查询，并将两个查询结果返回为 `Pair` 。

```kotlin
val q1: Query<Address> = QueryDsl.insert(a).single(Address(16, "STREET 16", 0)) // 1st query
val query: Query<Pair<Address, List<Employee>>> = q1.flatZip { newAddress ->
    QueryDsl.from(e).where { e.addressId less newAddress.addressId } // 2nd query
}
val pair: Pair<Address, List<Employee>> = db.runQuery { query }
/*
insert into ADDRESS (ADDRESS_ID, STREET, VERSION) values (?, ?, ?)
select t0_.EMPLOYEE_ID, t0_.EMPLOYEE_NO, t0_.EMPLOYEE_NAME, t0_.MANAGER_ID, t0_.HIREDATE, t0_.SALARY, t0_.DEPARTMENT_ID, t0_.ADDRESS_ID, t0_.VERSION from EMPLOYEE as t0_ where t0_.ADDRESS_ID < ?
*/
```