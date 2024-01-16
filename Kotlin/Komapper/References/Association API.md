# Association API

通过关联 API，可以轻松地从通过执行指定 include 或 includeAll 的查询获取的 EntityStore 中导航关联对象。

使用专用批注对实体类（或实体定义类）进行批注会生成用于导航关联对象的实用程序函数。

>关联 API 是一项实验性功能。要使用它，请将以下代码添加到您的 Gradle 构建脚本中：
>
>```kotlin
>tasks {
>    withType<org.jetbrains.kotlin.gradle.tasks.KotlinCompile>().configureEach {
>        kotlinOptions.freeCompilerArgs += listOf("-opt-in=org.komapper.annotation.KomapperExperimentalAssociation")
>    }
>}
>```

## Annotations

### @KomapperOneToOne

指示带批注的实体类与目标实体类之间的一对一关系。

The `targetEntity` property specifies the entity class (or entity definition class) associated with the annotated class. The specification is required.
该 `targetEntity` 属性指定与带批注的类关联的实体类（或实体定义类）。规范是必需的。

The `navigator` property specifies the name of a utility function for navigating the association. If not specified, it is inferred from the value specified for the `targetEntity` property.
该 `navigator` 属性指定用于导航关联的实用工具函数的名称。如果未指定，则从为 `targetEntity` 属性指定的值推断。

根据上述定义生成以下效用函数：

```kotlin
fun example.Employee.`address`(
    store: org.komapper.core.dsl.query.EntityStore,
    source: example._Employee = org.komapper.core.dsl.Meta.`employee`,
    target: example._Address = org.komapper.core.dsl.Meta.`address`,
): example.Address? {
    return store.oneToOne(source, target)[this]
}
```

### @KomapperManyToOne

指示带批注的实体类与目标实体类之间的多对一关系。

### @KomapperOneToMany

指示带批注的实体类与目标实体类之间的一对多关系。

### @KomapperLink

指示关联的源实体元模型和关联的目标实体元模型。

### @KomapperAggregateRoot

指示带批注的实体类（或实体定义类）是聚合根

## Example

### Entity class definitions 

假设我们有以下实体类定义：

```kotlin
@KomapperEntity
@KomapperOneToOne(targetEntity = Employee::class)
data class Address(
    @KomapperId
    val addressId: Int,
    val street: String,
)

@KomapperEntity
@KomapperAggregateRoot("departments")
@KomapperOneToMany(targetEntity = Employee::class, navigator = "employees")
data class Department(
    @KomapperId
    val departmentId: Int,
    val departmentName: String,
)

@KomapperEntity
@KomapperManyToOne(targetEntity = Department::class)
@KomapperOneToOne(targetEntity = Address::class)
data class Employee(
    @KomapperId
    val employeeId: Int,
    val employeeName: String,
    val departmentId: Int,
    val addressId: Int,
)
```

### Navigation code 导航代码

我们可以使用生成的实用程序函数简洁地从 `EntityStore` 中检索关联对象：

```kotlin
val a = Meta.address
val e = Meta.employee
val d = Meta.department

val query = QueryDsl.from(a)
    .innerJoin(e) {
        a.addressId eq e.addressId
    }.innerJoin(d) {
        e.departmentId eq d.departmentId
    }.includeAll()

val store: EntityStore = db.runQuery(query)

for (department in store.departments()) {
    val employees = department.employees(store)
    for (employee in employees) {
        val address = employee.address(store)
        println("department=${department.departmentName}, employee=${employee.employeeName}, address=${address?.street}")
    }
}
```

### Navigation code using context receiver 使用上下文接收器的导航代码

启用 komapper.enableEntityStoreContext 选项后，无需显式传递 `EntityStore` 参数，从而可以更简洁地导航关联对象。

```kotlin
val a = Meta.address
val e = Meta.employee
val d = Meta.department

val query = QueryDsl.from(a)
    .innerJoin(e) {
        a.addressId eq e.addressId
    }.innerJoin(d) {
        e.departmentId eq d.departmentId
    }.includeAll()

val store: EntityStore = db.runQuery(query)

with(store.asContext()) {
    for (department in departments()) {
        val employees = department.employees()
        for (employee in employees) {
            val address = employee.address()
            println("department=${department.departmentName}, employee=${employee.employeeName}, address=${address?.street}")
        }
    }
}
```