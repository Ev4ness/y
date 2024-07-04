import io

from gtts import gTTS
from pyrogram import filters

from DanteMusic import app


@app.on_message(filters.command("tts"))
async def text_to_speech(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "Please provide some text to convert to speech."
        )

    text = message.text.split(None, 1)[1]
    tts = gTTS(text, lang="hi")
    audio_data = io.BytesIO()
    tts.write_to_fp(audio_data)
    audio_data.seek(0)

    audio_file = io.BytesIO(audio_data.read())
    audio_file.name = "audio.mp3"
    await message.reply_audio(audio_file)

__HELP__ = """<blockquote><b>
**text to speech bot command**

use the `/tts` command to convert text into speech.

- `/tts <text>`: converts the given text to speech in hindi.

**example:**
- `/tts `

**note:**
make sure to provide some text after the `/tts` command.</b></blockquote>
"""

__MODULE__ = "Tts"
