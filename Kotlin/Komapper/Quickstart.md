## Quickstart

[Komapper Quickstart](https://www.komapper.org/docs/quickstart/)

### Build Script 构建脚本

```kotlin
plugins {
    application
    id("com.google.devtools.ksp") version "1.9.22-1.0.16"
    kotlin("jvm") version "1.9.22"
}

dependencies {
    val komapperVersion = "1.16.0"
  
  	// Kotlin Jvm
    platform("org.komapper:komapper-platform:$komapperVersion").let {
        implementation(it)
        ksp(it)
    }
    ksp("org.komapper:komapper-processor")
    // Kotlin Multiplatform 
  	dependencies {
    	add("kspCommonMainMetadata", "org.komapper:komapper-processor:$komapperVersion")
    	add("kspJvm", "org.komapper:komapper-processor:$komapperVersion")
		}
  	
  	// For JDBC 
    implementation("org.komapper:komapper-starter-jdbc")
    implementation("org.komapper:komapper-dialect-h2-jdbc")
  
    testImplementation("org.junit.jupiter:junit-jupiter-api:5.8.2")
    testRuntimeOnly("org.junit.jupiter:junit-jupiter-engine:5.8.2")
}
```

##  Entity Class

```kotlin
@KomapperEntity
data class Employee(
  @KomapperId @KomapperAutoIncrement
  val id: Int = 0,
  val name: String,
  @KomapperVersion
  val version: Int = 0,
  @KomapperCreatedAt
  val createdAt: LocalDateTime = LocalDateTime.MIN,
  @KomapperUpdatedAt
  val updatedAt: LocalDateTime = LocalDateTime.MIN,
)
```

## Query

```kotlin
fun main() {
  // (1) create a database instance
  val database = JdbcDatabase("jdbc:h2:mem:quickstart;DB_CLOSE_DELAY=-1")

  // (2) start transaction
  database.withTransaction {

    // (3) get an entity metamodel
    val e = Meta.employee

    // (4) create schema
    database.runQuery {
      QueryDsl.create(e)
    }

    // (5) insert multiple employees at once
    database.runQuery {
      QueryDsl.insert(e).multiple(Employee(name = "AAA"), Employee(name = "BBB"))
    }

    // (6) select all
    val employees = database.runQuery {
      QueryDsl.from(e).orderBy(e.id)
    }

    // (7) print all results
    for ((i, employee) in employees.withIndex()) {
      println("RESULT $i: $employee")
    }
  }
}
```

