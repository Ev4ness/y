from pyrogram import filters
from TheApi import api

from DanteMusic import app


@app.on_message(filters.command(["write"]))
async def write(client, message):
    if message.reply_to_message and message.reply_to_message.text:
        txt = message.reply_to_message.text
    elif len(message.command) > 1:
        txt = message.text.split(None, 1)[1]
    else:
        return await message.reply(
            "Please reply to message or write after command to use write CMD"
        )
    nan = await message.reply_text("Processing...")
    try:
        img = api.write(txt)
        await message.reply_photo(img)
        await nan.delete()
    except Exception as e:
        await nan.edit(e)

__MODULE__ = "Write"
__HELP__ = """<blockquote><b>
**COMMANDS**:
- /write: write text on an cloud and get an edited photo.

**INFO**:
- module name: write
- description: write text on an cloud and get an edited photo.
- commands: /write
- permissions needed: none

**NOTE**:
- use directly in a group chat with me for the best results.</b></blockquote>"""
