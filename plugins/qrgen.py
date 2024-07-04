from pyrogram import filters

from DanteMusic import app


@app.on_message(filters.command(["qr"]))
async def write_text(client, message):
    if len(message.command) < 2:
        await message.reply_text("**Usage**:- `/qr https://t.me/`")
        return
    text = " ".join(message.command[1:])
    photo_url = "https://apis.xditya.me/qr/gen?text=" + text
    await app.send_photo(
        chat_id=message.chat.id, photo=photo_url, caption="Here is your qrcode"
    )

__MODULE__ = "Qr"

__HELP__ = """<blockquote><b>
Ƭhis module generates Qr codes. Use the /qr command followed by the text or URL you want to encode into a Qr code. For example, `/qr name`. The bot will then generate a Qr code for the provided input. Make sure to include the protocol (http:// or https://) for URLs. Enjoy creating Qr codes with ease!
</b></blockquote>"""
