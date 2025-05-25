from pyrogram import __version__
from bot import Bot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import PRICE1, PRICE2, PRICE3, PRICE4, PRICE5, UPI_ID, UPI_IMAGE_URL, SCREENSHOT_URL

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data

    if data == "about":
        await query.message.edit_text(
            text = f'<b>○ Language : <a href="https://t.me/hiddenlust7">Python</a></b> 🐍\n'
                   f'<b>○ Version : v{__version__} 🫏</b>\n'
                   f'<b>○ Developer : <b> kya krega😼</b>',
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("🔒 Close", callback_data="close")]]
            )
        )

    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

    elif data == "buy_prem":
        await query.message.edit_text(
            text = (f"👋 {query.from_user.username}\n\n🎖️ Available Plans :\n\n"
                    f"● {PRICE1} rs For 7 Days Prime Membership\n"
                    f"● {PRICE2} rs For 1 Month Prime Membership\n"
                    f"● {PRICE3} rs For 3 Months Prime Membership\n"
                    f"● {PRICE4} rs For 6 Months Prime Membership\n"
                    f"● {PRICE5} rs For 1 Year Prime Membership\n\n"
                    f"💵 UPI ID - <code>{UPI_ID}</code>\n\n"
                    f"📸 QR - <a href='{UPI_IMAGE_URL}'>Click Here to Scan</a>\n\n"
                    "♻️ If payment is not getting sent on above given QR code then inform admin, he will give you new QR code\n\n"
                    "‼️ Must Send Screenshot after payment"),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Send Payment Screenshot (ADMIN) 📸", url=SCREENSHOT_URL)],
                    [InlineKeyboardButton("🔒 Close", callback_data="close")]
                ]
            )
                                         )
