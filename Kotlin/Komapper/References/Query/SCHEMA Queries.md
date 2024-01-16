# SCHEMA Queries

SCHEMA 查询从映射定义生成以下 DDL 语句：

- 对应于实体类的表的 CREATE/DROP 语句
- 生成实体 ID 值的序列的 CREATE/DROP 语句

## create

要生成 CREATE 语句，请调用以下 `create` 函数：

```kotlin
val query: Query<Unit> = QueryDsl.create(Meta.address, Meta.employee)
/*
create table if not exists ADDRESS (ADDRESS_ID integer not null, STREET varchar(500) not null, VERSION integer not null, constraint pk_ADDRESS primary key(ADDRESS_ID));
create table if not exists EMPLOYEE (EMPLOYEE_ID integer not null, EMPLOYEE_NO integer not null, EMPLOYEE_NAME varchar(500) not null, MANAGER_ID integer, HIREDATE date not null, SALARY bigint not null, DEPARTMENT_ID integer not null, ADDRESS_ID integer not null, VERSION integer not null, constraint pk_EMPLOYEE primary key(EMPLOYEE_ID));
*/
```

## drop

若要生成 DROP 语句，请调用以下 `drop` 函数：

```kotlin
val query: Query<Unit> = QueryDsl.drop(Meta.address, Meta.employee)
/*
drop table if exists ADDRESS;
drop table if exists EMPLOYEE;
*/
```

## options

**pass**