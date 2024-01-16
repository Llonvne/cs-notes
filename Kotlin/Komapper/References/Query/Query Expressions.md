# Query Expressions

本页介绍表达式的组件，包括声明、运算符和函数。

## Declarations

例如，在查询 DSL 中，可以将表示搜索条件的 lambda 表达式传递给 `where` 函数。

```kotlin
QueryDsl.from(a).where { a.addressId eq 1 }
```

我们将此类 lambda 表达式称为声明。所有声明在 `org.komapper.core.dsl.expression` 包中都定义为 typealias。

- AssignmentDeclaration 

  与 `values` 和 `set` 函数一起使用。

- HavingDeclaration 

  与 `having` 函数一起使用。

- OnDeclaration 

  与 `on` 函数一起使用。

- WhenDeclaration 

  与 `When` 函数一起使用。

- WhereDeclaration 

  与 `where` 函数一起使用。
  这些声明是可组合的。

### plus

`+`运算符构造一个新声明，该声明按顺序执行其操作数：

```kotlin
val w1: WhereDeclaration = {
    a.addressId eq 1
}
val w2: WhereDeclaration = {
    a.version eq 1
}
val w3: WhereDeclaration = w1 + w2 // Use of the `+` operator
val query: Query<List<Address>> = QueryDsl.from(a).where(w3)
val list: List<Address> = db.runQuery { query }
/*
select t0_.ADDRESS_ID, t0_.STREET, t0_.VERSION from ADDRESS as t0_ where t0_.ADDRESS_ID = ? and t0_.VERSION = ?
*/
`+` 运算符在所有声明中都可用。
```

### and
该函数构造一个新声明，该 `and` 声明将其接收器和参数与 AND 谓词连接起来：

```kotlin
val w1: WhereDeclaration = {
    a.addressId eq 1
}
val w2: WhereDeclaration = {
    a.version eq 1
    or { a.version eq 2 }
}
val w3: WhereDeclaration = w1.and(w2) // Use of the `and` function
val query: Query<List<Address>> = QueryDsl.from(a).where(w3)
val list: List<Address> = db.runQuery { query }
/*
select t0_.ADDRESS_ID, t0_.STREET, t0_.VERSION from ADDRESS as t0_ where t0_.ADDRESS_ID = ? and (t0_.VERSION = ? or (t0_.VERSION = ?))
*/
```

该 `and` 函数可应用于 Having、When 和 Where 声明。

### or
该函数构造一个新声明，该 `or` 声明将其接收器和参数与 OR 谓词连接起来：

```kotlin
val w1: WhereDeclaration = {
    a.addressId eq 1
}
val w2: WhereDeclaration = {
    a.version eq 1
    a.street eq "STREET 1"
}
val w3: WhereDeclaration = w1.or(w2) // Use of the `or` function
val query: Query<List<Address>> = QueryDsl.from(a).where(w3)
val list: List<Address> = db.runQuery { query }
/*
select t0_.ADDRESS_ID, t0_.STREET, t0_.VERSION from ADDRESS as t0_ where t0_.ADDRESS_ID = ? or (t0_.VERSION = ? and t0_.STREET = ?)
*/
```

该 `or` 函数可应用于 Having、When 和 Where 声明。

## Comparison operators

比较运算符在 Having、On、When 和 Where 声明中可用。

如果 `null` 作为参数传递给比较运算符，则不计算运算符。也就是说，不会生成相应的 SQL：

```kotlin
val nullable: Int? = null
val query = QueryDsl.from(a).where { a.addressId eq nullable }
```

因此，当执行上述 `query` 操作时，将发出以下 SQL：

```sql
select t0_.ADDRESS_ID, t0_.STREET, t0_.VERSION from ADDRESS as t0_
```

### eq ==

### notEq !=

### less <

### lessEq <=

### greater >

### greaterEq >=

### isNull

### isNotNull

### like

### notLike

### startsWith

### notStartsWith

### contains

### notContains

### endsWith

### notEndsWith

### between

### notBetween

### inList

The `inList` operator also accepts a subquery.

```kotlin
QueryDsl.from(e).where {
    e.addressId inList {
        QueryDsl.from(a)
            .where {
                e.addressId eq a.addressId
                e.employeeName like "%S%"
            }.select(a.addressId)
    }
}
/*
select t0_.EMPLOYEE_ID, t0_.EMPLOYEE_NO, t0_.EMPLOYEE_NAME, t0_.MANAGER_ID, t0_.HIREDATE, t0_.SALARY, t0_.DEPARTMENT_ID, t0_.ADDRESS_ID, t0_.VERSION from EMPLOYEE as t0_ where t0_.ADDRESS_ID in (select t1_.ADDRESS_ID from ADDRESS as t1_ where t0_.ADDRESS_ID = t1_.ADDRESS_ID and t0_.EMPLOYEE_NAME like ? escape ?)
*/
```

### notInList

### inList2

### notInList2

### exists

### notExists

## Logical operators

### and

声明中的表达式使用 AND 运算符隐式连接。

### or

要使用 OR 运算符连接表达式，请将 lambda 表达式传递给函数 `or` 。

### not

## Arithmetic operators

以下运算符可用作算术运算符：

- `+`
- `-`
- `*`
- `/`
- `%`

```kotlin
QueryDsl.update(a).set {
    a.version eq (a.version + 10)
}.where {
    a.addressId eq 1
}
/*
update ADDRESS as t0_ set VERSION = (t0_.VERSION + ?) where t0_.ADDRESS_ID = ?
*/
```

## Mathematical functions

### random

```kotlin
QueryDsl.from(a).orderBy(random())
/*
select t0_.ADDRESS_ID, t0_.STREET, t0_.VERSION from ADDRESS as t0_ order by random() asc
*/
```

## String functions 

以下函数可用作字符串函数：

- concat
- substring
- locate
- lower
- upper
- trim
- ltrim
- rtrim

## Aggregate functions

以下函数可用作聚合函数：

- avg
- count 
- sum
- max
- min

聚合函数调用获取的表达式旨在与 `having` or `select` 函数一起使用：

```kotlin
QueryDsl.from(e)
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

### avg

```kotlin
QueryDsl.from(a).select(avg(a.addressId))
/*
select avg(t0_.ADDRESS_ID) from ADDRESS as t0_
*/
```

### count 计数

To generate a SQL `count(*)`, call the `count` function with no arguments:
要生成 SQL `count(*)` ，请调用不带参数的 `count` 函数：

```kotlin
QueryDsl.from(a).select(count())
/*
select count(*) from ADDRESS as t0_
*/
```

It is possible to pass a metamodel property to the `count` function:
可以将元模型属性传递给 `count` 函数：

```kotlin
QueryDsl.from(a).select(count(a.street))
/*
select count(t0_.STREET) from ADDRESS as t0_
*/
```

### sum

```kotlin
QueryDsl.from(a).select(sum(a.addressId))
/*
select sum(t0_.ADDRESS_ID) from ADDRESS as t0_
*/
```

### max

```kotlin
QueryDsl.from(a).select(max(a.addressId))
/*
select max(t0_.ADDRESS_ID) from ADDRESS as t0_
*/
```

### min

```kotlin
QueryDsl.from(a).select(min(a.addressId))
/*
select min(t0_.ADDRESS_ID) from ADDRESS as t0_
*/
```

## Window Functions

提供以下功能：

- rowNumber
- rank
- denseRank
- percentRank
- cumeDist
- ntile
- lag
- lead
- firstValue
- lastValue
- nthValue

### rowNumber

```kotlin
QueryDsl.from(e)
    .orderBy(e.departmentId)
    .selectNotNull(e.departmentId, rowNumber().over { orderBy(e.departmentId) })
/*
select t0_.department_id, row_number() over(order by t0_.department_id asc) from employee as t0_ order by t0_.department_id asc
*/
```

### rank

```kotlin
QueryDsl.from(e)
    .orderBy(e.departmentId)
    .selectNotNull(e.departmentId, rank().over { orderBy(e.departmentId) })
/*
select t0_.department_id, rank() over(order by t0_.department_id asc) from employee as t0_ order by t0_.department_id asc
*/
```

### denseRank

```kotlin
QueryDsl.from(e)
    .orderBy(e.departmentId)
    .selectNotNull(e.departmentId, denseRank().over { orderBy(e.departmentId) })
/*
select t0_.department_id, dense_rank() over(order by t0_.department_id asc) from employee as t0_ order by t0_.department_id asc
*/
```

### percentRank

```kotlin
QueryDsl.from(e)
    .orderBy(e.departmentId)
    .selectNotNull(e.departmentId, percentRank().over { orderBy(e.departmentId) })
/*
select t0_.department_id, percent_rank() over(order by t0_.department_id asc) from employee as t0_ order by t0_.department_id asc
*/
```

### cumeDist

```kotlin
QueryDsl.from(e)
    .orderBy(e.departmentId)
    .selectNotNull(e.departmentId, cumeDist().over { orderBy(e.departmentId) })
/*
select t0_.department_id, cume_dist() over(order by t0_.department_id asc) from employee as t0_ order by t0_.department_id asc
*/
```

### ntile

```kotlin
QueryDsl.from(e)
    .orderBy(e.departmentId)
    .selectNotNull(e.departmentId, ntile(5).over { orderBy(e.departmentId) })
/*
select t0_.department_id, ntile(5) over(order by t0_.department_id asc) from employee as t0_ order by t0_.department_id asc
*/
```

### lag

```kotlin
val c1 = d.departmentId
val c2 = lag(d.departmentId).over { orderBy(d.departmentId) }
val c3 = lag(d.departmentId, 2).over { orderBy(d.departmentId) }
val c4 = lag(d.departmentId, 2, literal(-1)).over { orderBy(d.departmentId) }

QueryDsl.from(d)
    .orderBy(d.departmentId)
    .select(c1, c2, c3, c4)
/*
select t0_.department_id, lag(t0_.department_id) over(order by t0_.department_id asc), lag(t0_.department_id, 2) over(order by t0_.department_id asc), lag(t0_.department_id, 2, -1) over(order by t0_.department_id asc) from department as t0_ order by t0_.department_id asc
*/
```

### lead

```kotlin
val d = Meta.department

val c1 = d.departmentId
val c2 = lead(d.departmentId).over { orderBy(d.departmentId) }
val c3 = lead(d.departmentId, 2).over { orderBy(d.departmentId) }
val c4 = lead(d.departmentId, 2, literal(-1)).over { orderBy(d.departmentId) }

QueryDsl.from(d)
    .orderBy(d.departmentId)
    .select(c1, c2, c3, c4)
/*
select t0_.department_id, lead(t0_.department_id) over(order by t0_.department_id asc), lead(t0_.department_id, 2) over(order by t0_.department_id asc), lead(t0_.department_id, 2, -1) over(order by t0_.department_id asc) from department as t0_ order by t0_.department_id asc
*/
```

### firstValue

```kotlin
val d = Meta.department

val c1 = d.departmentId
val c2 = firstValue(d.departmentId).over { orderBy(d.departmentId) }
val c3 = firstValue(d.departmentId).over {
    orderBy(d.departmentId)
    rows(preceding(1))
}

QueryDsl.from(d)
    .orderBy(d.departmentId)
    .select(c1, c2, c3)
/*
select t0_.department_id, first_value(t0_.department_id) over(order by t0_.department_id asc), first_value(t0_.department_id) over(order by t0_.department_id asc rows 1 preceding) from department as t0_ order by t0_.department_id asc
*/
```

### lastValue

```kotlin
val d = Meta.department

val c1 = d.departmentId
val c2 = lastValue(d.departmentId).over {
    orderBy(d.departmentId)
    rows(unboundedPreceding, unboundedFollowing)
}
val c3 = lastValue(d.departmentId).over {
    orderBy(d.departmentId)
    rows(currentRow, following(1))
}

QueryDsl.from(d)
    .orderBy(d.departmentId)
    .select(c1, c2, c3)
/*
select t0_.department_id, last_value(t0_.department_id) over(order by t0_.department_id asc rows between unbounded preceding and unbounded following), last_value(t0_.department_id) over(order by t0_.department_id asc rows between current row and 1 following) from department as t0_ order by t0_.department_id asc
*/
```

### nthValue nth值

```kotlin
val d = Meta.department

val c1 = d.departmentId
val c2 = nthValue(d.departmentId, 2).over {
    orderBy(d.departmentId)
}
val c3 = nthValue(d.departmentId, 2).over {
    orderBy(d.departmentId)
    rows(preceding(2))
}

QueryDsl.from(d)
    .orderBy(d.departmentId)
    .select(c1, c2, c3)
/*
select t0_.department_id, nth_value(t0_.department_id, 2) over(order by t0_.department_id asc), nth_value(t0_.department_id, 2) over(order by t0_.department_id asc rows 2 preceding) from department as t0_ order by t0_.department_id asc
*/
```

## Conditional expression

以下函数和表达式可用作条件表达式：

- coalesce
- case

### coalesce 合并

以下是使用该 `coalesce` 函数的示例：

```kotlin
QueryDsl.from(a).select(a.addressId, coalesce(a.street, literal("default")))
/*
select t0_.ADDRESS_ID, coalesce(t0_.STREET, 'default') from ADDRESS as t0_
*/
```

### CASE expressions CASE 表达式

要使用 CASE 表达式，请调用以下 `case` 函数：

```kotlin
val caseExpression = case(
  When(
    {
      a.street eq "STREET 2"
      a.addressId greater 1
    },
    literal("HIT")
  )
) { literal("NO HIT") }
val list: List<Pair<String?, String?>> = db.runQuery {
  QueryDsl.from(a).where { a.addressId inList listOf(1, 2, 3) }
    .orderBy(a.addressId)
    .select(a.street, caseExpression)
}
/*
select t0_.street, case when t0_.street = ? and t0_.address_id > ? then 'HIT' else 'NO HIT' end from address as t0_ where t0_.address_id in (?, ?, ?) order by t0_.address_id asc
*/
```

## Scalar subqueries

使用聚合函数返回标量的查询是标量子查询。标量子查询可以传递给另一个查询的 `select` 函数：

```kotlin
val subquery = QueryDsl.from(e).where { d.departmentId eq e.departmentId }.select(count())
val query = QueryDsl.from(d)
    .orderBy(d.departmentId)
    .select(d.departmentName, subquery)
/*
select t0_.department_name, (select count(*) from employee as t1_ where t0_.department_id = t1_.department_id) from department as t0_ order by t0_.department_id asc
*/
```

## Literals

若要在不绑定变量的情况下将值作为文本直接嵌入到 SQL 中，请调用该 `literal` 函数。

该 `literal` 函数支持以下参数类型：

- Boolean
- Int
- Long
- String

## User-defined expressions

### Custom comparison operators

在用作 `org.komapper.core.dsl.operator.CriteriaContext` 构造函数参数的类中定义自定义比较运算符。生成与运算符对应的 SQL 的逻辑作为 lambda 函数添加到 CriteriaContext 中。

在下面的示例中，定义了 `~` and `!~` 运算符：

```kotlin
class MyExtension(private val context: CriteriaContext) {

    infix fun <T : Any> ColumnExpression<T, String>.`~`(pattern: T?) {
        if (pattern == null) return
        val o1 = Operand.Column(this)
        val o2 = Operand.Argument(this, pattern)
        context.add {
            visit(o1)
            append(" ~ ")
            visit(o2)
        }
    }

    infix fun <T : Any> ColumnExpression<T, String>.`!~`(pattern: T?) {
        if (pattern == null) return
        val o1 = Operand.Column(this)
        val o2 = Operand.Argument(this, pattern)
        context.add {
            visit(o1)
            append(" !~ ")
            visit(o2)
        }
    }
}
```

若要使用运算符，请在 Where 或 Having 等声明中调用该 `extension` 函数。指定上述构造函数和 lambda 表达式以调用运算符作为 `extension` 函数的参数。

您可以在查询中使用 `~` and `!~` 运算符，如下所示：

```kotlin
QueryDsl.from(e).where {
    e.salary greaterEq BigDecimal(1000)
    extension(::MyExtension) {
        e.employeeName `~` "S"
        e.employeeName `!~` "T"
    }
}.orderBy(e.employeeName)
/*
select 
    t0_.EMPLOYEE_ID, 
    t0_.EMPLOYEE_NO, 
    t0_.EMPLOYEE_NAME, 
    t0_.MANAGER_ID, 
    t0_.HIREDATE, 
    t0_.SALARY, 
    t0_.DEPARTMENT_ID, 
    t0_.ADDRESS_ID, 
    t0_.VERSION 
from 
    EMPLOYEE as t0_ 
where 
    t0_.SALARY >= ?
    t0_.EMPLOYEE_NAME ~ ?
    t0_.EMPLOYEE_NAME !~ ?
order by
    t0_.EMPLOYEE_NAME
*/
```

### Custom column expressions

将自定义列表达式定义为返回 `org.komapper.core.dsl.expression.ColumnExpression` .您可以通过调用 `org.komapper.core.dsl.operator.columnExpression` 进行创建 `ColumnExpression` 。将列表达式的类型、用于唯一标识列表达式的信息以及用于生成 SQL 的 lambda 表达式传递给 `columnExpression` 。

```kotlin
private fun <T: Any> replace(
    expression: ColumnExpression<T, String>,
    from: T,
    to: T,
): ColumnExpression<T, String> {
    val name = "replace"
    val o1 = Operand.Column(expression)
    val o2 = Operand.Argument(expression, from)
    val o3 = Operand.Argument(expression, to)
    return columnExpression(expression, name, listOf(o1, o2, o3)) {
        append("$name(")
        visit(o1)
        append(", ")
        visit(o2)
        append(", ")
        visit(o3)
        append(")")
    }
}
```