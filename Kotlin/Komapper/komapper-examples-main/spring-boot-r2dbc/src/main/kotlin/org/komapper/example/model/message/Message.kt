package org.komapper.example.model.message

import org.komapper.annotation.KomapperAutoIncrement
import org.komapper.annotation.KomapperEntityDef
import org.komapper.annotation.KomapperId
import org.komapper.annotation.KomapperProjection

data class Message(
    val id: Int? = null,
    val text: String,
)

@KomapperEntityDef(Message::class)
@KomapperProjection
data class MessageDef(
    @KomapperId @KomapperAutoIncrement
    val id: Nothing,
)
