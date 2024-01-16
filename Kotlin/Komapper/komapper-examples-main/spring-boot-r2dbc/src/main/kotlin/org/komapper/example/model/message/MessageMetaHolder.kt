package org.komapper.example.model.message

import org.komapper.core.dsl.Meta
import org.komapper.core.dsl.metamodel.define

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

    private fun Meta.idEq(id: Int) = Meta.message.define { d ->
        where {
            d.id eq id
        }
    }
}
