import asyncio
import aiohttp
import os
from aiofiles import open as aio_open
from pyrogram import Client
from pyrogram.types import InputMediaPhoto
from bing_image_urls import bing_image_urls
from config import BANNED_USERS
from YukkiMusic import app
from pyrogram import filters
from pyrogram.types import InputMediaPhoto
from pyrogram.errors.exceptions.flood_420 import FloodWait

async def send_photos(send_photos, photo_urls):
    download_folder="downloads"
    photo_paths = []
    photo_cnt = 0
    messagesend = await message.reply_text("**🔍**")
    async with aiohttp.ClientSession() as session:
        for idx, url in enumerate(photo_urls):
            async with session.get(url) as response:
                if response.status == 200:
                    photo_path = os.path.join(download_folder, f"photo{idx + 1}.jpg")
                    async with aio_open(photo_path, 'wb') as f:
                        await f.write(await response.read())
                    photo_paths.append(photo_path)
                    try:
                        await messagesend.edit(f"**ғᴏᴜɴᴅ {photo_cnt} ɪᴍᴀɢᴇs**")
                    except FloodWait as e:
                        asyncio.sleep(e.value)
                    photo_cnt+=1
    await messagesend.edit(f"**ғᴏᴜɴᴅ {photo_cnt} ɪᴍᴀɢᴇs\nɴᴏᴡ ᴜᴘʟᴏᴀᴅɪɴɢ...**")
    media = [InputMediaPhoto(photo_path) for photo_path in photo_paths]
    try:
        await app.send_media_group(message.chat.id, media)
        await messagesend.delete()
    except Exception as e:
        await messagesend.edit(e)
        pass
    for photo_path in photo_paths:
        try:
            os.remove(photo_path)
        except OSError as e:
            print(f"Error: {photo_path} : {e.strerror}")
        except Exception:
            pass

@app.on_message(
    filters.command(["image"], prefixes=["/", "!", "."]) & ~BANNED_USERS
)
async def image_from_bing(_, message):
    chat_id = message.chat.id
    if len(message.command) < 2 and not message.reply_to_message:
        return await message.reply_text("**ɢɪᴠᴇ ɪᴍᴀɢᴇ ɴᴀᴍᴇ ғᴏʀ sᴇᴀʀᴄʜ 🔍**")

    if message.reply_to_message and message.reply_to_message.text:
        query = message.reply_to_message.text
    else:
        query = " ".join(message.command[1:])


    await send_photos(message, bing_image_urls(query, limit=9))


__MODULE__ = "Iᴍᴀɢᴇ"
__HELP__ = """
/image [ǫᴜᴇʀʏ] - ᴛᴏ ɢᴇᴛ ᴛᴏᴘ ɪᴍᴀɢᴇs ғʀᴏᴍ ʙɪɴɢ
/wall | /wallpaper - [ǫᴜᴇʀʏ] - ᴛᴏ ɢᴇᴛ ʀᴇǫᴜᴇsᴛᴇᴅ ᴡᴀʟᴘᴀᴘᴇʀ
/cat - ɢᴇᴛ ʀᴀɴᴅᴏᴍ ᴄᴀᴛ ɪᴍᴀɢᴇs
/dog - ɢᴇᴛ ʀᴀɴᴅᴏᴍ ᴅᴏɢ ɪᴍᴀɢᴇs
"""