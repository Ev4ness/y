import asyncio

from pyrogram import filters
from pyrogram.enums import ChatMembersFilter
from pyrogram.errors import FloodWait

from YukkiMusic import app
from YukkiMusic.utils.database import get_assistant
from YukkiMusic.utils.filter import admin_filter

SPAM_CHATS = []


@app.on_message(
    filters.command(["all", "allmention", "mentionall", "tagall"], prefixes=["/", "@"])
    & admin_filter
)
async def tag_all_users(_, message):
    if message.chat.id in SPAM_CHATS:
        return await message.reply_text(
            "ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss ɪs ᴀʟʀᴇᴀᴅʏ ʀᴜɴɴɪɴɢ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴛᴏᴘ sᴏ ᴜsᴇ /cancel"
        )
    replied = message.reply_to_message
    if len(message.command) < 2 and not replied:
        await message.reply_text(
            "** ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴛᴀɢ ᴀʟʟ, ʟɪᴋᴇ »** `@all Hi Friends`"
        )
        return
    if replied:
        try:
            SPAM_CHATS.append(message.chat.id)
            usernum = 0
            usertxt = ""
            async for m in app.get_chat_members(message.chat.id):
                if message.chat.id not in SPAM_CHATS:
                    break
                usernum += 1
                usertxt += f"[{m.user.first_name}](tg://user?id={m.user.id})"
                if usernum == 14:
                    await app.send_message(
                        message.chat.id,
                        f"{replied.text}\n\n{usertxt}",
                        disable_web_page_preview=True,
                    )
                    await asyncio.sleep(1)
                    usernum = 0
                    usertxt = ""

        except FloodWait as e:
            await asyncio.sleep(e.value)
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass
    else:
        try:
            text = message.text.split(None, 1)[1]
            SPAM_CHATS.append(message.chat.id)
            usernum = 0
            usertxt = ""
            async for m in app.get_chat_members(message.chat.id):
                if message.chat.id not in SPAM_CHATS:
                    break
                usernum += 1
                usertxt += f"[{m.user.first_name}](tg://user?id={m.user.id})"
                if usernum == 14:
                    await app.send_message(
                        message.chat.id,
                        f"{text}\n{usertxt}",
                        disable_web_page_preview=True,
                    )
                    await asyncio.sleep(2)
                    usernum = 0
                    usertxt = ""
        except FloodWait as e:
            await asyncio.sleep(e.value)
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass


async def tag_all_admins(_, message):
    if message.chat.id in SPAM_CHATS:
        return await message.reply_text(
            "ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss ɪs ᴀʟʀᴇᴀᴅʏ ʀᴜɴɴɪɴɢ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴛᴏᴘ sᴏ ᴜsᴇ /cancel"
        )
    replied = message.reply_to_message
    if len(message.command) < 2 and not replied:
        await message.reply_text(
            "** ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴛᴀɢ ᴀʟʟ, ʟɪᴋᴇ »** `@admins Hi Friends`"
        )
        return
    if replied:
        try:
            SPAM_CHATS.append(message.chat.id)
            usernum = 0
            usertxt = ""
            async for m in app.get_chat_members(
                message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS
            ):
                if message.chat.id not in SPAM_CHATS:
                    break
                usernum += 1
                usertxt += f"[{m.user.first_name}](tg://user?id={m.user.id})"
                if usernum == 14:
                    await app.send_message(
                        message.chat.id,
                        f"{replied.text}\n\n {usertxt}",
                        disable_web_page_preview=True,
                    )
                    await asyncio.sleep(1)
                    usernum = 0
                    usertxt = ""

        except FloodWait as e:
            await asyncio.sleep(e.value)
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass
    else:
        try:
            text = message.text.split(None, 1)[1]
            SPAM_CHATS.append(message.chat.id)
            usernum = 0
            usertxt = ""
            async for m in app.get_chat_members(
                message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS
            ):
                if message.chat.id not in SPAM_CHATS:
                    break
                usernum += 1
                usertxt += f"[{m.user.first_name}](tg://user?id={m.user.id})"
                if usernum == 14:
                    await app.send_message(
                        message.chat.id,
                        f"{text}\n{usertxt}",
                        disable_web_page_preview=True,
                    )
                    await asyncio.sleep(2)
                    usernum = 0
                    usertxt = ""
        except FloodWait as e:
            await asyncio.sleep(e.value)
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass


@app.on_message(
    filters.command(
        ["atag", "aall", "amention", "amentionall"], prefixes=["/", "@", ".", "#"]
    )
    & admin_filter
)
async def atag_all_useres(_, message):
    userbot = await get_assistant(message.chat.id)
    if message.chat.id in SPAM_CHATS:
        return await message.reply_text(
            "ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss ɪs ᴀʟʀᴇᴀᴅʏ ʀᴜɴɴɪɴɢ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴛᴏᴘ sᴏ ᴜsᴇ /acancel"
        )
    replied = message.reply_to_message
    if len(message.command) < 2 and not replied:
        await message.reply_text(
            "** ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴛᴀɢ ᴀʟʟ, ʟɪᴋᴇ »** `@aall Hi Friends`"
        )
        return
    if replied:
        SPAM_CHATS.append(message.chat.id)
        usernum = 0
        usertxt = ""
        async for m in app.get_chat_members(message.chat.id):
            if message.chat.id not in SPAM_CHATS:
                break
            usernum += 1
            usertxt += f"[{m.user.first_name}](tg://openmessage?user_id={m.user.id})"
            if usernum == 14:
                await userbot.send_message(
                    message.chat.id,
                    f"{replied.text}\n\n{usertxt}",
                    disable_web_page_preview=True,
                )
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass
    else:
        text = message.text.split(None, 1)[1]

        SPAM_CHATS.append(message.chat.id)
        usernum = 0
        usertxt = ""
        async for m in app.get_chat_members(message.chat.id):
            if message.chat.id not in SPAM_CHATS:
                break
            usernum += 1
            usertxt += f'<a href="tg://openmessage?user_id={m.user.id}">{m.user.first_name}</a>'

            if usernum == 14:
                await userbot.send_message(
                    message.chat.id, f"{text}\n{usertxt}", disable_web_page_preview=True
                )
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass


@app.on_message(
    filters.command(["admin", "admins"], prefixes=["/", "@"]) & filters.group
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
        return await message.reply_text("**ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss sᴜᴄᴄᴇssғᴜʟʟʏ sᴛᴏᴘᴘᴇᴅ!**")

    else:
        await message.reply_text("**ɴᴏ ᴘʀᴏᴄᴇss ᴏɴɢᴏɪɴɢ!**")
        return
__HELP__ = """
**ᴛᴀɢɢɪɴɢ ᴜsᴇʀs ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs**

ᴜsᴇ ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴜsᴇʀs ᴏʀ ᴀᴅᴍɪɴs ɪɴ ᴀ ᴄʜᴀᴛ:

- /all ᴏʀ @all: ʀᴇᴘʟʏ ᴛᴏ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ ᴛᴇxᴛᴍᴇɴᴛɪᴏɴ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴛʜᴇ ᴄʜᴀᴛ.
- /admin ᴏʀ @admin : ʀᴇᴘʟʏ ᴛᴏ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ ᴛᴇxᴛ ᴍᴇɴᴛɪᴏɴ ᴀʟʟ ᴀᴅᴍɪɴs ɪɴ ᴛʜᴇ ᴄʜᴀᴛ.
- /cancel : sᴛᴏᴘ ᴛʜᴇ ᴏɴɢᴏɪɴɢ ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss.

ʜᴏᴡ ᴛᴏ ᴜsᴇ:
1. **ᴛᴀɢ ᴀʟʟ:** ᴛʏᴘᴇ `/all <ᴍᴇssᴀɢᴇ>` ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴀʟʟ ᴍᴇᴍʙᴇʀs.
2. **ᴛᴀɢ ᴀᴅᴍɪɴs:** ᴛʏᴘᴇ `/admin <ᴍᴇssᴀɢᴇ>` ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴀʟʟ ᴀᴅᴍɪɴs.
3. **ᴄᴀɴᴄᴇʟ ᴛᴀɢɢɪɴɢ:** ᴛʏᴘᴇ `/stopmention` ᴛᴏ sᴛᴏᴘ ᴛʜᴇ ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss.

ɴᴏᴛᴇ:
- ᴛʜᴇ ʙᴏᴛ ᴍᴜsᴛ ʙᴇ ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ ᴛᴏ ᴜsᴇ ᴛʜᴇsᴇ ғᴜɴᴄᴛɪᴏɴs.
- ᴀᴠᴏɪᴅ sᴘᴀᴍᴍɪɴɢ ᴛᴏ ᴘʀᴇᴠᴇɴᴛ ʙᴇɪɴɢ ʙᴀɴɴᴇᴅ.

**ʜᴀᴘᴘʏ ᴛᴀɢɢɪɴɢ!**
"""

__MODULE__ = "Tᴀɢ"
