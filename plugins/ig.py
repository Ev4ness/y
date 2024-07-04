import requests
from pyrogram import filters

from DanteMusic import app


@app.on_message(filters.command(["ig", "instagram", "reel"]))
async def download_instagram_video(client, message):
    if len(message.command) < 2:
        await message.reply_text(
            "Please provide the Instagram reel URL after the command"
        )
        return
    a = await message.reply_text("processing...")
    url = message.text.split()[1]
    api_url = (
        f"https://nodejs-1xn1lcfy3-jobians.vercel.app/v2/downloader/instagram?url={url}"
    )

    response = requests.get(api_url)
    data = response.json()

    if data["status"]:
        video_url = data["data"][0]["url"]
        await a.delete()
        await client.send_video(message.chat.id, video_url)
    else:
        await a.edit("Failed to download reel")

__MODULE__ = "Reel"
__HELP__ = """<blockquote><b>
**instagram reel downloader:**

• `/ig [URL]`: download instagram reels. Provide the instagram reel URL after the command.
• `/instagram [URL]`: download instagram reels. Provide the instagram reel URL after the command.
• `/reel [URL]`: download instagram reels. Provide the instagram reel URL after the command.
</b></blockquote>"""
