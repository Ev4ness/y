from pyrogram import filters
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import Message, User

from DanteMusic import app


def ReplyCheck(message: Message):
    reply_id = None

    if message.reply_to_message:
        reply_id = message.reply_to_message.message_id

    elif not message.from_user.is_self:
        reply_id = message.message_id

    return reply_id


infotext = (
    "[{full_name}](tg://user?id={user_id})\n\n"
    "user id: `{user_id}`\n"
    "first name: `{first_name}`\n"
    "last name: `{last_name}`\n"
    "username: `@{username}`\n"
    "last seen: `{last_online}`"
)


def LastOnline(user: User):
    if user.is_bot:
        return ""
    elif user.status == "recently":
        return "recently"
    elif user.status == "within_week":
        return "within the last week"
    elif user.status == "within_month":
        return "within the last month"
    elif user.status == "long_time_ago":
        return "a long time ago :("
    elif user.status == "online":
        return "currently online"
    elif user.status == "offline":
        return datetime.fromtimestamp(user.status.date).strftime(
            "%a, %d %b %Y, %H:%M:%S"
        )


def FullName(user: User):
    return user.first_name + " " + user.last_name if user.last_name else user.first_name


@app.on_message(filters.command("whois"))
async def whois(client, message):
    cmd = message.command
    if not message.reply_to_message and len(cmd) == 1:
        get_user = message.from_user.id
    elif len(cmd) == 1:
        get_user = message.reply_to_message.from_user.id
    elif len(cmd) > 1:
        get_user = cmd[1]
        try:
            get_user = int(cmd[1])
        except ValueError:
            pass
    try:
        user = await client.get_users(get_user)
    except PeerIdInvalid:
        await message.reply("I don't know that user.")
        return
    desc = await client.get_chat(get_user)
    desc = desc.description
    await message.reply_text(
        infotext.format(
            full_name=FullName(user),
            user_id=user.id,
            user_dc=user.dc_id,
            first_name=user.first_name,
            last_name=user.last_name if user.last_name else "",
            username=user.username if user.username else "",
            last_online=LastOnline(user),
            bio=desc if desc else "emᴩty.",
        ),
        disable_web_page_preview=True,
    )
__HELP__ = """<blockquote><b>
**command:**

• /whois - **check user information.**

**info:**

- this bot provides a command to check user information.
- use /whois command followed by a reply to a message or a user id to get information about the user.

**note:**

- the /whois command can be used to retrieve information about a user in the chat.
- the information includes user id, first name, last name, username, and last seen status.</b></blockquote>
"""

__MODULE__ = "WhoIs"
