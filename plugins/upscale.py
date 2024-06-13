from pyrogram import Client, filters
from lexica import Client as LexicaClient

from YukkiMusic import app 

lexica_client = LexicaClient()

def upscale_image(image: bytes) -> bytes:
    return lexica_client.upscale(image)

@app.on_message(filters.command("upscale") & filters.reply)
async def upscale_reply_image(client, message):
    if message.reply_to_message.photo:
        photo = await client.download_media(message.reply_to_message.photo.file_id)
        
        with open(photo, 'rb') as f:
            image_bytes = f.read()
        
        upscaled_image_bytes = upscale_image(image_bytes)
        
        with open('upscaled.png', 'wb') as f:
            f.write(upscaled_image_bytes)
            await message.reply_photo(photo='upscaled.png')