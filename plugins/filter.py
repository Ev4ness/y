import re
import datetime
from pyrogram import filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from typing import Dict, List, Union
from YukkiMusic import app
from YukkiMusic.core.mongo import mongodb
from utils.error import capture_err
from YukkiMusic.utils.permissions import adminsOnly, member_permissions
from YukkiMusic.utils.keyboard import ikb
from .notes import extract_urls
from YukkiMusic.utils.functions import (
    check_format,
    extract_text_and_keyb,
    get_data_and_name,
)
from config import BANNED_USERS

filtersdb = mongodb.filters

__MODULE__ = "Filters"
__HELP__ = """/filters To Get All The Filters In The Chat.
/filter [FILTER_NAME] To Save A Filter(reply to a message).

Supported filter types are Text, Animation, Photo, Document, Video, video notes, Audio, Voice.

To use more words in a filter use.
`/filter Hey_there` To filter "Hey there".

/stop [FILTER_NAME] To Stop A Filter.
/stopall To delete all the filters in a chat (permanently).

You can use markdown or html to save text too.

Checkout /markdownhelp to know more about formattings and other syntax.
"""

async def get_filters_count() -> dict:
    chats_count = 0
    filters_count = 0
    async for chat in filtersdb.find({"chat_id": {"$lt": 0}}):
        filters_name = await get_filters_names(chat["chat_id"])
        filters_count += len(filters_name)
        chats_count += 1
    return {
        "chats_count": chats_count,
        "filters_count": filters_count,
    }


async def _get_filters(chat_id: int) -> Dict[str, int]:
    _filters = await filtersdb.find_one({"chat_id": chat_id})
    if not _filters:
        return {}
    return _filters["filters"]


async def get_filters_names(chat_id: int) -> List[str]:
    _filters = []
    for _filter in await _get_filters(chat_id):
        _filters.append(_filter)
    return _filters


async def get_filter(chat_id: int, name: str) -> Union[bool, dict]:
    name = name.lower().strip()
    _filters = await _get_filters(chat_id)
    if name in _filters:
        return _filters[name]
    return False


async def save_filter(chat_id: int, name: str, _filter: dict):
    name = name.lower().strip()
    _filters = await _get_filters(chat_id)
    _filters[name] = _filter
    await filtersdb.update_one(
        {"chat_id": chat_id},
        {"$set": {"filters": _filters}},
        upsert=True,
    )


async def delete_filter(chat_id: int, name: str) -> bool:
    filtersd = await _get_filters(chat_id)
    name = name.lower().strip()
    if name in filtersd:
        del filtersd[name]
        await filtersdb.update_one(
            {"chat_id": chat_id},
            {"$set": {"filters": filtersd}},
            upsert=True,
        )
        return True
    return False


async def deleteall_filters(chat_id: int):
    return await filtersdb.delete_one({"chat_id": chat_id})
    
    

@app.on_message(filters.command("filter") & ~filters.private & ~BANNED_USERS)
@adminsOnly("can_change_info")
async def save_filters(_, message):
    try:
        if len(message.command) < 2:
            return await message.reply_text(
                "**ᴜsᴀsɢᴇ:**\nʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴡɪᴛʜ  /filter [FILTER_NAME] [CONTENT] ᴛᴏ sᴇᴛ ᴀ ɴᴇᴡ ғɪʟᴛᴇʀ."
            )
        replied_message = message.reply_to_message
        if not replied_message:
            replied_message = message
        data, name = await get_data_and_name(replied_message, message)
        if data == "error":
            return await message.reply_text(
                "**ᴜsᴀsɢᴇ:**\n__/filter [FILTER_NAME] [CONTENT]__\n`-----------OR-----------`\nʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴡɪᴛʜ. \n/filter [FILTER_NAME]."
            )
        if replied_message.text:
            _type = "text"
            file_id = None
        if replied_message.sticker:
            _type = "sticker"
            file_id = replied_message.sticker.file_id
        if replied_message.animation:
            _type = "animation"
            file_id = replied_message.animation.file_id
        if replied_message.photo:
            _type = "photo"
            file_id = replied_message.photo.file_id
        if replied_message.document:
            _type = "document"
            file_id = replied_message.document.file_id
        if replied_message.video:
            _type = "video"
            file_id = replied_message.video.file_id
        if replied_message.video_note:
            _type = "video_note"
            file_id = replied_message.video_note.file_id
        if replied_message.audio:
            _type = "audio"
            file_id = replied_message.audio.file_id
        if replied_message.voice:
            _type = "voice"
            file_id = replied_message.voice.file_id
        if replied_message.reply_markup and not re.findall(r"\[.+\,.+\]", data):
            urls = extract_urls(replied_message.reply_markup)
            if urls:
                response = "\n".join(
                    [f"{name}=[{text}, {url}]" for name, text, url in urls]
                )
                data = data + response
        if data:
            data = await check_format(ikb, data)
            if not data:
                return await message.reply_text(
                    "**ᴡʀᴏɴɢ ғᴏʀᴍᴀᴛᴛɪɴɢ, ᴄʜᴇᴄᴋ ᴛʜᴇ ʜᴇʟᴘ sᴇᴄᴛɪᴏɴ.**"
                )
        name = name.replace("_", " ")
        _filter = {
            "type": _type,
            "data": data,
            "file_id": file_id,
        }
        
        chat_id = message.chat.id
        await save_filter(chat_id, name, _filter)
        return await message.reply_text(f"__**sᴀᴠᴇᴅ ғɪʟᴛᴇʀ {name}.**__")
    except UnboundLocalError:
        return await message.reply_text(
            "**ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ ɪs ɪɴᴀᴄᴇssᴀʙʟᴇ.\n`ғᴏʀᴡᴀʀᴅ ᴛʜᴇ ᴍᴇssᴀɢᴇ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ.`**"
        )


@app.on_message(filters.command("filters") & ~filters.private & ~BANNED_USERS)
@capture_err
async def get_filterss(_, message):
    _filters = await get_filters_names(message.chat.id)
    if not _filters:
        return await message.reply_text("**ɴᴏ ғɪʟᴛᴇʀs ɪɴ ᴛʜᴇ ᴄʜᴀᴛ.**")
    _filters.sort()
    msg = f"ʟɪsᴛ ᴏғ ғɪʟᴛᴇʀs ɪɴ ᴛʜᴇ **{message.chat.title}** :\n"
    for _filter in _filters:
        msg += f"**-** `{_filter}`\n"
    await message.reply_text(msg)


@app.on_message(filters.command("stop") & ~filters.private & ~BANNED_USERS)
@adminsOnly("can_change_info")
async def del_filter(_, message):
    if len(message.command) < 2:
        return await message.reply_text("**ᴜsᴀsɢᴇ:**\n__/stop [FILTER_NAME]__")
    name = message.text.split(None, 1)[1].strip()
    if not name:
        return await message.reply_text("**ᴜsᴀsɢᴇ:**\n__/stop [FILTER_NAME]__")
    chat_id = message.chat.id
    deleted = await delete_filter(chat_id, name)
    if deleted:
        await message.reply_text(f"**ᴅᴇʟᴇᴛᴇᴅ ғɪʟᴛᴇʀ {name}.**")
    else:
        await message.reply_text("**ɴᴏ sᴜᴄʜ ғɪʟᴛᴇʀ.**")


@app.on_message(
    filters.text & ~filters.private & ~filters.channel & ~filters.via_bot & ~filters.forwarded & ~BANNED_USERS, group=1)
@capture_err
async def filters_re(_, message):
    from_user = message.from_user if message.from_user else message.sender_chat
    user_id = from_user.id
    chat_id = message.chat.id
    text = message.text.lower().strip()
    if not text:
        return
    chat_id = message.chat.id
    list_of_filters = await get_filters_names(chat_id)
    for word in list_of_filters:
        pattern = r"( |^|[^\w])" + re.escape(word) + r"( |$|[^\w])"
        if re.search(pattern, text, flags=re.IGNORECASE):
            _filter = await get_filter(chat_id, word)
            data_type = _filter["type"]
            data = _filter["data"]
            file_id = _filter.get("file_id")
            keyb = None
            if data:
                if "{app.mention}" in data:
                    data = data.replace("{app.mention}", app.mention)
                if "{GROUPNAME}" in data:
                    data = data.replace("{GROUPNAME}", message.chat.title)
                if "{NAME}" in data:
                    data = data.replace("{NAME}", message.from_user.mention)
                if "{ID}" in data:
                    data = data.replace("{ID}", f"`message.from_user.id`")
                if "{FIRSTNAME}" in data:
                    data = data.replace("{FIRSTNAME}", message.from_user.first_name)
                if "{SURNAME}" in data:
                    sname = message.from_user.last_name or "None"
                    data = data.replace("{SURNAME}", sname)
                if "{USERNAME}" in data:
                    susername = message.from_user.username or "None"
                    data = data.replace("{USERNAME}", susername)
                if "{DATE}" in data:
                    DATE = datetime.datetime.now().strftime("%Y-%m-%d")        
                    data = data.replace("{DATE}", DATE)
                if "{WEEKDAY}" in data:
                    WEEKDAY = datetime.datetime.now().strftime("%A")
                    data = data.replace("{WEEKDAY}", WEEKDAY)
                if "{TIME}" in data:
                    TIME = datetime.datetime.now().strftime("%H:%M:%S")
                    data = data.replace("{TIME}", f"{TIME} UTC")

                if re.findall(r"\[.+\,.+\]", data):
                    keyboard = extract_text_and_keyb(ikb, data)
                    if keyboard:
                        data, keyb = keyboard
            replied_message = message.reply_to_message
            if replied_message:
                replied_user = replied_message.from_user if replied_message.from_user else replied_message.sender_chat
                if text.startswith("~"):
                    await message.delete()
                if replied_user.id != from_user.id:
                    message = replied_message

            if data_type == "text":
                await message.reply_text(
                    text=data,
                    reply_markup=keyb,
                    disable_web_page_preview=True,
                )
            else:
                if not file_id:
                    continue
            if data_type == "sticker":
                await message.reply_sticker(
                    sticker=file_id,
                )
            if data_type == "animation":
                await message.reply_animation(
                    animation=file_id,
                    caption=data,
                    reply_markup=keyb,
                )
            if data_type == "photo":
                await message.reply_photo(
                    photo=file_id,
                    caption=data,
                    reply_markup=keyb,
                )
            if data_type == "document":
                await message.reply_document(
                    document=file_id,
                    caption=data,
                    reply_markup=keyb,
                )
            if data_type == "video":
                await message.reply_video(
                    video=file_id,
                    caption=data,
                    reply_markup=keyb,
                )
            if data_type == "video_note":
                await message.reply_video_note(
                    video_note=file_id,
                )
            if data_type == "audio":
                await message.reply_audio(
                    audio=file_id,
                    caption=data,
                    reply_markup=keyb,
                )
            if data_type == "voice":
                await message.reply_voice(
                    voice=file_id,
                    caption=data,
                    reply_markup=keyb,
                )
            return  # NOTE: Avoid filter spam


@app.on_message(filters.command("stopall") & ~filters.private & ~BANNED_USERS)
@adminsOnly("can_change_info")
async def stop_all(_, message):
    _filters = await get_filters_names(message.chat.id)
    if not _filters:
        await message.reply_text("**ɴᴏ ғɪʟᴛᴇʀs ɪɴ ᴛʜɪs ᴄʜᴀᴛ.**")
    else:
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ʏᴇs, ᴅᴏ ɪᴛ", callback_data="stop_yes"
                    ),
                    InlineKeyboardButton("ɴᴏ, ᴅᴏɴ'ᴛ ᴅᴏ ɪᴛ", callback_data="stop_no"),
                ]
            ]
        )
        await message.reply_text(
            "**ᴀʀᴇ ʏᴏᴜ sᴜʀᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ᴛʜᴇ ғɪʟᴛᴇʀs ɪɴ ᴛʜɪs ᴄʜᴀᴛ ғᴏʀᴇᴠᴇʀ ?.**",
            reply_markup=keyboard,
        )


@app.on_callback_query(filters.regex("stop_(.*)") & ~BANNED_USERS)
async def stop_all_cb(_, cb):
    chat_id = cb.message.chat.id
    from_user = cb.from_user
    permissions = await member_permissions(chat_id, from_user.id)
    permission = "can_change_info"
    if permission not in permissions:
        return await cb.answer(
            f"ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ʀᴇᴄǫᴜʀɪᴇᴅ ᴘᴇʀᴍɪssɪᴏɴ.\n ᴘᴇʀᴍɪssɪᴏɴ: {permission}",
            show_alert=True,
        )
    input = cb.data.split("_", 1)[1]
    if input == "yes":
        stoped_all = await deleteall_filters(chat_id)
        if stoped_all:
            return await cb.message.edit(
                "**sᴜᴄᴇssғᴜʟʟʏ ᴅᴇʟᴇᴅᴇᴅ ᴀʟʟ ғɪʟᴛᴇʀ's ᴏɴ ᴛʜɪs ᴄʜᴀᴛ.**"
            )
    if input == "no":
        await cb.message.reply_to_message.delete()
        await cb.message.delete()