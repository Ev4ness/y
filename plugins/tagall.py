import asyncio
from pyrogram import filters
from pyrogram.enums import ChatMembersFilter
from pyrogram.errors import FloodWait

from DanteMusic import app
from DanteMusic.utils.database import get_assistant
from DanteMusic.utils.filter import admin_filter

SPAM_CHATS = []


@app.on_message(
    filters.command(["all", "allmention", "mentionall", "tagall"], prefixes=["/", "@"])
    & admin_filter
)
async def tag_all_users(_, message):
    if message.chat.id in SPAM_CHATS:
        return await message.reply_text(
            "tagging process is already running if you want to stop so use /cancel"
        )
    replied = message.reply_to_message
    if len(message.command) < 2 and not replied:
        await message.reply_text(
            "** give some text to tag all, like »** `@all Hi Friends`"
        )
        return
    if replied:
        usernum = 0
        usertxt = ""
        try:
            SPAM_CHATS.append(message.chat.id)
            async for m in app.get_chat_members(message.chat.id):
                if message.chat.id not in SPAM_CHATS:
                    break
                if m.user.is_deleted or m.user.is_bot:
                    continue
                usernum += 1
                usertxt += f"[{m.user.first_name}](tg://user?id={m.user.id})  "
                if usernum == 14:
                    await app.send_message(
                        message.chat.id,
                        f"{replied.text}\n\n{usertxt}",
                        disable_web_page_preview=True,
                    )
                    await asyncio.sleep(1)
                    usernum = 0
                    usertxt = ""

            if usernum != 0:
                await app.send_message(
                    message.chat.id,
                    f"{replied.text}\n\n{usertxt}",
                    disable_web_page_preview=True,
                )
        except FloodWait as e:
            await asyncio.sleep(e.value)
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass
    else:
        try:
            usernum = 0
            usertxt = ""
            text = message.text.split(None, 1)[1]
            SPAM_CHATS.append(message.chat.id)
            async for m in app.get_chat_members(message.chat.id):
                if message.chat.id not in SPAM_CHATS:
                    break
                if m.user.is_deleted or m.user.is_bot:
                    continue
                usernum += 1
                usertxt += f"[{m.user.first_name}](tg://user?id={m.user.id})  "
                if usernum == 14:
                    await app.send_message(
                        message.chat.id,
                        f"{text}\n{usertxt}",
                        disable_web_page_preview=True,
                    )
                    await asyncio.sleep(2)
                    usernum = 0
                    usertxt = ""
            if usernum != 0:
                await app.send_message(
                    message.chat.id,
                    f"{text}\n\n{usertxt}",
                    disable_web_page_preview=True,
                )
        except FloodWait as e:
            await asyncio.sleep(e.value)
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass


async def tag_all_admins(_, message):
    if message.chat.id in SPAM_CHATS:
        return await message.reply_text(
            "tagging process is already running if you want to stop so use /cancel"
        )
    replied = message.reply_to_message
    if len(message.command) < 2 and not replied:
        await message.reply_text(
            "** give some text to tag all, like »** `@admins Hi Friends`"
        )
        return
    if replied:
        usernum = 0
        usertxt = ""
        try:
            SPAM_CHATS.append(message.chat.id)
            async for m in app.get_chat_members(
                message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS
            ):
                if message.chat.id not in SPAM_CHATS:
                    break
                if m.user.is_deleted or m.user.is_bot:
                    continue
                usernum += 1
                usertxt += f"[{m.user.first_name}](tg://user?id={m.user.id})  "
                if usernum == 14:
                    await app.send_message(
                        message.chat.id,
                        f"{replied.text}\n\n {usertxt}",
                        disable_web_page_preview=True,
                    )
                    await asyncio.sleep(1)
                    usernum = 0
                    usertxt = ""
            if usernum != 0:
                await app.send_message(
                    message.chat.id,
                    f"{replied.text}\n\n{usertxt}",
                    disable_web_page_preview=True,
                )
        except FloodWait as e:
            await asyncio.sleep(e.value)
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass
    else:
        usernum = 0
        usertxt = ""
        try:
            text = message.text.split(None, 1)[1]
            SPAM_CHATS.append(message.chat.id)
            async for m in app.get_chat_members(
                message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS
            ):
                if message.chat.id not in SPAM_CHATS:
                    break
                if m.user.is_deleted or m.user.is_bot:
                    continue
                usernum += 1
                usertxt += f"[{m.user.first_name}](tg://user?id={m.user.id})  "
                if usernum == 14:
                    await app.send_message(
                        message.chat.id,
                        f"{text}\n{usertxt}",
                        disable_web_page_preview=True,
                    )
                    await asyncio.sleep(2)
                    usernum = 0
                    usertxt = ""
            if usernum != 0:
                await app.send_message(
                    message.chat.id,
                    f"{text}\n\n{usertxt}",
                    disable_web_page_preview=True,
                )
        except FloodWait as e:
            await asyncio.sleep(e.value)
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass

@app.on_message(
    filters.command(["admin", "admins","report"], prefixes=["/", "@"]) & filters.group
)
async def admintag_with_reporting(client, message):
    if not message.from_user:
        return
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    admins = [
        admin.user.id
        async for admin in client.get_chat_members(
            chat_id, filter=ChatMembersFilter.ADMINISTRATORS
        )
    ]
    if message.command[0] == "report":
        if from_user_id in admins:
            return await message.reply_text("opps! you are looks like an admin!\nyou can't report any users to admin")

    if from_user_id in admins:
        return await tag_all_admins(client, message)

    if len(message.text.split()) <= 1 and not message.reply_to_message:
        return await message.reply_text("Reply to a message to report that user.")

    reply = message.reply_to_message or message
    reply_user_id = reply.from_user.id if reply.from_user else reply.sender_chat.id
    linked_chat = (await client.get_chat(chat_id)).linked_chat
    if reply_user_id == app.id:
        return await message.reply_text("Why would I report myself?")
    if (
        reply_user_id in admins
        or reply_user_id == chat_id
        or (linked_chat and reply_user_id == linked_chat.id)
    ):
        return await message.reply_text(
            "Do you know that the user you are replying to is an admin?"
        )

    user_mention = reply.from_user.mention if reply.from_user else "the user"
    text = f"Reported {user_mention} to admins!."

    for admin in admins:
        admin_member = await client.get_chat_member(chat_id, admin)
        if not admin_member.user.is_bot and not admin_member.user.is_deleted:
            text += f"[\u2063](tg://user?id={admin})"

    await reply.reply_text(text)


@app.on_message(
    filters.command(
        [
            "stopmention",
            "cancel",
            "cancelmention",
            "offmention",
            "mentionoff",
            "cancelall",
        ],
        prefixes=["/", "@"],
    )
    & admin_filter
)
async def cancelcmd(_, message):
    chat_id = message.chat.id
    if chat_id in SPAM_CHATS:
        try:
            SPAM_CHATS.remove(chat_id)
        except Exception:
            pass
        return await message.reply_text("**tagging process successfully stopped!**")

    else:
        await message.reply_text("**no process ongoing!**")
        return
__MODULE__ = "Tagall"
__HELP__ = """<blockquote><b>

@all or /all | /tagall or  @tagall | /mentionall or  @mentionall [text] or [reply to any message] to tag all user's in your group bt bot

/admins | @admins | /report [text] or [reply to any message] to tag all admin's in your group


/cancel Or @cancel |  /offmention Or @offmention | /mentionoff Or @mentionoff | /cancelall Or @cancelall - to stop running any tag process

**__Note__** This command can only use the Admins of Chat and make Sure Bot and assistant is an admin in your group's</b></blockquote>
"""
