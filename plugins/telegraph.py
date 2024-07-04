import os

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegraph import upload_file

from DanteMusic import app


@app.on_message(filters.command(["tgm", "tgt", "telegraph", "tl"]))
async def get_link_group(client, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "please reply to a media to upload on telegraph"
        )
    try:
        text = await message.reply("processing...")

        async def progress(current, total):
            await text.edit_text(f"📥 downloading... {current * 100 / total:.1f}%")

        try:
            local_path = await message.reply_to_message.download( progress=progress
            )
            await text.edit_text("📤 uploading to telegraph...")
            upload_path = upload_file(local_path)
            await text.edit_text(
                f"🌐 | [telegraph link](https://telegra.ph{upload_path[0]})",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "telegraph link",
                                url=f"https://telegra.ph{upload_path[0]}",
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
            await text.edit_text(f"❌ |file upload failed \n\n<i>reason: {e}</i>")
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
