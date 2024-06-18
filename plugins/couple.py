import os 
import random
from datetime import datetime 
from telegraph import upload_file
from PIL import Image, ImageDraw
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ChatType
import requests

from YukkiMusic import app
from utils import _get_image, get_couple, save_couple


def dt():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M")
    dt_list = dt_string.split(" ")
    return dt_list

def dt_tom():
    a = (
        str(int(dt()[0].split("/")[0]) + 1)
        + "/"
        + dt()[0].split("/")[1]
        + "/"
        + dt()[0].split("/")[2]
    )
    return a

def download_image(url, path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(path, 'wb') as f:
            f.write(response.content)
    return path

tomorrow = str(dt_tom())
today = str(dt()[0])

@app.on_message(filters.command("couples"))
async def ctest(_, message):
    cid = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply_text("ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴡᴏʀᴋs ɪɴ ɢʀᴏᴜᴘs.")
    try:
        await app.resolve_peer(OWNER_ID[0])
        OWNER = OWNER_ID[0]
    except:
        OWNER = f"tg://openmessage?user_id={OWNER_ID[0]}"

    p1_path = "pfp.png"
    p2_path = "pfp1.png"
    test_image_path = f'test_{cid}.png'
    cppic_path = "cppic.png"

    try:
        is_selected = await get_couple(cid, today)
        if not is_selected:
            msg = await message.reply_text("ɢᴇɴᴇʀᴀᴛɪɴɢ ᴄᴏᴜᴘʟᴇs ɪᴍᴀɢᴇ...")
            # GET LIST OF USERS
            list_of_users = []

            async for i in app.get_chat_members(message.chat.id, limit=50):
                if not i.user.is_bot:
                    list_of_users.append(i.user.id)

            c1_id = random.choice(list_of_users)
            c2_id = random.choice(list_of_users)
            while c1_id == c2_id:
                c1_id = random.choice(list_of_users)

            photo1 = (await app.get_chat(c1_id)).photo
            photo2 = (await app.get_chat(c2_id)).photo

            N1 = (await app.get_users(c1_id)).mention 
            N2 = (await app.get_users(c2_id)).mention

            try:
                p1 = await app.download_media(photo1.big_file_id, file_name=p1_path)
            except Exception:
                p1 = download_image("https://telegra.ph/file/4251fbf7679e36391d2ae.jpg", p1_path)
            try:
                p2 = await app.download_media(photo2.big_file_id, file_name=p2_path)
            except Exception:
                p2 = download_image("https://telegra.ph/file/4251fbf7679e36391d2ae.jpg", p2_path)

            img1 = Image.open(p1)
            img2 = Image.open(p2)

            background_image_path = download_image("https://telegra.ph/file/eaba8a332cf12bdec2f60.jpg", cppic_path)
            img = Image.open(background_image_path)

            img1 = img1.resize((437, 437))
            img2 = img2.resize((437, 437))

            mask = Image.new('L', img1.size, 0)
            draw = ImageDraw.Draw(mask) 
            draw.ellipse((0, 0) + img1.size, fill=255)

            mask1 = Image.new('L', img2.size, 0)
            draw = ImageDraw.Draw(mask1) 
            draw.ellipse((0, 0) + img2.size, fill=255)

            img1.putalpha(mask)
            img2.putalpha(mask1)

            draw = ImageDraw.Draw(img)

            img.paste(img1, (116, 160), img1)
            img.paste(img2, (789, 160), img2)

            img.save(test_image_path)

            TXT = f"""
**ᴛᴏᴅᴀʏ's ᴄᴏᴜᴘʟᴇ ᴏғ ᴛʜᴇ ᴅᴀʏ:

{N1} + {N2} = 💚

ɴᴇxᴛ ᴄᴏᴜᴘʟᴇs ᴡɪʟʟ ʙᴇ sᴇʟᴇᴄᴛᴇᴅ ᴏɴ {tomorrow} !!**
"""

            await message.reply_photo(test_image_path, caption=TXT, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="ᴍʏ ᴄᴜᴛᴇ ᴅᴇᴠᴇʟᴏᴘᴇʀ 🌋", user_id=OWNER)]]),)

            await msg.delete()
            a = upload_file(test_image_path)
            for x in a:
                img_url = "https://graph.org/" + x
                couple = {"c1_id": c1_id, "c2_id": c2_id}
                await save_couple(cid, today, couple, img_url)

        else:
            msg = await message.reply_text("𝐆ᴇᴛᴛɪɴɢ 𝐓ᴏᴅᴀʏ's 𝐂ᴏᴜᴘʟᴇs 𝐈ᴍᴀɢᴇ...")
            b = await _get_image(cid)
            c1_id = int(is_selected["c1_id"])
            c2_id = int(is_selected["c2_id"])
            c1_name = (await app.get_users(c1_id)).first_name
            c2_name = (await app.get_users(c2_id)).first_name

            TXT = f"""
**𝐓ᴏᴅᴀʏ's 𝐒ᴇʟᴇᴄᴛᴇᴅ 𝐂ᴏᴜᴘʟᴇs 🎉 :
➖➖➖➖➖➖➖➖➖➖➖➖
[{c1_name}](tg://openmessage?user_id={c1_id}) + [{c2_name}](tg://openmessage?user_id={c2_id}) = ❣️
➖➖➖➖➖➖➖➖➖➖➖➖
𝐍ᴇxᴛ 𝐂ᴏᴜᴘʟᴇs 𝐖ɪʟʟ 𝐁ᴇ 𝐒ᴇʟᴇᴄᴛᴇᴅ 𝐎ɴ {tomorrow} !!**
"""
            await message.reply_photo(b, caption=TXT,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="ᴍʏ ᴄᴜᴛᴇ ᴅᴇᴠᴇʟᴏᴘᴇʀ 🌋", user_id=OWNER)]]))
            await msg.delete()

    except Exception as e:
        print(str(e))
    finally:
        try:
            os.remove(p1_path)
            os.remove(p2_path)
            os.remove(test_image_path)
            os.remove(cppic_path)
        except Exception as cleanup_error:
            print(f"Error during cleanup: {cleanup_error}")