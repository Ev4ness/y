from DanteMusic import app 
from pyrogram import filters
import nekos

@app.on_message(filters.command("slap"))
async def slap(client, message):
    try:
        if message.reply_to_message:
            await message.reply_video(nekos.img("slap"), caption=f"{message.from_user.mention} slapped {message.reply_to_message.from_user.mention}")
        else:
            await message.reply_video(nekos.img("slap"))
    except Exception as e:
        await message.reply_text(f"Error: {e}")

__HELP__ = """<blockquote><b>
Available commands:
- /slap: Slaps someone. If used as a reply, slaps the replied user.
</b></blockquote>"""
__MODULE__ = "Slap"
