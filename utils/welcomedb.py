from YukkiMusic.core.mongo import mongodb

greetingsdb = mongodb.greetings

greeting_message = {
    "welcome": {},
    "goodbye": {}
}

async def get_greeting(chat_id: int, greeting_type: str) -> (str, str, str):
    data = await greetingsdb.find_one({"chat_id": chat_id, "type": greeting_type})
    if not data:
        return "", "", ""

    message = data.get("message", "")
    raw_text = data.get("raw_text", "")
    file_id = data.get("file_id", "")

    return message, raw_text, file_id

async def set_greeting(
    chat_id: int, greeting_type: str, message: str, raw_text: str, file_id: str
):
    update_data = {
        "message": message,
        "raw_text": raw_text,
        "file_id": file_id,
        "type": greeting_type,
    }

    return await greetingsdb.update_one(
        {"chat_id": chat_id, "type": greeting_type}, {"$set": update_data}, upsert=True
    )

async def del_greeting(chat_id: int, greeting_type: str):
    return await greetingsdb.delete_one({"chat_id": chat_id, "type": greeting_type})

async def get_welcome(chat_id: int) -> (str, str, str):
    return await get_greeting(chat_id, "welcome")


async def set_welcome(chat_id: int, welcome: str, raw_text: str, file_id: str):
    return await set_greeting(chat_id, "welcome", welcome, raw_text, file_id)


async def del_welcome(chat_id: int):
    return await del_greeting(chat_id, "welcome")


async def get_goodbye(chat_id: int) -> (str, str, str):
    return await get_greeting(chat_id, "goodbye")


async def set_goodbye(chat_id: int, goodbye: str, raw_text: str, file_id: str):
    return await set_greeting(chat_id, "goodbye", goodbye, raw_text, file_id)


async def del_goodbye(chat_id: int):
    return await del_greeting(chat_id, "goodbye")


async def get_clean_greetings(chat_id: int, greeting_type: str) -> bool:
    data = await greetingsdb.find_one({"chat_id": chat_id, "type": greeting_type})
    if not data:
        return False

    clean = data.get("clean", "off").lower()
    return clean in ["yes", "on"]


async def set_clean_greetings(chat_id: int, greeting_type: str, clean: bool) -> bool:
    clean_value = "on" if clean else "off"
    result = await greetingsdb.update_one(
        {"chat_id": chat_id, "type": greeting_type},
        {"$set": {"clean": clean_value}},
        upsert=True,
    )
    return result.modified_count > 0 or result.upserted_id is not None


async def get_welcome_clean(chat_id: int) -> bool:
    return await get_clean_greetings(chat_id, "welcome")


async def set_welcome_clean(chat_id: int, clean: bool) -> bool:
    return await set_clean_greetings(chat_id, "welcome", clean)


async def get_goodbye_clean(chat_id: int) -> bool:
    return await get_clean_greetings(chat_id, "goodbye")


async def set_goodbye_clean(chat_id: int, clean: bool) -> bool:
    return await set_clean_greetings(chat_id, "goodbye", clean)

async def get_old_message(chat_id: int, greeting_type: str) -> int:
    return greeting_message[greeting_type].get(chat_id, 0)


async def set_old_message(chat_id: int, greeting_type: str, message_id: int):
    greeting_message[greeting_type][chat_id] = message_id
    return True

async def get_old_welcome(chat_id: int) -> int:
    return await get_old_message(chat_id, "welcome")


async def set_old_welcome(chat_id: int, message_id: int) -> bool:
    return await set_old_message(chat_id, "welcome", message_id)


async def get_old_goodbye(chat_id: int) -> int:
    return await get_old_message(chat_id, "goodbye")


async def set_old_goodbye(chat_id: int, message_id: int) -> bool:
    return await set_old_message(chat_id, "goodbye", message_id)

