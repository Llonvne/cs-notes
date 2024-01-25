package org.komapper.example.model.address

import org.komapper.annotation.*

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

