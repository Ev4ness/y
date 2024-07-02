from pyrogram import enums, filters

from DanteMusic import app
from DanteMusic.utils.filter import admin_filter

# ------------------------------------------------------------------------------- #


@app.on_message(filters.command("removephoto") & admin_filter)
async def deletechatphoto(_, message):

    chat_id = message.chat.id
    user_id = message.from_user.id
    msg = await message.reply_text("**processing....**")
    admin_check = await app.get_chat_member(chat_id, user_id)
    if message.chat.type == enums.ChatType.PRIVATE:
        await msg.edit("**this command work on groups !**")
    try:
        if admin_check.privileges.can_change_info:
            await app.delete_chat_photo(chat_id)
            await msg.edit(
                "**groups  profile photo removed  !\nby** {}".format(
                    message.from_user.mention
                )
            )
    except:
        await msg.edit(
            "**the user most need change info admin rights to remove group photo !**"
        )


# --------------------------------------------------------------------------------- #


@app.on_message(filters.command("setphoto") & admin_filter)
async def setchatphoto(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    user_id = message.from_user.id
    msg = await message.reply_text("processing...")
    admin_check = await app.get_chat_member(chat_id, user_id)
    if message.chat.type == enums.ChatType.PRIVATE:
        await msg.edit("`this command work on groups !`")
    elif not reply:
        await msg.edit("**reply to a photo or document.**")
    elif reply:
        try:
            if admin_check.privileges.can_change_info:
                photo = await reply.download()
                await message.chat.set_photo(photo=photo)
                await msg.edit_text(
                    "**new group profile photo changed !\nby** {}".format(
                        message.from_user.mention
                    )
                )
            else:
                await msg.edit("**something wrong happened try another photo !**")

        except:
            await msg.edit(
                "**the user most need change info admin rights to change group photo !**"
            )


# --------------------------------------------------------------------------------- #


@app.on_message(filters.command("settitle") & admin_filter)
async def setgrouptitle(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    user_id = message.from_user.id
    msg = await message.reply_text("processing...")
    if message.chat.type == enums.ChatType.PRIVATE:
        await msg.edit("**this command work on groups !**")
    elif reply:
        try:
            title = message.reply_to_message.text
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
                await message.chat.set_title(title)
                await msg.edit(
                    "**new group name changed !\nby** {}".format(
                        message.from_user.mention
                    )
                )
        except AttributeError:
            await msg.edit(
                "the user most need **change info** admin rights to change group title !"
            )
    elif len(message.command) > 1:
        try:
            title = message.text.split(None, 1)[1]
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
                await message.chat.set_title(title)
                await msg.edit(
                    "**new group name changed !\nby** {}".format(
                        message.from_user.mention
                    )
                )
        except AttributeError:
            await msg.edit(
                "**the user most need change info admin rights to change group title !**"
            )

    else:
        await msg.edit(
            "**you need reply to text or give some text to change group title **"
        )


# --------------------------------------------------------------------------------- #


@app.on_message(filters.command(["setdiscription", "setdesc"]) & admin_filter)
async def setg_discription(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    user_id = message.from_user.id
    msg = await message.reply_text("**processing...**")
    if message.chat.type == enums.ChatType.PRIVATE:
        await msg.edit("**this command works on groups!**")
    elif reply:
        try:
            discription = message.reply_to_message.text
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
                await message.chat.set_description(discription)
                await msg.edit(
                    "**new discription of group changed!**\nby {}".format(
                        message.from_user.mention
                    )
                )
        except AttributeError:
            await msg.edit(
                "**the user must have change info admin rights to change group discription!**"
            )
    elif len(message.command) > 1:
        try:
            discription = message.text.split(None, 1)[1]
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
                await message.chat.set_description(discription)
                await msg.edit(
                    "**new discription of group changed!**\nby {}".format(
                        message.from_user.mention
                    )
                )
        except AttributeError:
            await msg.edit(
                "**the user must have change info admin rights to change group discription!**"
            )
    else:
        await msg.edit(
            "**you need to reply to text or give some text to change group discripton!**"
        )