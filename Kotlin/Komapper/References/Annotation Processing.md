# Annotation Processing

Komapper 使用 Kotlin 符号处理 API （KSP） 处理映射定义中的注释，并在编译时将结果生成为元模型源代码。

## Options

选项允许您更改注释处理器的行为。可用选项如下：

- komapper.prefix
- komapper.suffix
- komapper.enumStrategy
- komapper.namingStrategy
- komapper.metaObject
- komapper.alwaysQuote
- komapper.enableEntityMetamodelListing
- komapper.enableEntityStoreContext
- komapper.enableEntityProjection

```kotlin
ksp {
  arg("komapper.prefix", "")
  arg("komapper.suffix", "Metamodel")
  arg("komapper.enumStrategy", "ordinal")
  arg("komapper.namingStrategy", "UPPER_SNAKE_CASE")
  arg("komapper.metaObject", "example.Metamodels")
  arg("komapper.alwaysQuote", "true")
  arg("komapper.enableEntityMetamodelListing", "true")
  arg("komapper.enableEntityStoreContext", "true")
  arg("komapper.enableEntityProjection", "true")
}
```

### komapper.prefix

This option specifies the prefix for the simple name of generated metamodel class. The default value is `_` (underscore).
此选项指定生成的元模型类的简单名称的前缀。默认值为 `_` （下划线）。

### komapper.suffix

此选项指定生成的元模型类名称的后缀。默认值为空字符串。

### komapper.enumStrategy

此选项指定如何将枚举属性映射到数据库列的策略。该值可以是 `ordinal` 或 `name` 。缺省值为 `name` 。

请注意，规范依据 `@KomapperEnum` 优先于此策略。

该 `komapper.enumStrategy` 选项的可能值定义如下：

- name 名字：将 `name` class 的 `Enum` 属性映射到 String 类型列。
- ordinal 序数：将 `ordinal` class 的 `Enum` 属性映射到 Integer 类型列。
- type 类型：将 `Enum` 类映射到枚举类型列。请注意，需要与 Enum 类对应的用户定义数据类型。

### komapper.namingStrategy

此选项指定了如何从 Kotlin 实体类和属性中解析数据库表名和列名的策略。

该 `komapper.namingStrategy` 选项的可能值定义如下：

* implicit 
  这种策略不会转换任何内容。实体类和属性名称按原样用作表名和列名。

* lower_snake_case
  此策略将实体类和属性名称转换为snake_case，然后转换为小写。

* UPPER_SNAKE_CASE
  此策略将实体类和属性名称转换为 snake_case，然后转换为 UPPERCASE。

缺省策略是 `lower_snake_case` 。

### komapper.metaObject

此选项指定提供元模型实例作为扩展属性的对象的名称。缺省值为 `org.komapper.core.dsl.Meta` 。

### komapper.alwaysQuote

此选项指示是否在 SQL 语句中引用表名或列名。缺省值为 `flase` 。

### komapper.enableEntityMetamodelListing

此选项指示实体元模型列表是否可用。缺省值为 `flase` 。

如果将此选项设置为 `true` ，则可以通过以下方式获取列表：

```kotlin
val metamodels: List<EntityMetamodel<*, *, *>> = Meta.all()
val metamodels: List<EntityMetamodel<*, *, *>> = EntityMetamodels.list(Meta)
```

### komapper.enableEntityStoreContext

是否启用 `EntityStore` 上下文。缺省值为 `false` 。

如果此选项设置为 `true` ，则 Komapper 的注释处理器将为使用上下文接收器的关联 API 生成代码。

### komapper.enableEntityProjection

此设置确定是否启用将查询结果投影到实体中。启用后，将为所有实体类生成两者 `SelectQuery` 的 `TemplateSelectQueryBuilder` 扩展函数。缺省值为 `false` 。

扩展函数的名称将格式为 `selectAs + the simple name of the entity class`

如果要更改扩展函数的名称或仅对特定实体类启用投影，请使用 `@KomapperProjection` 注解。