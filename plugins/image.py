import os
import requests
from pyrogram.types import InputMediaPhoto
from bing_image_urls import bing_image_urls
from config import BANNED_USERS
from YukkiMusic import app
from pyrogram import filters
from pyrogram.errors.exceptions.flood_420 import FloodWait

def to_tiny_caps(text):
    return text.translate(str.maketrans("abcdefghijklmnopqrstuvwxyz", "ᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ"))

def download_photo(url, photo_path, retries=3):
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                with open(photo_path, 'wb') as f:
                    f.write(response.content)
                return photo_path
        except requests.exceptions.RequestException as e:
            print(f"Failed to connect to {url}: {e}")
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
            else:
                raise

async def send_photos(message, photo_urls):
    download_folder = "downloads" 
    photo_paths = []
    photo_cnt = 0
    messagesend = await message.reply_text("**🔍 sᴇᴀʀᴄʜɪɴɢ ғᴏʀ ɪᴍᴀɢᴇs...**")
    
    for idx, url in enumerate(photo_urls):
        photo_path = os.path.join(download_folder, f"ᴘʜᴏᴛᴏ{idx + 1}.jpg")
        try:
            download_photo(url, photo_path)
            photo_paths.append(photo_path)
            photo_cnt += 1
            try:
                await messagesend.edit(f"**ғᴏᴜɴᴅ {photo_cnt} ɪᴍᴀɢᴇs**")
            except FloodWait as e:
                pass
        except Exception as e:
            print(f"Failed to download image {idx + 1}: {e}")
    
    await messagesend.edit(f"**ғᴏᴜɴᴅ {photo_cnt} ɪᴍᴀɢᴇs\nɴᴏᴡ ᴜᴘʟᴏᴀᴅɪɴɢ...**")
    
    media = [InputMediaPhoto(photo_path) for photo_path in photo_paths]
    try:
        await app.send_media_group(message.chat.id, media)
        await messagesend.delete()
    except Exception as e:
        await messagesend.edit(f"Error: {e}")
    
    for photo_path in photo_paths:
        try:
            os.remove(photo_path)
        except OSError as e:
            print(f"Error removing file {photo_path}: {e.strerror}")
        except Exception:
            pass

# Command handler to search for images
@app.on_message(
    filters.command(["ɪᴍᴀɢᴇ"], prefixes=["/", "!", "."]) & ~BANNED_USERS
)
async def image_from_bing(_, message):
    if len(message.command) < 2 and not message.reply_to_message:
        return await message.reply_text("**ɢɪᴠᴇ ɪᴍᴀɢᴇ ɴᴀᴍᴇ ғᴏʀ sᴇᴀʀᴄʜ 🔍**")
    
    if message.reply_to_message and message.reply_to_message.text:
        query = message.reply_to_message.text
    else:
        query = " ".join(message.command[1:])
    
    await send_photos(message, bing_image_urls(query, limit=9))