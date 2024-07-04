import asyncio
import re
from contextlib import suppress
from time import time

from pyrogram import filters
from pyrogram.enums import ChatMembersFilter, ChatMemberStatus, ChatType
from pyrogram.types import (
    CallbackQuery,
    ChatPermissions,
    ChatPrivileges,
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from string import ascii_lowercase
from typing import Dict, List, Union

from DanteMusic import app
from DanteMusic.misc import SUDOERS
from DanteMusic.core.mongo import mongodb
from utils.error import capture_err
from DanteMusic.utils.keyboard import ikb
from DanteMusic.utils.database import save_filter
from DanteMusic.utils.functions import (
    extract_user,
    extract_user_and_reason,
    time_converter,
)
from DanteMusic.utils.permissions import adminsOnly, member_permissions
from config import adminlist, BANNED_USERS
warnsdb = mongodb.warns

__MODULE__ = "Ban"
__HELP__ = """<blockquote><b>
/ban - Ban A User
/sban - Delete all messages of user that sended in group and ban the user
/tban - Ban A User For Specific Time
/unban - Unban A User
/warn - Warn A User
/swarn - Delete all the message sended in group and warn the user
/rmwarns - Remove All Warning of A User
/warns - Show Warning Of A User
/kick - Kick A User
/skick - Delete the replied message kicking its sender
/purge - Purge Messages
/purge [n] - Purge "n" number of messages from replied message
/del - Delete Replied Message
/promote - Promote A Member
/fullpromote - Promote A Member With All Rights
/demote - Demote A Member
/pin - Pin A Message
/unpin - unpin a message 
/unpinall - unpinall messages 
/mute - Mute A User
/tmute - Mute A User For Specific Time
/unmute - Unmute A User
/zombies - Ban Deleted Accounts
/report | @admins | @admin - Report A Message To Admins.
/link - Send in Group/SuperGroup Invite Link.</b></blockquote>"""

async def int_to_alpha(user_id: int) -> str:
    alphabet = list(ascii_lowercase)[:10]
    text = ""
    user_id = str(user_id)
    for i in user_id:
        text += alphabet[int(i)]
    return text
    
async def get_warns_count() -> dict:
    chats_count = 0
    warns_count = 0
    async for chat in warnsdb.find({"chat_id": {"$lt": 0}}):
        for user in chat["warns"]:
            warns_count += chat["warns"][user]["warns"]
        chats_count += 1
    return {"chats_count": chats_count, "warns_count": warns_count}


async def get_warns(chat_id: int) -> Dict[str, int]:
    warns = await warnsdb.find_one({"chat_id": chat_id})
    if not warns:
        return {}
    return warns["warns"]


async def get_warn(chat_id: int, name: str) -> Union[bool, dict]:
    name = name.lower().strip()
    warns = await get_warns(chat_id)
    if name in warns:
        return warns[name]


async def add_warn(chat_id: int, name: str, warn: dict):
    name = name.lower().strip()
    warns = await get_warns(chat_id)
    warns[name] = warn

    await warnsdb.update_one(
        {"chat_id": chat_id}, {"$set": {"warns": warns}}, upsert=True
    )


async def remove_warns(chat_id: int, name: str) -> bool:
    warnsd = await get_warns(chat_id)
    name = name.lower().strip()
    if name in warnsd:
        del warnsd[name]
        await warnsdb.update_one(
            {"chat_id": chat_id},
            {"$set": {"warns": warnsd}},
            upsert=True,
        )
        return True
    return False

@app.on_message(filters.command(["kick", "skick"]) & ~filters.private & ~BANNED_USERS)
@adminsOnly("can_restrict_members")
async def kickFunc(_, message: Message):
    user_id, reason = await extract_user_and_reason(message)
    if not user_id:
        return await message.reply_text("i can't find that user")
    if user_id == app.id:
        return await message.reply_text(
            "i can't kick myself, i can leave if you want."
        )
    if user_id in SUDOERS:
        return await message.reply_text("you wanna kick the elevated one ?")
    if user_id in [member.user.id async for member  in app.get_chat_members(chat_id=message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS
)]:
        return await message.reply_text(
            "i can't kick an admin, you know the rules, you know the rules, so do i "
        )
    mention = (await app.get_users(user_id)).mention
    msg = f"""
**kicked user:** {mention}
**kicked by:** {message.from_user.mention if message.from_user else 'anonmous'}
**reason:** {reason or 'no reason provided'}"""
    await message.chat.ban_member(user_id)
    replied_message = message.reply_to_message
    if replied_message:
        message = replied_message
    await message.reply_text(msg)
    await asyncio.sleep(1)
    await message.chat.unban_member(user_id)
    if message.command[0][0] == "s":
        await message.reply_to_message.delete()
        await app.delete_user_history(message.chat.id, user_id)


# Ban members


@app.on_message(filters.command(["ban", "sban", "tban"]) & ~filters.private & ~BANNED_USERS)
@adminsOnly("can_restrict_members")
async def banFunc(_, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)

    if not user_id:
        return await message.reply_text("I can't find that user.")
    if user_id == app.id:
        return await message.reply_text(
            "I can't ban myself, i can leave if you want."
        )
    if user_id in SUDOERS:
        return await message.reply_text(
            "You Wanna Ban The Elevated One?, RECONSIDER!"
        )
    if user_id in [member.user.id async for member  in app.get_chat_members(chat_id=message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS
)]:
        return await message.reply_text(
            "I can't ban an admin, You know the rules, so do i."
        )

    try:
        mention = (await app.get_users(user_id)).mention
    except IndexError:
        mention = (
            message.reply_to_message.sender_chat.title
            if message.reply_to_message
            else "Anon"
        )

    msg = (
        f"**Banned User:** {mention}\n"
        f"**Banned By:** {message.from_user.mention if message.from_user else 'Anon'}\n"
    )
    if message.command[0][0] == "s":
        await message.reply_to_message.delete()
        await app.delete_user_history(message.chat.id, user_id)
    if message.command[0] == "tban":
        split = reason.split(None, 1)
        time_value = split[0]
        temp_reason = split[1] if len(split) > 1 else ""
        temp_ban = await time_converter(message, time_value)
        msg += f"**Banned For:** {time_value}\n"
        if temp_reason:
            msg += f"**Reason:** {temp_reason}"
        with suppress(AttributeError):
            if len(time_value[:-1]) < 3:
                await message.chat.ban_member(user_id, until_date=temp_ban)
                replied_message = message.reply_to_message
                if replied_message:
                    message = replied_message
                await message.reply_text(msg)
            else:
                await message.reply_text("You can't use more than 99")
        return
    if reason:
        msg += f"**Reason:** {reason}"
    await message.chat.ban_member(user_id)
    replied_message = message.reply_to_message
    if replied_message:
        message = replied_message
    await message.reply_text(msg)


# Unban members


@app.on_message(filters.command("unban") & ~filters.private & ~BANNED_USERS)
@adminsOnly("can_restrict_members")
async def unban_func(_, message: Message):
    # we don't need reasons for unban, also, we
    # don't need to get "text_mention" entity, because
    # normal users won't get text_mention if the user
    # they want to unban is not in the group.
    reply = message.reply_to_message
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply_text("I can't find that user.")

    if reply and reply.sender_chat and reply.sender_chat != message.chat.id:
        return await message.reply_text("You cannot unban a channel")

    await message.chat.unban_member(user_id)
    umention = (await app.get_users(user_id)).mention
    replied_message = message.reply_to_message
    if replied_message:
        message = replied_message
    await message.reply_text(f"Unbanned! {umention}")
 # Promote Members


@app.on_message(filters.command(["promote", "fullpromote"]) & ~filters.private & ~BANNED_USERS)
@adminsOnly("can_promote_members")
async def promoteFunc(_, message: Message):
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply_text("I can't find that user.")

    bot = (await app.get_chat_member(message.chat.id, app.id)).privileges
    if user_id == app.id:
        return await message.reply_text("I can't promote myself.")
    if not bot:
        return await message.reply_text("I'm not an admin in this chat.")
    if not bot.can_promote_members:
        return await message.reply_text("I don't have enough permissions")

    umention = (await app.get_users(user_id)).mention

    if message.command[0][0] == "f":
        await message.chat.promote_member(
            user_id=user_id,
            privileges=ChatPrivileges(
                can_change_info=bot.can_change_info,
                can_invite_users=bot.can_invite_users,
                can_delete_messages=bot.can_delete_messages,
                can_restrict_members=bot.can_restrict_members,
                can_pin_messages=bot.can_pin_messages,
                can_promote_members=bot.can_promote_members,
                can_manage_chat=bot.can_manage_chat,
                can_manage_video_chats=bot.can_manage_video_chats,
            ),
        )
        return await message.reply_text(f"Fully Promoted! {umention}")

    await message.chat.promote_member(
        user_id=user_id,
        privileges=ChatPrivileges(
            can_change_info=False,
            can_invite_users=bot.can_invite_users,
            can_delete_messages=bot.can_delete_messages,
            can_restrict_members=False,
            can_pin_messages=False,
            can_promote_members=False,
            can_manage_chat=bot.can_manage_chat,
            can_manage_video_chats=bot.can_manage_video_chats,
        ),
    )
    await message.reply_text(f"Promoted! {umention}")


# Demote Member



@app.on_message(filters.command("purge") & ~filters.private)
@adminsOnly("can_delete_messages")
async def purgeFunc(_, message: Message):
    repliedmsg = message.reply_to_message
    await message.delete()

    if not repliedmsg:
        return await message.reply_text("Reply to a message to purge from.")

    cmd = message.command
    if len(cmd) > 1 and cmd[1].isdigit():
        purge_to = repliedmsg.id + int(cmd[1])
        if purge_to > message.id:
            purge_to = message.id
    else:
        purge_to = message.id

    chat_id = message.chat.id
    message_ids = []

    for message_id in range(
        repliedmsg.id,
        purge_to,
    ):
        message_ids.append(message_id)

        # Max message deletion limit is 100
        if len(message_ids) == 100:
            await app.delete_messages(
                chat_id=chat_id,
                message_ids=message_ids,
                revoke=True,  # For both sides
            )

            # To delete more than 100 messages, start again
            message_ids = []

    # Delete if any messages left
    if len(message_ids) > 0:
        await app.delete_messages(
            chat_id=chat_id,
            message_ids=message_ids,
            revoke=True,
        )



@app.on_message(filters.command("del") & ~filters.private)
@adminsOnly("can_delete_messages")
async def deleteFunc(_, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("Reply To A Message To Delete It")
    await message.reply_to_message.delete()
    await message.delete()



@app.on_message(filters.command("demote") & ~filters.private & ~BANNED_USERS)
@adminsOnly("can_promote_members")
async def demote(_, message: Message):
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply_text("I can't find that user.")
    if user_id == app.id:
        return await message.reply_text("I can't demote myself.")
    if user_id in SUDOERS:
        return await message.reply_text(
            "You wanna demote the elevated one?, RECONSIDER!"
        )
    try:
        member = await app.get_chat_member(message.chat.id, user_id)
        if member.status == ChatMemberStatus.ADMINISTRATOR:
            await message.chat.promote_member(
                user_id=user_id,
                privileges=ChatPrivileges(
                    can_change_info=False,
                    can_invite_users=False,
                    can_delete_messages=False,
                    can_restrict_members=False,
                    can_pin_messages=False,
                    can_promote_members=False,
                    can_manage_chat=False,
                    can_manage_video_chats=False,
                ),
            )
            umention = (await app.get_users(user_id)).mention
            await message.reply_text(f"Demoted! {umention}")
        else:
            await message.reply_text(
                "The person you mentioned is not an admin."
            )
    except Exception as e:
        await message.reply_text(e)


# Pin Messages
 
@app.on_message(filters.command(["unpinall"]) & filters.group & ~BANNED_USERS)
@adminsOnly("can_pin_messages")
async def pin(_, message: Message):
    if message.command[0] == "unpinall":
        return await message.reply_text("Are you sure you want to unpin all messages?",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="yes", callback_data="unpin_yes"),InlineKeyboardButton(text="no", callback_data="unpin_no")],]))


@app.on_callback_query(filters.regex(r"unpin_(yes|no)"))
async def callback_query_handler(_, query: CallbackQuery):
    if query.data == "unpin_yes":
        await app.unpin_all_chat_messages(query.message.chat.id)
        return await query.message.edit_text("All pinned messages have been unpinned.")
    elif query.data == "unpin_no":
        return await query.message.edit_text("Unpin of all pinned messages has been cancelled.")


@app.on_message(filters.command(["pin", "unpin"]) & ~filters.private & ~BANNED_USERS)
@adminsOnly("can_pin_messages")
async def pin(_, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("Reply to a message to pin/unpin it.")
    r = message.reply_to_message
    if message.command[0][0] == "u":
        await r.unpin()
        return await message.reply_text(
            f"Unpinned [this]({r.link}) message.",
            disable_web_page_preview=True,
        )
    await r.pin(disable_notification=True)
    await message.reply(
        f"Pinned [this]({r.link}) message.",
        disable_web_page_preview=True,
    )
    msg = "Please check the pinned message: ~ " + f"[Check, {r.link}]"
    filter_ = dict(type="text", data=msg)
    await save_filter(message.chat.id, "~pinned", filter_)
# Mute members

@app.on_message(filters.command(["mute", "tmute"]) & ~filters.private & ~BANNED_USERS)
@adminsOnly("can_restrict_members")
async def mute(_, message: Message):
    user_id, reason = await extract_user_and_reason(message)
    if not user_id:
        return await message.reply_text("I can't find that user.")
    if user_id == app.id:
        return await message.reply_text("I can't mute myself.")
    if user_id in SUDOERS:
        return await message.reply_text(
            "You wanna mute the elevated one?, RECONSIDER!"
        )
    if user_id in [member.user.id async for member  in app.get_chat_members(chat_id=message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS
)]:
        return await message.reply_text(
            "I can't mute an admin, You know the rules, so do i."
        )
    mention = (await app.get_users(user_id)).mention
    keyboard = ikb({"🚨  Unmute  🚨": f"unmute_{user_id}"})
    msg = (
        f"**Muted User:** {mention}\n"
        f"**Muted By:** {message.from_user.mention if message.from_user else 'Anon'}\n"
    )
    if message.command[0] == "tmute":
        split = reason.split(None, 1)
        time_value = split[0]
        temp_reason = split[1] if len(split) > 1 else ""
        temp_mute = await time_converter(message, time_value)
        msg += f"**Muted For:** {time_value}\n"
        if temp_reason:
            msg += f"**Reason:** {temp_reason}"
        try:
            if len(time_value[:-1]) < 3:
                await message.chat.restrict_member(
                    user_id,
                    permissions=ChatPermissions(),
                    until_date=temp_mute,
                )
                replied_message = message.reply_to_message
                if replied_message:
                    message = replied_message
                await message.reply_text(msg, reply_markup=keyboard)
            else:
                await message.reply_text("You can't use more than 99")
        except AttributeError:
            pass
        return
    if reason:
        msg += f"**Reason:** {reason}"
    await message.chat.restrict_member(user_id, permissions=ChatPermissions())
    replied_message = message.reply_to_message
    if replied_message:
        message = replied_message
    await message.reply_text(msg, reply_markup=keyboard)

@app.on_message(filters.command("unmute") & ~filters.private & ~BANNED_USERS)
@adminsOnly("can_restrict_members")
async def unmute(_, message: Message):
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply_text("I can't find that user.")
    await message.chat.unban_member(user_id)
    umention = (await app.get_users(user_id)).mention
    replied_message = message.reply_to_message
    if replied_message:
        message = replied_message
    await message.reply_text(f"Unmuted! {umention}")
 
@app.on_message(filters.command(["warn", "swarn"]) & ~filters.private & ~BANNED_USERS)
@adminsOnly("can_restrict_members")
async def warn_user(_, message: Message):
    user_id, reason = await extract_user_and_reason(message)
    chat_id = message.chat.id
    if not user_id:
        return await message.reply_text("i cant find that user")
    if user_id == app.id:
        return await message.reply_text(
            "i can't warn myself, i can leave if you want."
        )
    if user_id in SUDOERS:
        return await message.reply_text(
            "i can't warn my manager's, because he manage me!"
        )
    if user_id in [member.user.id async for member  in app.get_chat_members(chat_id=message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS
)]:
        return await message.reply_text(
            "i can't warn an admin, you know the rules so do i."
        )
    user, warns = await asyncio.gather(
        app.get_users(user_id),
        get_warn(chat_id, await int_to_alpha(user_id)),
    )
    mention = user.mention
    keyboard = ikb({"🚨  remove warn  🚨": f"unwarn_{user_id}"})
    if warns:
        warns = warns["warns"]
    else:
        warns = 0
    if message.command[0][0] == "s":
        await message.reply_to_message.delete()
        await app.delete_user_history(message.chat.id, user_id)
    if warns >= 2:
        await message.chat.ban_member(user_id)
        await message.reply_text(
            f"number of warns of {mention} exceeded, banned!"
        )
        await remove_warns(chat_id, await int_to_alpha(user_id))
    else:
        warn = {"warns": warns + 1}
        msg = f"""
**warned user:** {mention}
**warned by:** {message.from_user.mention if message.from_user else 'anonmous'}
**reason :** {reason or 'no reason provoded'}
**warns:** {warns + 1}/3"""
        replied_message = message.reply_to_message
        if replied_message:
            message = replied_message
        await message.reply_text(msg, reply_markup=keyboard)
        await add_warn(chat_id, await int_to_alpha(user_id), warn)


@app.on_callback_query(filters.regex("unwarn_") & ~BANNED_USERS)
async def remove_warning(_, cq: CallbackQuery):
    from_user = cq.from_user
    chat_id = cq.message.chat.id
    permissions = await member_permissions(chat_id, from_user.id)
    permission = "can_restrict_members"
    if permission not in permissions:
        return await cq.answer(
            "you don't have enough permissions to perform this action\n"
            + f"permission needed: {permission}",
            show_alert=True,
        )
    user_id = cq.data.split("_")[1]
    warns = await get_warn(chat_id, await int_to_alpha(user_id))
    if warns:
        warns = warns["warns"]
    if not warns or warns == 0:
        return await cq.answer("user has no warnings.")
    warn = {"warns": warns - 1}
    await add_warn(chat_id, await int_to_alpha(user_id), warn)
    text = cq.message.text.markdown
    text = f"~~{text}~~\n\n"
    text += f"__warn removed by {from_user.mention}__"
    await cq.message.edit(text)

@app.on_message(filters.command("rmwarns") & ~filters.private & ~BANNED_USERS)
@adminsOnly("can_restrict_members")
async def remove_warnings(_, message: Message):
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply_text("I can't find that user.")
    mention =  (await app.get_users(user_id)).mention
    chat_id = message.chat.id
    warns = await get_warn(chat_id, await int_to_alpha(user_id))
    if warns:
        warns = warns["warns"]
    if warns == 0 or not warns:
        await message.reply_text(f"{mention} has no warnings.")
    else:
        await remove_warns(chat_id, await int_to_alpha(user_id))
        await message.reply_text(f"removed warnings of {mention}.")

@app.on_message(filters.command("warns") & ~filters.private & ~BANNED_USERS)
@capture_err
async def check_warns(_, message: Message):
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply_text("i can't find that user.")
    warns = await get_warn(message.chat.id, await int_to_alpha(user_id))
    mention = (await app.get_users(user_id)).mention
    if warns:
        warns = warns["warns"]
    else:
        return await message.reply_text(f"{mention} has no warnings.")
    return await message.reply_text(f"{mention} has {warns}/3 warnings")
 
@app.on_message(filters.command("link") & ~BANNED_USERS)
@adminsOnly("can_invite_users")
async def invite(_, message):
    if message.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        link = (await app.get_chat(message.chat.id)).invite_link
        if not link:
            link = await app.export_chat_invite_link(message.chat.id)
        text = f"here's the group invite link \n\n{link}"
        if message.reply_to_message:
            await message.reply_to_message.reply_text(
                text, disable_web_page_preview=True
            )
        else:
            await message.reply_text(text, disable_web_page_preview=True)
