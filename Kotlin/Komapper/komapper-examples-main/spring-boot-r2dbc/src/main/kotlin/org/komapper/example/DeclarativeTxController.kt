package org.komapper.example

import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.withContext
import org.komapper.core.dsl.Meta
import org.komapper.core.dsl.QueryDsl
import org.komapper.core.dsl.query.EntityStore
import org.komapper.core.dsl.query.EntityStoreContext
import org.komapper.core.dsl.query.asContext
import org.komapper.example.model.address.*
import org.komapper.example.model.message.Message
import org.komapper.example.model.message.message
import org.komapper.r2dbc.R2dbcDatabase
import org.springframework.transaction.annotation.Transactional
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RequestParam
import org.springframework.web.bind.annotation.RestController

@RequestMapping("/")
@RestController
@Transactional
class DeclarativeTxController(private val database: R2dbcDatabase) {

    @RequestMapping
    suspend fun list(): Flow<Message> {
        return database.flowQuery {
            val m = Meta.message
            QueryDsl.from(m)
                .orderBy(m.id)
        }
    }

    @RequestMapping(params = ["text"])
    suspend fun add(@RequestParam text: String): Message {
        val message = Message(text = text)

        return database.runQuery {
            val m = Meta.message
            QueryDsl.insert(m).single(message)
        }
    }

    operator fun <R : Any> EntityStore.invoke(block: context(EntityStoreContext) () -> R): R {
        return block(this.asContext())
    }

    suspend fun a() {
        val a = Meta.address
        val e = Meta.employee
        val d = Meta.department

        val query = QueryDsl.from(a)
            .innerJoin(e) {
                a.addressId eq e.addressId
            }.innerJoin(d) {
                e.departmentId eq d.departmentId
            }.includeAll()

        val store: EntityStore = database.runQuery(query)

        withContext(Dispatchers.IO) {
            store {
                for (department in departments()) {
                    val employees = department.employees()
                    for (employee in employees) {
                        val address = employee.address()
                        println("department=${department.departmentName}, employee=${employee.employeeName}, address=${address?.street}")
                    }
                }
            }
        }
    }
}
