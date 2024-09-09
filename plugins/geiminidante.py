import asyncio
import aiohttp
from pymongo import MongoClient
from config import MONGO_DB_URI
from pyrogram import Client, filters

# MongoDB setup
DATABASE = MongoClient(MONGO_DB_URI)

db = DATABASE["MAIN"]["USERS"]

collection = db["members"]

# Function to add user to database
def add_user_database(user_id: int):
    """
    Add a user to the MongoDB collection if not already present.

    Parameters:
    - user_id (int): User ID to add to the database.

    Returns:
    - pymongo.collection.InsertOneResult or None: Result of the insertion operation.
    """
    check_user = collection.find_one({"user_id": user_id})
    if not check_user:
        return collection.insert_one({"user_id": user_id})

# Async function to chat with API
async def chat_with_api(model, prompt):
    """
    Fetch response from an external API asynchronously.

    Parameters:
    - model (str): Name of the model or endpoint.
    - prompt (str): Query or prompt to send to the API.

    Returns:
    - str: Response content from the API or an error message.
    """
    url = f"https://tofu-api.onrender.com/chat/{model}/{prompt}"
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    if data["code"] == 2:
                        return data["content"]
                    else:
                        return "ᴇʀʀᴏʀ: ᴜɴᴀʙʟᴇ ᴛᴏ ɢᴇᴛ ᴠᴀʟɪᴅ ʀᴇꜱᴘᴏɴꜱᴇ ꜰʀᴏᴍ ᴛʜᴇ ᴀᴘɪ"
                else:
                    return f"ᴇʀʀᴏʀ: ᴀᴘɪ ʀᴇᴛᴜʀɴᴇᴅ ꜱᴛᴀᴛᴜꜱ ᴄᴏᴅᴇ {response.status}"
        except aiohttp.ClientError as e:
            return f"ᴇʀʀᴏʀ: ᴜɴᴀʙʟᴇ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ᴛᴏ ᴛʜᴇ ᴀᴘɪ - {str(e)}"

from DanteMusic import app

@app.on_message(filters.command("geminisearch", ["/"]))
async def gptAi(client, message):
    split_text = message.text.split(None, 1)
    if len(split_text) < 2:
        await message.reply_text(f"/geminisearch {text}")
    else:
        response = await chat_with_api("gemini", split_text[1])
        await message.reply_text(response)
