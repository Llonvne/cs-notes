# Data Types

本节介绍 Kotlin 和 SQL 之间的数据类型映射。

方言决定了 Kotlin 和 SQL 之间的默认数据类型映射。

## Postgres Data Types

<img src="./assets/CleanShot 2024-01-15 at 21.53.37@2x.png" alt="CleanShot 2024-01-15 at 21.53.37@2x" style="zoom:50%;" />

<img src="./assets/CleanShot 2024-01-15 at 21.53.56@2x.png" alt="CleanShot 2024-01-15 at 21.53.56@2x" style="zoom:50%;" />

<img src="./assets/CleanShot 2024-01-15 at 21.54.11@2x.png" alt="CleanShot 2024-01-15 at 21.54.11@2x" style="zoom:50%;" />

## User-defined data types

要将用户定义的 Kotlin 数据类型映射到 SQL 数据类型，必须创建并注册符合服务提供程序接口规范的类。

例如，假设您要将以下 Kotlin 数据类型映射 `example.Age` 到 SQL INTEGER 类型。

```kotlin
package example

data class Age(val value: Int)
```

**In the case of R2DBC**

创建一个实现 `org.komapper.r2dbc.spi.R2dbcUserDefinedDataType` 以执行映射的类：

```kotlin
package example.r2dbc

import example.Age
import io.r2dbc.spi.Row
import io.r2dbc.spi.Statement
import org.komapper.r2dbc.spi.R2dbcUserDefinedDataType
import kotlin.reflect.KClass

class AgeType : R2dbcUserDefinedDataType<Age> {

    override val name: String = "integer"

    override val klass: KClass<Age> = Age::class

    override val r2dbcType: Class<Int> = Int::class.javaObjectType

    override fun getValue(row: Row, index: Int): Age? {
        return row.get(index, Int::class.javaObjectType)?.let { Age(it) }
    }

    override fun getValue(row: Row, columnLabel: String): Age? {
        return row.get(columnLabel, Int::class.javaObjectType)?.let { Age(it) }
    }

    override fun setValue(statement: Statement, index: Int, value: Age) {
        // The second argument must be of the same type as the r2dbcType property.
        statement.bind(index, value.value)
    }

    override fun setValue(statement: Statement, name: String, value: Age) {
        // The second argument must be of the same type as the r2dbcType property.
        statement.bind(name, value.value)
    }

    override fun toString(value: Age): String {
        return value.value.toString()
    }
}
```

在具有以下名称的文件中注册上述类：

``META-INF/services/org.komapper.r2dbc.spi.R2dbcUserDefinedDataType``

此文件包含类的完全限定名称，如下所示：

`example.r2dbc.AgeType`

## Data type conversion

若要将一种数据类型转换为另一种类型，必须创建并注册符合服务提供程序接口规范的类。

例如，假设您希望在应用程序中处理 `Int` 以下内容 `example.PhoneNumber` 。

创建一个实现 `org.komapper.core.spi.DataTypeConverter` 以执行转换的类：

```kotlin
package example

import org.komapper.core.spi.DataTypeConverter
import kotlin.reflect.KClass

class PhoneNumberTypeConverter : DataTypeConverter<PhoneNumber, Int> {
    override val exteriorClass: KClass<PhoneNumber> = PhoneNumber::class
    override val interiorClass: KClass<Int> = Int::class

    override fun unwrap(exterior: PhoneNumber): Int {
        return exterior.value
    }

    override fun wrap(interior: Int): PhoneNumber {
        return PhoneNumber(interior)
    }
}
```

在具有以下名称的文件中注册上述类：

``META-INF/services/org.komapper.core.spi.DataTypeConverter`

此文件包含类的完全限定名称，如下所示：

`example.PhoneNumberTypeConverter`

## Value classes

使用值类时，值类的内部类型用于映射。

## Alternate types

可以通过为属性指定值类来更改要映射的 `@KomapperColumn.alternateType` SQL 类型。

例如，如果要映射 `kotlin.String` 到 `CLOB` or `TEXT` 而不是 `VARCHAR` 或 `VARCHAR2` ，请指定 `org.komapper.core.type.ClobString` 。

```kotlin
@KomapperColumn(alternateType = ClobString::class)
val description: String
```

该 `alternateType` 属性允许用户指定自己的值类。但是，必须创建并注册与该值类对应的用户定义数据类型。

请注意，值类必须满足以下要求：

* 构造函数必须是公共的

- Parameter 属性必须是公共的且不可为 null
- 参数属性类型必须与批注的 `@KomapperColumn` 实体属性类型匹配

## Support for kotlinx-datetime

Komapper 支持以下类型的 kotlinx-datetime：

- kotlinx.datetime.Instant
- kotlinx.datetime.LocalDate
- kotlinx.datetime.LocalDateTime

要使用这些类型，请在 Gradle 依赖项声明中声明 `kotlinx-datetime` 如下：

```kotlin
dependencies {
    implementation("org.jetbrains.kotlinx:kotlinx-datetime:0.3.2")
}
```

另外，声明 `komapper-datetime-jdbc` 或 `komapper-datetime-r2dbc` ：

```kotlin
val komapperVersion: String by project
dependencies {
    runtimeOnly("org.komapper:komapper-datetime-jdbc:$komapperVersion")
}
```

如果使用其中一个 Starter ，则无需声明 `komapper-datetime-jdbc` 和 `komapper-datetime-r2dbc`。