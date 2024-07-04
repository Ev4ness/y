from pyrogram import filters
from DanteMusic import app


@app.on_message(filters.command("id"))
async def get_id(client, message):
    try:
        if not message.reply_to_message and message.chat:
            await message.reply(
                f"user <b>{message.from_user.first_name}'s</b> id is <code>{message.from_user.id}</code>.\nthis chat's id is: <code>{message.chat.id}</code>."
            )
        elif not message.reply_to_message.sticker or message.reply_to_message is None:
            if message.reply_to_message.forward_from_chat:
                await message.reply(f"The forwarded {str(message.reply_to_message.forward_from_chat.type)[9:].lower()}, {message.reply_to_message.forward_from_chat.title} has an ID of <code>{message.reply_to_message.forward_from_chat.id}</code>")

            elif message.reply_to_message.forward_from:
                await message.reply(
                    f"The forwarded user, {message.reply_to_message.forward_from.first_name} has an ID of <code>{message.reply_to_message.forward_from.id}</code>."
                )

            elif message.reply_to_message.forward_sender_name:
                await message.reply(
                    "Sorry, I never saw that user's message or I am unable to fetch the ID."
                )
            else:
                await message.reply(
                    f"user {message.reply_to_message.from_user.first_name}'s ID is <code>{message.reply_to_message.from_user.id}</code>."
                )
        elif message.reply_to_message.sticker:
            if message.reply_to_message.forward_from_chat:
                await message.reply(
                    f"The forwarded {str(message.reply_to_message.forward_from_chat.type)[9:].lower()}, {message.reply_to_message.forward_from_chat.title} has an ID of <code>{message.reply_to_message.forward_from_chat.id}</code> \nand the replied sticker ID is <code>{message.reply_to_message.sticker.file_id}</code>"
                )

            elif message.reply_to_message.forward_from:
                await message.reply(
                    f"The forwarded user, {message.reply_to_message.forward_from.first_name} has an ID of <code>{message.reply_to_message.forward_from.id}</code> \nand the replied sticker ID is <code>{message.reply_to_message.sticker.file_id}</code>."
                )

            elif message.reply_to_message.forward_sender_name:
                await message.reply(
                    "Sorry, I never saw that user's message or I am unable to fetch the ID."
                )

            else:
                await message.reply(
                    f"user {message.reply_to_message.from_user.first_name}'s ID is <code>{message.reply_to_message.from_user.id}</code>\n and the replied sticker ID is <code>{message.reply_to_message.sticker.file_id}</code>."
                )
        else:
            await message.reply(
                f"User {message.reply_to_message.from_user.first_name}'s user ID is <code>{message.reply_to_message.from_user.id}</code>."
            )
    except Exception as r:
        await message.reply(f"An error occurred while getting the ID. {r}")

__MODULE__ = "UserID"
__HELP__ = """<blockquote><b>
**id retriever:**

• `/id`: Retrieve user and chat IDs.
</b></blockquote>"""
