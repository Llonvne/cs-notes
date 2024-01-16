# Entity Classes

在 Komapper 中，与数据库表对应的 Kotlin 类称为实体类。

使用注释映射定义对于将实体类映射到表是必需的。

## Entity class definitions

实体类必须满足以下要求：

* 成为数据类
* 可见性不是私有的
* 无类型参数

## Mapping definitions

有两种方法可以创建映射定义：

* 实体类本身有自己的映射定义（自映射）
* 独立于实体类的类具有映射定义（分离映射）

### Self mapping

除了上一节中描述的要求外，实体类还必须满足以下条件：

注释 `@KomapperEntity`

```kotlin
@KomapperEntity
data class Address(
  @KomapperId
  @KomapperAutoIncrement
  @KomapperColumn(name = "ADDRESS_ID")
  val id: Int = 0,
  val street: String,
  @KomapperVersion
  val version: Int = 0,
  @KomapperCreatedAt
  val createdAt: LocalDateTime? = null,
  @KomapperUpdatedAt
  val updatedAt: LocalDateTime? = null,
)
```

### Separation mapping 

映射类必须满足以下要求：

* 成为数据类
* 可见性不是私有的
* 使用 `@KomapperEntityDef` 实体类进行注释并接受实体类作为参数
* 没有名称与实体类中定义的名称不同的属性

```kotlin
@KomapperEntityDef(Address::class)
data class AddressDef(
  @KomapperId
  @KomapperAutoIncrement
  @KomapperColumn(name = "ADDRESS_ID")
  val id: Nothing,
  @KomapperVersion
  val version: Nothing,
  @KomapperCreatedAt
  val createdAt: Nothing,
  @KomapperUpdatedAt
  val updatedAt: Nothing,
)
```

对分隔映射中的属性类型没有限制。我们在上面的例子中使用 `Nothing` 。

### aliases

在上面的示例中，扩展属性的名称是 `address` 。但是，可以使用 `@KomapperEntity` or `@KomapperEntityDef` aliases 属性进行更改。

```kotlin
@KomapperEntity(aliases = ["addr"])
```

可以为 `aliases` 属性指定多个名称。在这种情况下，每个名称都公开为不同的实例。需要多个不同实例的主要用例是自联接和子查询。

例如，若要获取经理列表，请使用上述定义创建以下查询：

```kotlin
val e = Meta.employee
val m = Meta.manager
val query: Query<List<Employee>> = QueryDsl.from(m)
  .distinct()
  .innerJoin(e) {
    m.employeeId eq e.managerId
  }
```

即使你没有提前定义一个有名字的元模型，你也可以使用这个 `clone` 函数来实现同样的事情：

### unit

在上面的示例中，它 `org.komapper.core.dsl.Meta` 具有 `address` 扩展属性。但是，可以使用 `@KomapperEntity` or `@KomapperEntityDef` unit 属性进行更改。

```kotlin
object MyMeta

@KomapperEntity(unit = MyMeta::class)
data class Address(
  ...
)
```

如上所述定义时，属性中的指定对象将具有 `address` 扩展 `unit` 属性：

```kotlin
// get a generated metamodel
val a = MyMeta.address

// define a query
val query = QueryDsl.from(a).where { a.street eq "STREET 101" }.orderBy(a.id)
```

### clone

该 `clone` 函数可用于基于现有元模型生成另一个元模型。主要用例是将数据复制到具有相同数据结构但名称不同的表中。

```kotlin
val a = Meta.address
val archive = a.clone(table = "ADDRESS_ARCHIVE")
val query = QueryDsl.insert(archive).select {
  QueryDsl.from(a).where { a.id between 1..5 }
}
```

如果要像公开任何其他元模型一样公开克隆的元模型，请使用该对象来保存实例并定义该 `Meta` 对象的扩展属性。

```kotlin
object MetamodelHolder {
  private val _addressArchive = Meta.address.clone(table = "ADDRESS_ARCHIVE")
  val Meta.addressArchive get() = _addressArchive
}
```

### define

可以使用该 `define` 函数为元模型定义默认的 WHERE 子句。当您希望在使用特定元模型时始终使用相同的搜索条件时，这很有用。

```kotlin
object MessageMetaHolder {
    /**
     * 定义默认的 Where 子句
     */
    private val idEq100: _MessageDef = Meta.message.define { d ->
        where {
            d.id eq 100
        }
    }

    /**
     * 通过 Meta 公开
     */
    val Meta.newMessage get() = idEq100
}
```

如果查询具有 WHERE 子句，则搜索条件将与 AND 谓词连接起来。

即使定义的元模型是联接的目标，此功能也有效。

它不仅对 SELECT 语句有效，而且对 UPDATE 和 DELETE 语句也有效。

如果要将参数传递给默认的 WHERE 子句，可以将其定义为扩展函数。但请注意，**元模型每次都是不同的实例**。

<img src="./assets/CleanShot 2024-01-16 at 09.38.57@2x.png" alt="CleanShot 2024-01-16 at 09.38.57@2x" style="zoom:50%;" />

## List of annotations for classes

### @KomapperEntity

指示实体类具有映射定义。它具有别名和单元属性。

### @KomapperEntityDef

指示类是映射定义。您可以指定实体、别名和单元属性。

### @KomapperTable

显式指定表名。

### @KomapperProjection

允许将查询结果投影到实体中。

该 `function` 属性允许您指定生成的扩展函数的名称。如果未指定，则名称将为 `selectAs + the simple name of the entity class` ，如 `selectAsAddress` 。扩展函数是为 和 `TemplateSelectQueryBuilder`生成的 `SelectQuery` 。

## List of annotations for properties

### @KomapperId

指示它是主键。若要表示复合主键，可以在单个实体类中指定多个此注释。

### @KomapperSequence

指示主键由数据库序列生成。必须始终与 `@KomapperId` .

提供此批注的属性类型必须是下列类型之一：

* Int

* Long

* UInt

* Value class with a property of one of the above types

### @KomapperAutoIncrement

表示主键由数据库的自增列生成。必须始终与 `@KomapperId` .

### @KomapperVersion

指示这是用于开放式锁定的版本号。

指定此注释时，将对 UPDATE 和 DELETE 操作执行乐观锁定。

### @KomapperCreatedAt

指示插入时的时间戳。

提供此批注的属性类型必须是下列类型之一：

- java.time.Instant
- java.time.LocalDateTime
- java.time.OffsetDateTime
- kotlinx.datetime.Instant
- kotlinx.datetime.LocalDateTime
- Value class with a property of one of the above types
  具有上述类型之一属性的 Value 类

### @KomapperUpdatedAt

指示这是更新时的时间戳。

### @KomapperEnum

显式指定如何将枚举属性映射到列。

* EnumType.NAME
  将 `name` class 的 `Enum` 属性映射到 String 类型列。

* EnumType.ORDINAL
  将 `ordinal` class 的 `Enum` 属性映射到 Integer 类型列。

* EnumType.PROPERTY
  将 class 的 `Enum` 任意属性映射到列。必须在 的属性中指定要映射的 `hint` `@KomapperEnum` 属性的名称。

```kotlin
@KomapperEnum(EnumType.PROPERTY, hint = "code")
val side: Color

enum class Color(val code: String) { RED("r"), GREEN("g"), BLUE("b") }
```

* EnumType.TYPE 枚举类型
  将 `Enum` 类映射到枚举类型列。请注意，需要与 Enum 类对应的用户定义数据类型。

### @KomapperColumn

显式指定要映射到属性的列的名称。

如果该 `alwaysQuote` 属性设置为 `true` ，则生成的 SQL 中的标识符将被引用。

如果该 `masking` 属性设置为 `true` ，则日志中将屏蔽相应的数据。

如果使用该 `alternateType` 属性，则可以更改要映射的 SQL 类型。有关模式详细信息，请参阅备用类型。

### @KomapperIgnore

指示它不受映射的约束。

指示复合主键的嵌入值。

```kotlin
data class EmoloyeeId(val id1: Int, val id2: String)

@KomapperEntity
data class Employee(@KomapperEmbeddedId val id: EmoloyeeId, val name: String)
```

### Embedded Value

<img src="./assets/CleanShot 2024-01-16 at 10.08.54@2x.png" alt="CleanShot 2024-01-16 at 10.08.54@2x" style="zoom:50%;" />

### @KomapperEmbeddedId

指示复合主键的嵌入值。

### @KomapperEmbedded

指示嵌入值。

### @KomapperEnumOverride

应用于 `@KomapperEnum` 嵌入值中的枚举属性。

### @KomapperColumnOverride

应用于 `@KomapperColumn` 嵌入值中的属性。