import datetime
from re import findall

from pyrogram import filters
from pyrogram.enums import ChatMemberStatus as CMS
from pyrogram.errors.exceptions.bad_request_400 import ChatAdminRequired
from pyrogram.types import (
    Chat,
    ChatMemberUpdated,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from YukkiMusic import app
from YukkiMusic.misc import SUDOERS
from .notes import extract_urls
from YukkiMusic.utils.database import is_gbanned_user
from utils import (
    del_goodbye,
    get_goodbye,
    set_goodbye,
    is_greetings_on,
    set_greetings_on,
    set_greetings_off,
)
from utils.error import capture_err
from YukkiMusic.utils.functions import check_format, extract_text_and_keyb
from YukkiMusic.utils.keyboard import ikb
from YukkiMusic.utils.permissions import adminsOnly


async def handle_left_member(member, chat):

    try:
        if member.id in SUDOERS:
            return
        if await is_gbanned_user(member.id):
            await chat.ban_member(member.id)
            await app.send_message(
                chat.id,
                f"{member.mention} was globally banned, and got removed,"
                + " if you think this is a false gban, you can appeal"
                + " for this ban in support chat.",
            )
            return
        if member.is_bot:
            return
        return await send_left_message(chat, member.id)

    except ChatAdminRequired:
        return

@app.on_message(filters.left_chat_member & filters.group, group=6)
@capture_err
async def goodbye(_, m:Message):

    member = await app.get_users(m.from_user.id)
    chat = m.chat
    return await handle_left_member(member, chat)


async def send_left_message(chat: Chat, user_id: int, delete: bool = False):
    ison = await is_greetings_on(chat.id, "goodbye")
    if ison in None:
        await set_greetings_on(chat.id, "goodbye")
        goodbye = "Animation"
        raw_text= "ʜɪɪ {NAME}  ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ {GROUPNAME}\nɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴏʀ ǫᴜᴇsᴛɪᴏɴs ʏᴏᴜ ᴄᴀɴ ᴀsᴋ ʜᴇʀᴇ"
        file_id = "CgACAgIAAyEFAASFqsojAAIPgGZwFG2XMOMlaC9jgKZSvUtqYchzAALbEgACGtVYSAGHbztDEjlEHgQ"
        return await set_goodbye(chat.id, goodbye, raw_text, file_id)

    if not ison:
        return

    goodbye, raw_text, file_id = await get_goodbye(chat.id)

    if not raw_text:
        return
    text = raw_text
    keyb = None
    if findall(r"\[.+\,.+\]", raw_text):
        text, keyb = extract_text_and_keyb(ikb, raw_text)
    u = await app.get_users(user_id)
    if "{GROUPNAME}" in text:
        text = text.replace("{GROUPNAME}", chat.title)
    if "{NAME}" in text:
        text = text.replace("{NAME}", u.mention)
    if "{ID}" in text:
        text = text.replace("{ID}", f"`{user_id}`")
    if "{FIRSTNAME}" in text:
        text = text.replace("{FIRSTNAME}", u.first_name)
    if "{SURNAME}" in text:
        sname = u.last_name or "None"
        text = text.replace("{SURNAME}", sname)
    if "{USERNAME}" in text:
        susername = u.username or "None"
        text = text.replace("{USERNAME}", susername)
    if "{DATE}" in text:
        DATE = datetime.datetime.now().strftime("%Y-%m-%d")
        text = text.replace("{DATE}", DATE)
    if "{WEEKDAY}" in text:
        WEEKDAY = datetime.datetime.now().strftime("%A")
        text = text.replace("{WEEKDAY}", WEEKDAY)
    if "{TIME}" in text:
        TIME = datetime.datetime.now().strftime("%H:%M:%S")
        text = text.replace("{TIME}", f"{TIME} UTC")

    if goodbye == "Text":
        m = await app.send_message(
            chat.id,
            text=text,
            reply_markup=keyb,
            disable_web_page_preview=True,
        )
    elif goodbye == "Photo":
        m = await app.send_photo(
            chat.id,
            photo=file_id,
            caption=text,
            reply_markup=keyb,
        )
    else:
        m = await app.send_animation(
            chat.id,
            animation=file_id,
            caption=text,
            reply_markup=keyb,
        )


@app.on_message(filters.command("setgoodbye") & ~filters.private)
@adminsOnly("can_change_info")
async def set_goodbye_func(_, message):
    usage = "You need to reply to a text, gif or photo to set it as goodbye message.\n\nNotes: caption required for gif and photo."
    key = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="More Help",
                    url=f"t.me/{app.username}?start=greetings",
                )
            ],
        ]
    )
    replied_message = message.reply_to_message
    chat_id = message.chat.id
    try:
        if not replied_message:
            await message.reply_text(usage, reply_markup=key)
            return
        if replied_message.animation:
            goodbye = "Animation"
            file_id = replied_message.animation.file_id
            text = replied_message.caption
            if not text:
                return await message.reply_text(usage, reply_markup=key)
            raw_text = text.markdown
        if replied_message.photo:
            goodbye = "Photo"
            file_id = replied_message.photo.file_id
            text = replied_message.caption
            if not text:
                return await message.reply_text(usage, reply_markup=key)
            raw_text = text.markdown
        if replied_message.text:
            goodbye = "Text"
            file_id = None
            text = replied_message.text
            raw_text = text.markdown
        if replied_message.reply_markup and not findall(r"\[.+\,.+\]", raw_text):
            urls = extract_urls(replied_message.reply_markup)
            if urls:
                response = "\n".join(
                    [f"{name}=[{text}, {url}]" for name, text, url in urls]
                )
                raw_text = raw_text + response
        raw_text = await check_format(ikb, raw_text)
        if raw_text:
            await set_goodbye(chat_id, goodbye, raw_text, file_id)
            return await message.reply_text(
                "goodbye message has been successfully set."
            )
        else:
            return await message.reply_text(
                "Wrong formatting, check the help section.\n\n**Usage:**\nText: `Text`\nText + Buttons: `Text ~ Buttons`",
                reply_markup=key,
            )
    except UnboundLocalError:
        return await message.reply_text(
            "**Only Text, Gif and Photo welcome message are supported.**"
        )


@app.on_message(filters.command(["delgoodbye", "deletegoodbye"]) & ~filters.private)
@adminsOnly("can_change_info")
async def del_goodbye_func(_, message):
    chat_id = message.chat.id
    await del_goodbye(chat_id)
    await message.reply_text("goodbye message has been deleted.")


@app.on_message(filters.command("goodbye") & ~filters.private)
@adminsOnly("can_change_info")
async def welcome_command(client, message):
    command = message.text.split()
    if len(command) == 1:
        return await get_goodbye_func(client, message)

    elif len(command) == 2 and command[1].lower() in ["on", "enable", "y", "yes", "true", "t"]:
        success = await is_greetings_on(message.chat.id, "goodbye")
        if success:
            await message.reply_text("I'll be welcoming all new members from now on!")


    elif len(command) == 2 and command[1].lower() in ["off", "disable", "n", "no"]:
        success = await set_greetings_off(message.chat.id, "goodbye")
        if success:
            await message.reply_text("I'll stay quiet when new members join.")
    else:
        await message.reply_text("\n/welcome - To get You welcome message\n/welcome [on , y, true, enable, t] - to turn on welcome\n\n/welcome [off , n, false, disable, f, no] - to turn on welcome)


async def get_goodbye_func(_, message):
    chat = message.chat
    goodbye, raw_text, file_id = await get_goodbye(chat.id)
    if not raw_text:
        return await message.reply_text("No Goodbye message set.")
    if not message.from_user:
        return await message.reply_text("You're anon, can't send goodbye message.")

    await send_left_message(chat, message.from_user.id)

    await message.reply_text(
        f'goodbye: {goodbye}\n\nFile_id: `{file_id}`\n\n`{raw_text.replace("`", "")}`'
    )