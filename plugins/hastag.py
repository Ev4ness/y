from MukeshAPI import api
from pyrogram import filters

from DanteMusic import app


@app.on_message(filters.command("hastag"))
async def hastag(bot, message):

    try:
        text = message.text.split(" ", 1)[1]
        res = api.hashtag(text)
        results = " ".join(res)
        hashtags = results.replace(",", "").replace("[", "").replace("]", "")

    except IndexError:
        return await message.reply_text("Example:\n\n/hastag python")

    await message.reply_text(
        f"here is your  hastag :\n<pre>{hashtags}</pre>", quote=True
    )


__MODULE__ = "Hastag"
__HELP__ = """<blockquote><b>
**hashtag generator:**

• `/hashtag [text]`: Generate hashtags for the given text.
</b></blockquote>"""
