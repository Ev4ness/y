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
from DanteMusic import app
from DanteMusic.misc import SUDOERS
from .notes import extract_urls
from DanteMusic.utils.database import is_gbanned_user
from utils import (
    del_goodbye,
    get_goodbye,
    set_goodbye,
    is_greetings_on,
    set_greetings_on,
    set_greetings_off,
)
from utils.error import capture_err
from DanteMusic.utils.functions import check_format, extract_text_and_keyb
from DanteMusic.utils.keyboard import ikb
from DanteMusic.utils.permissions import adminsOnly


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


async def send_left_message(chat: Chat, user_id: int, delete: bool = False, nothing: bool = False):
    ison = await is_greetings_on(chat.id, "goodbye")
    
    if ison is None and not nothing:
        await set_greetings_on(chat.id, "goodbye")
        goodbye = "Animation"
        raw_text = "hii {NAME}  welcome to the {GROUPNAME}\nif you have any problem or questions you can ask here"
        file_id = "CAACAgUAAx0Cfld0gAABAn25ZotwgWb3w8bg9vzHO23Ek3Ho6koAAs8KAALTvLlVK98vc1SalTUeBA"
        return await set_goodbye(chat.id, goodbye, raw_text, file_id)

    if not ison and not nothing:
        return

    goodbye, raw_text, file_id = await get_goodbye(chat.id)

    if not raw_text:
        return
    
    text = raw_text
    keyb = None
    
    if findall(r"\[.+\,.+\]", raw_text):
        text, keyb = extract_text_and_keyb(ikb, raw_text)
    
    u = await app.get_users(user_id)
    
    replacements = {
        "{GROUPNAME}": chat.title,
        "{NAME}": u.mention,
        "{ID}": f"`{user_id}`",
        "{FIRSTNAME}": u.first_name,
        "{SURNAME}": u.last_name or "None",
        "{USERNAME}": u.username or "None",
        "{DATE}": datetime.datetime.now().strftime("%Y-%m-%d"),
        "{WEEKDAY}": datetime.datetime.now().strftime("%A"),
        "{TIME}": datetime.datetime.now().strftime("%H:%M:%S") + " UTC"
    }
    
    for placeholder, value in replacements.items():
        if placeholder in text:
            text = text.replace(placeholder, value)
    
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
async def goodbye(client, message: Message):
    command = message.text.split()
    
    if len(command) == 1:
        return await get_goodbye_func(client, message)
    
    if len(command) == 2:
        action = command[1].lower()
        if action in ["on", "enable", "y", "yes", "true", "t"]:
            success = await set_greetings_on(message.chat.id, "goodbye")
            if success:
                await message.reply_text("I'll be saying goodbye to any leavers from now on!")
            else:
                await message.reply_text("Failed to enable goodbye messages.")
        
        elif action in ["off", "disable", "n", "no", "false", "f"]:
            success = await set_greetings_off(message.chat.id, "goodbye")
            if success:
                await message.reply_text("I'll stay quiet when people leave.")
            else:
                await message.reply_text("Failed to disable goodbye messages.")
        
        else:
            await message.reply_text(
                "Invalid command. Please use:\n"
                "/goodbye - To get your goodbye message\n"
                "/goodbye [on, y, true, enable, t] - to turn on goodbye messages\n"
                "/goodbye [off, n, false, disable, f, no] - to turn off goodbye messages"
            )
    else:
        await message.reply_text(
            "Invalid command. Please use:\n"
            "/goodbye - To get your goodbye message\n"
            "/goodbye [on, y, true, enable, t] - to turn on goodbye messages\n"
            "/goodbye [off, n, false, disable, f, no] - to turn off goodbye messages"
        )
 

async def get_goodbye_func(_, message):
    chat = message.chat
    goodbye, raw_text, file_id = await get_goodbye(chat.id)
    if not raw_text:
        return await message.reply_text("No Goodbye message set.")
    if not message.from_user:
        return await message.reply_text("You're anon, can't send goodbye message.")

    await send_left_message(chat, message.from_user.id, nothing=True)
    isgrt = await is_greetings_on(chat.id, "goodbye")
    if isgrt is None:
        text = "False"
    if isgrt:
        text = "True"
    await message.reply_text(
        f'I am currently saying goodbye to users :- {text}\ngoodbye: {goodbye}\n\nFile_id: `{file_id}`\n\n`{raw_text.replace("`", "")}`'
    )
