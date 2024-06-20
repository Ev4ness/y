import random

import requests
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from YukkiMusic import app


@app.on_message(filters.command(["wall", "wallpaper"]))
async def wall(_, message: Message):

    try:
        text = message.text.split(None, 1)[1]
    except IndexError:
        text = None
    if not text:
        return await message.reply_text("`Please give some query to search.`")
    m = await message.reply_text("sᴇᴀʀᴄʜɪɴɢ...")
    try:
        url = requests.get(f"https://api.safone.dev/wall?query={text}").json()[
            "results"
        ]
        ran = random.randint(0, 7)
        await message.reply_photo(
            photo=url[ran]["imageUrl"],
            caption=f"ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ : {message.from_user.mention}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("ʟɪɴᴋ", url=url[ran]["imageUrl"])],
                ]
            ),
        )
        await m.delete()
    except Exception as e:
        await m.edit_text(
            f"`ᴡᴀʟʟᴘᴀᴘᴇʀ ɴᴏᴛ ғᴏᴜɴᴅ ғᴏʀ : `{text}`",
        )

__MODULE__ = "Wall"
__HELP__ = """
**COMMANDS:**

• /WALL - **ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴᴅ sᴇɴᴅ ᴡᴀʟʟᴘᴀᴘᴇʀ.**

**INFO:**

- ᴛʜɪs ʙᴏᴛ ᴘʀᴏᴠɪᴅᴇs ᴀ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴᴅ sᴇɴᴅ ᴡᴀʟʟᴘᴀᴘᴇʀ.
- ᴜsᴇ /WALL ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜ ᴀ ᴛᴇxᴛ ᴛᴏ sᴇᴀʀᴄʜ ғᴏʀ ᴡᴀʟʟᴘᴀᴘᴇʀ ᴀɴᴅ sᴇɴᴅ ɪᴛ ᴛᴏ ᴛʜᴇ ᴄʜᴀᴛ.

**NOTE:**

- ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴᴅ sᴇɴᴅ ᴡᴀʟʟᴘᴀᴘᴇʀ.
"""