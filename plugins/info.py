import os

from pyrogram import enums, filters
from pyrogram.types import Message

from DanteMusic import app
from DanteMusic.misc import SUDOERS
from DanteMusic.utils.database import is_gbanned_user
from DanteMusic.utils.sections import section


async def userstatus(user_id):
    try:
        user = await app.get_users(user_id)
        x = user.status
        if x == enums.UserStatus.RECENTLY:
            return "Recently."
        elif x == enums.UserStatus.LAST_WEEK:
            return "Last week."
        elif x == enums.UserStatus.LONG_AGO:
            return "Long time ago."
        elif x == enums.UserStatus.OFFLINE:
            return "Offline."
        elif x == enums.UserStatus.ONLINE:
            return "Online."
    except:
        return "**something wrong happened !**"


async def get_user_info(user, already=False):
    if not already:
        user = await app.get_users(user)
    if not user.first_name:
        return ["Deleted account", None]
    user_id = user.id
    online = await userstatus(user_id)
    username = user.username
    first_name = user.first_name
    mention = user.mention("Link")
    dc_id = user.dc_id
    photo_id = user.photo.big_file_id if user.photo else None
    is_gbanned = await is_gbanned_user(user_id)
    is_sudo = user_id in SUDOERS
    is_premium = user.is_premium
    body = {
        "name": [first_name],
        "username": [("@" + username) if username else "Null"],
        "id": user_id,
        "dc id": dc_id,
        "mention": [mention],
        "preimium": is_premium,
        "last seen" : online,
    }
    caption = section("user info", body)
    return [caption, photo_id]


async def get_chat_info(chat):
    chat = await app.get_chat(chat)
    username = chat.username
    link = f"[Link](t.me/{username})" if username else "Null"
    photo_id = chat.photo.big_file_id if chat.photo else None
    info = f"""
    
    chat info 

chat id {chat.id}
name {chat.title}
username {chat.username}
dc id {chat.dc_id}
description {chat.description}
chattype {chat.type}
is verified {chat.is_verified}
is restricted {chat.is_restricted}
is creator {chat.is_creator}
is scam {chat.is_scam}
is fake {chat.is_fake}
member's count {chat.members_count}
link {link}

"""

    return info, photo_id


@app.on_message(filters.command("info"))
async def info_func(_, message: Message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user.id
    elif not message.reply_to_message and len(message.command) == 1:
        user = message.from_user.id
    elif not message.reply_to_message and len(message.command) != 1:
        user_input = message.text.split(None, 1)[1]
        if user_input.isdigit():
            user = int(user_input)
        elif user_input.startswith('@'):
            user = user_input
        else:
            return await message.reply_text("please provide a user's user id or username or reply to a user to get info")

    m = await message.reply_text("processing...")

    try:
        info_caption, photo_id = await get_user_info(user)
    except Exception as e:
        return await m.edit(str(e))

    if not photo_id:
        return await m.edit(info_caption, disable_web_page_preview=True)
    photo = await app.download_media(photo_id)

    await message.reply_photo(photo, caption=info_caption, quote=False)
    await m.delete()
    os.remove(photo)


@app.on_message(filters.command("chatinfo"))
async def chat_info_func(_, message: Message):
    splited = message.text.split()
    if len(splited) == 1:
        chat = message.chat.id
        if chat == message.from_user.id:
            return await message.reply_text("**Usage:**/chat_info [USERNAME|ID]")
    else:
        chat = splited[1]
    try:
        m = await message.reply_text("Processing")

        info_caption, photo_id = await get_chat_info(chat)
        if not photo_id:
            return await m.edit(info_caption, disable_web_page_preview=True)

        photo = await app.download_media(photo_id)
        await message.reply_photo(photo, caption=info_caption, quote=False)

        await m.delete()
        os.remove(photo)
    except Exception as e:
        await m.edit(e)


__MODULE__ = "Info"
__HELP__ = """<blockquote><b>
**user & chat information:**

• `/info`: Get information about the user. Username, ID, and more.
• `/chatinfo [username|id]`: Get information about the chat. member count, is verified, invite link, and more.
</b></blockquote>"""
