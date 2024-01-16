# Query Builders

生成查询部分的函数称为生成器。

## where

该 `where` 函数生成 Where 声明。

```kotlin
val salaryWhere = where {
  e.salary greater BigDecimal(1_000)
}
val query: Query<List<Employee>> = QueryDsl.from(e).where(salaryWhere)
```

## on

该 `on` 函数生成一个 On 声明。

```kotlin
val departmentIdOn = on {
    e.departmentId eq d.departmentId
}
val query: Query<List<Employee>> = QueryDsl.from(e).innerJoin(d, departmentIdOn)
```

## having

该 `having` 函数生成一个 Have 声明。

```kotlin
val countHaving = having {
    count() greater 3
}
val query: Query<List<Int?>> = QueryDsl.from(e)
    .groupBy(e.departmentId)
    .having(countHaving)
    .select(e.departmentId)
```

## set

该 `set` 函数生成 Assignment 声明。

```kotlin
val addressAssignment = set(a) {
    a.street eq "STREET 16"
}
val query: Query<Int> = QueryDsl.update(a).set(addressAssignment).where {
    a.addressId eq 1
}
```

## values

该 `values` 函数生成 Assignment 声明。

```kotlin
val addressAssignment = values(a) {
    a.street eq "STREET 16"
}
val query: Query<Pair<Int, Int?>> = QueryDsl.insert(a).values(addressAssignment)
```

## join

## groupBy

## orderBy