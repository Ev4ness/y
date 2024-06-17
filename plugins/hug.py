from YukkiMusic import app 
from pyrogram import client, filters
import nekos

@app.on_message(filters.command("hug"))
async def huggg(client, message):
    try:
        if message.reply_to_message:
            await message.reply_video(nekos.img("hug"), caption=f"{message.from_user.mention} hugged {message.reply_to_message.from_user.mention}")
        else:
            await message.reply_video(nekos.img("hug"))
    except Exception as e:
        await message.reply_text(f"Error: {e}")