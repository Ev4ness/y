import re
import datetime
from pyrogram import filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from typing import Dict, List, Union
from DanteMusic import app
from DanteMusic.core.mongo import mongodb
from utils.error import capture_err
from DanteMusic.utils.permissions import adminsOnly, member_permissions
from DanteMusic.utils.keyboard import ikb
from .notes import extract_urls
from DanteMusic.utils.functions import (
    check_format,
    extract_text_and_keyb,
    get_data_and_name,
)
from DanteMusic.utils.database import (
    delete_filter,
    deleteall_filters,
    get_filter,
    get_filters_names,
    save_filter,
)

from config import BANNED_USERS


__MODULE__ = "Filters"
__HELP__ = """<blockquote><b>/filters To Get All The Filters In The Chat.
/filter [FILTER_NAME] To Save A Filter(reply to a message).

Supported filter types are Text, Animation, Photo, Document, Video, video notes, Audio, Voice.

To use more words in a filter use.
`/filter Hey_there` To filter "Hey there".

/stop [FILTER_NAME] To Stop A Filter.
/stopall To delete all the filters in a chat (permanently).

You can use markdown or html to save text too.

Checkout /markdownhelp to know more about formattings and other syntax.
</b></blockquote>"""
@app.on_message(filters.command("filter") & ~filters.private & ~BANNED_USERS)
@adminsOnly("can_change_info")
async def save_filters(_, message):
    try:
        if len(message.command) < 2:
            return await message.reply_text(
                "**usasge:**\nreply to a message with  /filter [FILTER_NAME] [CONTENT] to set a new filter."
            )
        replied_message = message.reply_to_message
        if not replied_message:
            replied_message = message
        data, name = await get_data_and_name(replied_message, message)
        if len(name) < 2:
            return await message.reply_text(f"to filter the {name} must be greater then 𝟸 words")
        if data == "error":
            return await message.reply_text(
                "**usasge:**\n__/filter [FILTER_NAME] [CONTENT]__\n`-----------OR-----------`\nreply to a message with. \n/filter [FILTER_NAME]."
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
                    "**wrong formatting, check the help section.**"
                )
        name = name.replace("_", " ")
        _filter = {
            "type": _type,
            "data": data,
            "file_id": file_id,
        }
        
        chat_id = message.chat.id
        await save_filter(chat_id, name, _filter)
        return await message.reply_text(f"__**saved filter {name}.**__")
    except UnboundLocalError:
        return await message.reply_text(
            "**replied message is inacessable.\n`forward the message and try again.`**"
        )


@app.on_message(filters.command("filters") & ~filters.private & ~BANNED_USERS)
@capture_err
async def get_filterss(_, message):
    _filters = await get_filters_names(message.chat.id)
    if not _filters:
        return await message.reply_text("**no filters in the chat.**")
    _filters.sort()
    msg = f"list of filters in the **{message.chat.title}** :\n"
    for _filter in _filters:
        msg += f"**-** `{_filter}`\n"
    await message.reply_text(msg)

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
        await message.reply_text("**no filters in this chat.**")
    else:
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "yes, do it", callback_data="stop_yes"
                    ),
                    InlineKeyboardButton("no, don't do it", callback_data="stop_no"),
                ]
            ]
        )
        await message.reply_text(
            "**are you sure you want to delete all the filters in this chat forever ?.**",
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
            f"you don't have the recquried permission.\n permission: {permission}",
            show_alert=True,
        )
    input = cb.data.split("_", 1)[1]
    if input == "yes":
        stoped_all = await deleteall_filters(chat_id)
        if stoped_all:
            return await cb.message.edit(
                "**sucessfully deleded all filter's on this chat.**"
            )
    if input == "no":
        await cb.message.reply_to_message.delete()
        await cb.message.delete()
