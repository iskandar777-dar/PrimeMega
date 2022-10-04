from config import EVENT_LOGS
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not EVENT_LOGS:  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member(EVENT_LOGS, msg.from_user.id)
        except UserNotParticipant:
            if EVENT_LOGS.isalpha():
                link = "https://t.me/" + EVENT_LOGS
            else:
                chat_info = await bot.get_chat(EVENT_LOGS)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(photo="https://telegra.ph/file/ba582d379f2586f227d66.png", caption=f"ɢᴀʙᴜɴɢ ɢʀᴜᴘ ᴅɪʙᴀᴡᴀʜ ᴅᴜʟᴜ ʟᴀʟᴜ ᴄᴏʙᴀ /string ʟᴀɢɪ!",
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("➕️ ɢᴀʙᴜɴɢ ɢʀᴜᴘ sɪɴɪ ➕️", url=f"{link}")]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"ᴘʀᴏᴍᴏsɪᴋᴀɴ sᴀʏᴀ sᴇʙᴀɢᴀɪ ᴀᴅᴍɪɴ ᴅɪ MUST_JOIN ᴄʜᴀᴛ : {EVENT_LOGS} !")
