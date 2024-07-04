import asyncio
from random import choice
from pyrogram.errors import FloodWait

import pyfiglet
from pyrogram import filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from DanteMusic import app


def figle(text):
    x = pyfiglet.FigletFont.getFonts()
    font = choice(x)
    figled = str(pyfiglet.figlet_format(text, font=font))
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="change", callback_data="figlet"),
                InlineKeyboardButton(text="close", callback_data="close_reply"),
            ]
        ]
    )
    return figled, keyboard


@app.on_message(filters.command("figlet"))
async def echo(bot, message):
    global text
    try:
        text = message.text.split(" ", 1)[1]
    except IndexError:
        return await message.reply_text("Example:\n\n`/figlet Yukki `")
    kul_text, keyboard = figle(text)
    await message.reply_text(
        f"here is your figlet :\n<pre>{kul_text}</pre>",
        quote=True,
        reply_markup=keyboard,
    )


@app.on_callback_query(filters.regex("figlet"))
async def figlet_handler(Client, query: CallbackQuery):
    try:
        kul_text, keyboard = figle(text)
        await query.message.edit_text(
            f"here is your figlet :\n<pre>{kul_text}</pre>", reply_markup=keyboard
        )
    except FloodWait as e:
        await asyncio.sleep(e.value)

    except Exception as e:
        return await query.answer(e, show_alert=True)

__MODULE__ = "Figlet"
__HELP__ = """<blockquote><b>
**figlet**

• /figlet <text> - creates a figlet of the given text.</b></blockquote>
"""
