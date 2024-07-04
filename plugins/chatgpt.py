import requests
from pyrogram import filters
from pyrogram.enums import ChatAction
from TheApi import api

from DanteMusic import app


@app.on_message(
    filters.command(
        ["chatgpt", "ai", "ask"], prefixes=["/"]
    )
)
async def chatgpt_chat(bot, message):
    if len(message.command) < 2 and not message.reply_to_message:
        await message.reply_text(
            "Example:\n\n`/ai write simple website code using html css, js?`"
        )
        return

    if message.reply_to_message and message.reply_to_message.text:
        user_input = message.reply_to_message.text
    else:
        user_input = " ".join(message.command[1:])

    try:
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        results = api.chatgpt(user_input)
        if results["success"]:
            await message.reply_text(results["results"])
    except requests.exceptions.RequestException as e:
        pass


__MODULE__ = "ChatGPT"
__HELP__ = """<blockquote><b>
/advice - get random advice by bot
/ai [query] - ask your question with chatgpt's ai
/gemini [query] - ask your question with google's gemini ai
/bard [query] -ask your question with google's bard ai.</b></blockquote>"""
