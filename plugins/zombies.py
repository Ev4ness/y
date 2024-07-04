import asyncio

from pyrogram import enums, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import FloodWait
from DanteMusic import app
from DanteMusic.utils.permissions import adminsOnly

chatQueue = []

stopProcess = False


@app.on_message(filters.command(["zombies"]))
@adminsOnly("can_restrict_members") 
async def remove(client, message):

    global stopProcess
    try:
        try:
            sender = await app.get_chat_member(message.chat.id, message.from_user.id)
            has_permissions = sender.privileges
        except:
            has_permissions = message.sender_chat
        if has_permissions:
            bot = await app.get_chat_member(message.chat.id, "self")
            if bot.status == ChatMemberStatus.MEMBER:
                await message.reply(
                    "➠ | i need admin permissions to remove deleted accounts."
                )
            else:
                if len(chatQueue) > 30:
                    await message.reply(
                        "➠ | i'm already working on my maximum number of 30 chats at the moment. please try again shortly."
                    )
                else:
                    if message.chat.id in chatQueue:
                        await message.reply(
                            "➠ | there's already an ongiing process in this chat. please [ /stop ] to start a new one."
                        )
                    else:
                        chatQueue.append(message.chat.id)
                        deletedList = []
                        async for member in app.get_chat_members(message.chat.id):
                            if member.user.is_deleted == True:
                                deletedList.append(member.user)
                            else:
                                pass
                        lenDeletedList = len(deletedList)
                        if lenDeletedList == 0:
                            await message.reply("⟳ | no deleted accounts in this chat.")
                            chatQueue.remove(message.chat.id)
                        else:
                            k = 0
                            processTime = lenDeletedList * 1
                            temp = await app.send_message(
                                message.chat.id,
                                f"🧭 | total of {lenDeletedList} deleted accounts has been detected.\n🥀 | estimated time: {processTime} seconds from now.",
                            )
                            if stopProcess:
                                stopProcess = False
                            while len(deletedList) > 0 and not stopProcess:
                                deletedAccount = deletedList.pop(0)
                                try:
                                    await app.ban_chat_member(
                                        message.chat.id, deletedAccount.id
                                    )
                                except Exception:
                                    pass
                                k += 1
                                await asyncio.sleep(10)
                            if k == lenDeletedList:
                                await message.reply(
                                    f"✅ | successfully removed all deleted acciunts from this chat."
                                )
                                await temp.delete()
                            else:
                                await message.reply(
                                    f"✅ | successfully removed {k} deleted accounts from this chat."
                                )
                                await temp.delete()
                            chatQueue.remove(message.chat.id)
        else:
            await message.reply(
                "👮🏻 | sorry, **only admin** can execute this command."
            )
    except FloodWait as e:
        await asyncio.sleep(e.value)

__MODULE__ = "Zombies"
__HELP__ = """<blockquote><b>
**commands:**
- /zombies: remove deleted accounts from the group.

**info:**
- module name: remove deleted accounts
- description: remove deleted accounts from the group.
- commands: /zombies
- permissions needed: can restrict members

**note:**
- use directly in a group chat with me for best effect. only admins can execute this command.</b></blockquote>"""
