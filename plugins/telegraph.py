import os

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegraph import upload_file

from DanteMusic import app
from TheApi import api


@app.on_message(filters.command(["tgm", "tgt", "telegraph", "tl"]))
async def get_link_group(client, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "please reply to a media to upload on telegraph"
        )

    media = message.reply_to_message
    file_size = 0
    if media.photo:
        file_size = media.photo.file_size
    elif media.video:
        file_size = media.video.file_size
    elif media.document:
        file_size = media.document.file_size

    if file_size > 15 * 1024 * 1024:
        return await message.reply_text("do not use high size.")

    try:
        text = await message.reply("proses...")

        async def progress(current, total):
            try:
                await text.edit_text(f"📥 Downloads... {current * 100 / total:.1f}%")
            except Exception:
                pass

        try:
            local_path = await media.download(progress=progress)
            await text.edit_text("📤 Uploads...")

            upload_path = api.upload_image(local_path)

            await text.edit_text(
                f"🌐 | [COPY LINK]({upload_path})",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "Upload File",
                                url=upload_path,
                            )
                        ]
                    ]
                ),
            )

            try:
                os.remove(local_path)
            except Exception:
                pass

        except Exception as e:
            await text.edit_text(f"❌ failed to upload file\n\n<i>use media not text!: {e}</i>")
            try:
                os.remove(local_path)
            except Exception:
                pass
            return
    except Exception:
        pass

__HELP__ = """<blockquote><b>
**telegraph upload bot commands**

use these commands to upload media to telegraph:

- `/tgm`: upload replied media to telegraph.
- `/tgt`: same as `/tgm`.
- `/telegraph`: same as `/tgm`.
- `/tl`: same as `/tgm`.

**example:**
- reply to a photo or video with `/tgm` to upload it.

**note:**
you must reply to a media file for the upload to work.</b></blockquote>
"""

__MODULE__ = "Link"
