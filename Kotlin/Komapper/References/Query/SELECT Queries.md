# SELECT Queries

SELECT 查询是通过调用 `from` 、 `with` 或 `select` on `QueryDsl` 来构造的。

以下查询对应于从 `ADDRESS` 表中检索所有记录的 SQL。

```kotlin
val query: Query<List<Address>> = QueryDsl.from(a)
/*
select t0_.ADDRESS_ID, t0_.STREET, t0_.VERSION from ADDRESS as t0_
*/
```

## from 

要指定 FROM 子句，请调用 `from` 。您应为 指定 `from` 实体元模型。

```kotlin
val query: Query<List<Address>> = QueryDsl.from(a)
/*
select t0_.ADDRESS_ID, t0_.STREET, t0_.VERSION from ADDRESS as t0_
*/
```

使用 `from` ，还可以将子查询与实体元模型一起指定。实体元模型必须与子查询的结果相对应。

```kotlin
val e = Meta.employee
val t = Meta.employeeRank

val subquery = QueryDsl.from(e).select(
    e.employeeId,
    e.employeeName,
    rank().over {
        partitionBy(e.departmentId)
        orderBy(e.salary.desc())
    }
)

val query = QueryDsl.from(t, subquery)
    .where {
        t.rank eq 1
    }
    .orderBy(t.employeeId)
/*
select t0_.employee_id, t0_.employee_name, t0_.rank from (select t1_.employee_id as employee_id, t1_.employee_name as employee_name, rank() over(partition by t1_.department_id order by t1_.salary desc) as rank from employee as t1_) as t0_ where t0_.rank = ? order by t0_.employee_id asc
*/
```

## with

要指定 WITH 子句，请调用 `with` 。该 `with` 函数需要指定实体元模型和子查询。实体元模型必须与子查询的结果相对应。

```kotlin
val e = Meta.employee
val t = Meta.employeeRank

val subquery = QueryDsl.from(e).select(
    e.employeeId,
    e.employeeName,
    rank().over {
        partitionBy(e.departmentId)
        orderBy(e.salary.desc())
    }
)

val query = QueryDsl.with(t, subquery)
        .from(e)
        .innerJoin(t) { e.employeeId eq t.employeeId }
        .where { t.rank eq 1 }
        .orderBy(e.departmentId)
        .select(e.departmentId, e.employeeId, e.employeeName)
/*
with employee_rank (employee_id, employee_name, rank) as (select t0_.employee_id, t0_.employee_name, rank() over(partition by t0_.department_id order by t0_.salary desc) from employee as t0_) select t0_.department_id, t0_.employee_id, t0_.employee_name from employee as t0_ inner join employee_rank as t1_ on (t0_.employee_id = t1_.employee_id) where t1_.rank = ? order by t0_.department_id asc
*/
```

## withRecursive

要指定 WITH RECURSIVE 子句，请调用 `withRecursive` 。该 `withRecursive` 函数需要指定实体元模型和子查询。实体元模型必须与子查询的结果相对应。

```kotlin
val t = Meta.t
val subquery =
    QueryDsl.select(literal(1)).unionAll(
    QueryDsl.from(t).where { t.n less 10 }.select(t.n + 1),
)
val query = QueryDsl.withRecursive(t, subquery).from(t).select(sum(t.n))
/*
with recursive t (n) as ((select 1) union all (select (t0_.n + ?) from t as t0_ where t0_.n < ?)) select sum(t0_.n) from t as t0_
*/
```

## where

若要指定 WHERE 子句，请调用以下 `where` 函数：

```kotlin
val query: Query<List<Address>> = QueryDsl.from(a).where { a.addressId eq 1 }
/*
select t0_.ADDRESS_ID, t0_.STREET, t0_.VERSION from ADDRESS as t0_ where t0_.ADDRESS_ID = ?
*/
```

## innerJoin/leftJoin

**pass**

## forUpdate

若要指定 FOR UPDATE 子句，请调用以下 `forUpdate` 函数：

```kotlin
val query: Query<List<Address>> = QueryDsl.from(a).where { a.addressId eq 1 }.forUpdate()
/*
select t0_.ADDRESS_ID, t0_.STREET, t0_.VERSION from ADDRESS as t0_ where t0_.ADDRESS_ID = ? for update
*/
```

在传递给函数的 `forUpdate` lambda 表达式中，可以通过调用 `nowait` 、 `skipLocked` 和 `wait` 等函数来指定锁定选项。

```kotlin
val query: Query<List<Address>> = QueryDsl.from(a).where { a.addressId eq 1 }.forUpdate { nowait() }
/*
select t0_.address_id, t0_.street, t0_.version from address as t0_ where t0_.address_id = ? for update nowait
*/
val query: Query<List<Address>> = QueryDsl.from(a).where { a.addressId eq 1 }.forUpdate { skipLocked() }
/*
select t0_.address_id, t0_.street, t0_.version from address as t0_ where t0_.address_id = ? for update skip locked
*/
val query: Query<List<Address>> = QueryDsl.from(a).where { a.addressId eq 1 }.forUpdate { wait(1) }
/*
select t0_.address_id, t0_.street, t0_.version from address as t0_ where t0_.address_id = ? for update wait 1
*/
```

## orderBy

若要指定 ORDER BY 子句，请调用以下 `orderBy` 函数：

```kotlin
val query: Query<List<Adress>> = QueryDsl.from(a).orderBy(a.addressId)
/*
select t0_.ADDRESS_ID, t0_.STREET, t0_.VERSION from ADDRESS as t0_ order by t0_.ADDRESS_ID asc
*/
```

默认顺序为升序。若要指定降序，请在将列传递给函数之前对列调用 `desc` `orderBy` 函数。还可以显式调用升 `asc` 序函数。

可以在 `orderBy` 函数中指定多个列。

```kotlin
val query: Query<List<Adress>> = QueryDsl.from(a).orderBy(a.addressId.desc(), a.street.asc())
/*
select t0_.ADDRESS_ID, t0_.STREET, t0_.VERSION from ADDRESS as t0_ order by t0_.ADDRESS_ID desc, t0_.STREET asc
*/
```

要控制 null 值的排序顺序，还可以在列上调用 、 `ascNullsFirst` 、 `ascNullsLast` `descNullsFirst` 和 `descNullsLast` 等函数。

## offset, limit

要从指定位置提取部分行，请调用 `offset` and `limit` 函数

## distinct

**pass**

## select

若要执行投影，请调用该 `select` 函数。

下面是投影单个列的示例：

```kotlin
val query: Query<List<String?>> = QueryDsl.from(a)
    .where {
        a.addressId inList listOf(1, 2)
    }
    .orderBy(a.addressId)
    .select(a.street)
/*
select t0_.STREET from ADDRESS as t0_ where t0_.ADDRESS_ID in (?, ?) order by t0_.ADDRESS_ID asc
*/
```

下面是投影两列的示例：

```kotlin
val query: Query<List<Pair<Int?, String?>>> = QueryDsl.from(a)
    .where {
        a.addressId inList listOf(1, 2)
    }
    .orderBy(a.addressId)
    .select(a.addressId, a.street)
/*
select t0_.ADDRESS_ID, t0_.STREET from ADDRESS as t0_ where t0_.ADDRESS_ID in (?, ?) order by t0_.ADDRESS_ID asc
*/
```

下面是投影三列的示例：

```kotlin
val query: Query<List<Triple<Int?, String?, Int?>>> = QueryDsl.from(a)
    .where {
        a.addressId inList listOf(1, 2)
    }
    .orderBy(a.addressId)
    .select(a.addressId, a.street, a.version)
/*
select t0_.ADDRESS_ID, t0_.STREET, t0_.VERSION from ADDRESS as t0_ where t0_.ADDRESS_ID in (?, ?) order by t0_.ADDRESS_ID asc
*/
```

如果投影的列超过三列，则结果值将包含在 `Record` .您可以使用 `select` 函数中指定的列作为键来检索值 `Record` 。

## selectNotNull

**pass**

## selectAsRecord

如果要在少于四列的投影中以 a `Record` 的形式接收结果，请调用该函数而不是该 `selectAsRecord``select` 函数。

## selectAsEntity

如果要投影结果并将其作为特定实体接收，请调用 `selectAsEntity` 。将实体的元模型指定为第一个参数，将要投影的属性指定为后续参数。属性的顺序和类型必须与实体类的构造函数匹配。

在以下示例中 `EMPLOYEE` ，正在查询表，但结果作为 `Address` 实体接收。

```kotlin
val query: Query<List<Address>> = QueryDsl.from(e)
    .selectAsEntity(a, e.addressId, e.employeeName, e.version)
/*
select t0_.ADDRESS_ID, t0_.EMPLOYEE_NAME, t0_.VERSION from EMPLOYEE as t0_
*/
```

当您用 批 `@KomapperProjection` 注要接收结果的实体类时，可以使用专用的扩展函数更简洁地编写代码，如下所示：

```kotlin
val e = Meta.employee

val query: Query<List<Address>> = QueryDsl.from(e)
    .selectAsAddress(
        version = e.version,
        addressId = e.addressId,
        street = e.employeeName,
    )
```

使用命名参数，可以自由地按任何顺序指定属性。

## having

若要指定 HAVING 子句，请调用以下 `having` 函数：

```kotlin
val query: Query<List<Pair<Int?, Long?>>> = QueryDsl.from(e)
    .having {
        count(e.employeeId) greaterEq 4L
    }
    .orderBy(e.departmentId)
    .select(e.departmentId, count(e.employeeId))
/*
select t0_.DEPARTMENT_ID, count(t0_.EMPLOYEE_ID) from EMPLOYEE as t0_ group by t0_.DEPARTMENT_ID having count(t0_.EMPLOYEE_ID) >= ? order by t0_.DEPARTMENT_ID asc
*/
```

#### Note 注意

如果没有对函数 `groupBy` 的调用，则从传递给 `select` 函数的参数推断并生成 GROUP BY 子句。

## groupBy

若要指定 GROUP BY 子句，请调用该 `groupBy` 函数。

```kotlin
val query: Query<List<Pair<Int?, Long?>>> = QueryDsl.from(e)
    .groupBy(e.departmentId)
    .having {
        count(e.employeeId) greaterEq 4L
    }
    .orderBy(e.departmentId)
    .select(e.departmentId, count(e.employeeId))
/*
select t0_.DEPARTMENT_ID, count(t0_.EMPLOYEE_ID) from EMPLOYEE as t0_ group by t0_.DEPARTMENT_ID having count(t0_.EMPLOYEE_ID) >= ? order by t0_.DEPARTMENT_ID asc
*/
```

## union

**pass**

### first

**pass**

### firstOrNull

**pass**

## single

**pass**

## singleOrNull

**pass**

## collect

要将结果集处理为 `kotlinx.coroutines.flow.Flow` ，请在末尾调用函数 `collect` 

使用该 `collect` 函数，所有行都是在逐个读取时进行处理的，而不是在所有行都读入内存后进行处理。因此，可以提高内存使用率。

## include

https://www.komapper.org/docs/reference/query/querydsl/select/#include

## options

若要自定义查询的行为，请调用该 `options` 函数。该 `options` 函数接受一个 lambda 表达式，其参数表示默认选项。在参数上调用函数 `copy` 以更改其属性。

```kotlin
val query: Query<List<Address>> = QueryDsl.from(a).options {
    it.copy(
      fetchSize = 100,
      queryTimeoutSeconds = 5
    )
}
```

- allowMissingWhereClause

​	是否允许空的 WHERE 子句。缺省值为 `true` 。

* escapeSequence

​	为 LIKE 谓词指定的转义序列。默认值是 `null` 指示使用 Dialect 值。

* fetchSize

​	Default is `null` to indicate that the driver value should be used.

* maxRows

​	Default is `null` to indicate use of the driver’s value.

* queryTimeoutSeconds

​	Query timeout in seconds. Default is `null` to indicate that the driver value should be used.

* suppressLogging

​	Whether to suppress SQL log output. Default is `false`.