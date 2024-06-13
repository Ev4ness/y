from pyrogram import Client, filters
from lexica import Client as LexicaClient

from YukkiMusic import app 
from utils.error import capture_err

lexica_client = LexicaClient()

def upscale_image(image: bytes) -> bytes:
    return lexica_client.upscale(image)

@app.on_message(filters.command("upscale"))
@capture_err
async def upscale_reply_image(client, message):
    if not message.reply_to_message.photo:
        return await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ᴛᴏ ᴜᴘsᴄᴀʟᴇ ɪᴛ....😑")
    if message.reply_to_message.photo:
        a = await message.reply_text("ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ᴀ ᴍᴏᴍᴇɴᴛ......")
        photo = await client.download_media(message.reply_to_message.photo.file_id)
        
        with open(photo, 'rb') as f:
            image_bytes = f.read()
        try:
            upscaled_image_bytes = upscale_image(image_bytes)
            await a.edit("ᴀʟᴍᴏsᴛ ᴅᴏɴᴇ......❣️")
            with open('upscaled.png', 'wb') as f:
                f.write(upscaled_image_bytes)
                await message.reply_photo(photo='upscaled.png')
                await a.delete()
        except Exception as e:
            await e.edit(e)
