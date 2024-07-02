# dante
from DanteMusic.core.mongo import mongodb

greetingsdb = mongodb.greetings

# In-memory storage for old messages
greeting_message = {
    "welcome": {},
    "goodbye": {}
}

# in used
async def set_welcome(chat_id: int, message: str, raw_text: str, file_id: str):
    update_data = {
        "message": message,
        "raw_text": raw_text,
        "file_id": file_id,
        "type": "welcome"
    }

    return await greetingsdb.update_one(
        {"chat_id": chat_id, "type": "welcome"}, {"$set": update_data}, upsert=True
    )
# in used
async def set_goodbye(chat_id: int, message: str, raw_text: str, file_id: str):
    update_data = {
        "message": message,
        "raw_text": raw_text,
        "file_id": file_id,
        "type": "goodbye"
    }

    return await greetingsdb.update_one(
        {"chat_id": chat_id, "type": "goodbye"}, {"$set": update_data}, upsert=True
    )
# in used
async def get_welcome(chat_id: int) -> (str, str, str):
    data = await greetingsdb.find_one({"chat_id": chat_id, "type": "welcome"})
    if not data:
        return "", "", ""

    message = data.get("message", "")
    raw_text = data.get("raw_text", "")
    file_id = data.get("file_id", "")

    return message, raw_text, file_id
# in used
async def del_welcome(chat_id: int):
    return await greetingsdb.delete_one({"chat_id": chat_id, "type": "welcome"})

async def get_goodbye(chat_id: int) -> (str, str, str):
    data = await greetingsdb.find_one({"chat_id": chat_id, "type": "goodbye"})
    if not data:
        return "", "", ""

    message = data.get("message", "")
    raw_text = data.get("raw_text", "")
    file_id = data.get("file_id", "")

    return message, raw_text, file_id
# in used
async def del_goodbye(chat_id: int):
    return await greetingsdb.delete_one({"chat_id": chat_id, "type": "goodbye"})

# not in used
async def is_greetings_clean_on(chat_id: int, greeting_type: str) -> bool:
    data = await greetingsdb.find_one({"chat_id": chat_id, "type": greeting_type})
    if not data:
        return None

    clean = data.get("clean", None)
    if clean is None:
        return None

    return clean.lower() in ["yes", "on"]

#  not in used
async def set_greetings_clean(chat_id: int, greeting_type: str, clean: bool) -> bool:
    clean_value = "on" if clean else "off"
    result = await greetingsdb.update_one(
        {"chat_id": chat_id, "type": greeting_type}, {"$set": {"clean": clean_value}}, upsert=True
    )
    return result.modified_count > 0 or result.upserted_id is not None

# not in used

async def get_old_greetings_message(chat_id: int, greeting_type: str) -> int:
    return greeting_message[greeting_type].get(chat_id, None)

# not in used
async def set_old_greetings_message(chat_id: int, greeting_type: str, message_id: int):
    greeting_message[greeting_type][chat_id] = message_id
    return True

# in used
async def set_greetings_on(chat_id: int, type: str) -> bool:
    if type == "welcome":
        type = "welcome_on"
    elif type == "goodbye":
        type = "goodbye_on"
    
    existing = await greetingsdb.find_one({"chat_id": chat_id})
    
    if existing and existing.get(type) is True:
        return True
    
    result = await greetingsdb.update_one(
        {"chat_id": chat_id},
        {"$set": {type: True}},
        upsert=True
    )
    
    return result.modified_count > 0 or result.upserted_id is not None

# in used
async def is_greetings_on(chat_id: int, type: str) -> bool:
    if type == "welcome":
        type = "welcome_on"
    elif type == "goodbye":
        type = "goodbye_on"
    
    data = await greetingsdb.find_one({"chat_id": chat_id})
    if not data:
        return False

    greetings_on = data.get(type)
    return greetings_on if greetings_on is not None else False

# in used
async def set_greetings_off(chat_id: int, type: str) -> bool:
    if type == "welcome":
        type = "welcome_on"
    elif type == "goodbye":
        type = "goodbye_on"

    result = await greetingsdb.update_one(
        {"chat_id": chat_id},
        {"$set": {type: False}},
        upsert=True
    )
    return result.modified_count > 0 or result.upserted_id is not None
