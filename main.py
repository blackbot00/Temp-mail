import io
import qrcode
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from config import Config

app = Client(
    "temp_mail_pro",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

# --- KEYBOARDS ---

def main_menu_kb(has_mail=False, is_premium=False):
    buttons = []
    
    # Mail Management Row
    if not has_mail:
        buttons.append([InlineKeyboardButton("🆕 **CREATE MAIL**", callback_data="gen_mail")])
    else:
        buttons.append([InlineKeyboardButton("🗑️ **DELETE MAIL**", callback_data="del_mail")])
    
    # Premium Row
    buttons.append([InlineKeyboardButton("💎 **BUY PREMIUM**", callback_data="view_plans")])
    
    # Premium Only Features
    if is_premium:
        buttons.append([InlineKeyboardButton("📤 **SEND MESSAGE**", callback_data="send_mail")])
    
    return InlineKeyboardMarkup(buttons)

def premium_menu_kb():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🗓️ **1 WEEK - ₹29**", callback_data="pay_29")],
        [InlineKeyboardButton("📅 **1 MONTH - ₹49**", callback_data="pay_49")],
        [InlineKeyboardButton("🏆 **3 MONTHS - ₹79**", callback_data="pay_79")],
        [InlineKeyboardButton("🔙 **BACK TO MENU**", callback_data="back_to_main")]
    ])

# --- UTILS ---

def generate_qr(amount):
    upi_link = f"upi://pay?pa={Config.UPI_ID}&pn={Config.MERCHANT_NAME}&am={amount}&cu=INR&tn=Premium_Purchase"
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(upi_link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    return img_byte_arr

# --- HANDLERS ---

@app.on_message(filters.command("start"))
async def start_handler(client, message):
    text = (
        "**👋 👋 VANKKAM! TEMP MAIL PRO-VIRKU VARAVEK KIROM.**\n\n"
        "**📧 CURRENT MAIL:** `NONE`\n"
        "**👑 STATUS:** **FREE USER**\n\n"
        "**BELOW BUTTONS-AH PAYANPADUTHI MAIL-AH MANAGE PANNAVUM.**"
    )
    await message.reply_text(text, reply_markup=main_menu_kb())

@app.on_callback_query()
async def callback_handler(client, cb):
    user_id = cb.from_user.id
    data = cb.data

    if data == "back_to_main":
        await cb.edit_message_text(
            "**👋 👋 VANKKAM! TEMP MAIL PRO-VIRKU VARAVEK KIROM.**\n\n"
            "**📧 CURRENT MAIL:** `NONE`\n"
            "**👑 STATUS:** **FREE USER**",
            reply_markup=main_menu_kb()
        )

    elif data == "view_plans":
        plan_text = (
            "**💎 PREMIUM PLANS SELECTION**\n\n"
            "**✅ CUSTOM DOMAIN ENABLED**\n"
            "**✅ NO AUTO-DELETE (MANUAL)**\n"
            "**✅ SEND REAL EMAILS**\n"
            "**✅ PREMIUM SUPPORT**\n\n"
            "**CHOOSE YOUR PLAN BELOW:**"
        )
        await cb.edit_message_text(plan_text, reply_markup=premium_menu_kb())

    elif data.startswith("pay_"):
        amount = data.split("_")[1]
        await cb.answer("⏳ Generating Dynamic QR...", show_alert=False)
        
        qr_code = generate_qr(amount)
        caption = (
            f"**💳 PREMIUM PAYMENT - ₹{amount}**\n\n"
            f"**UPI ID:** `{Config.UPI_ID}`\n\n"
            "**STEP 1:** ABOVE QR-AH SCAN PANNAVUM.\n"
            "**STEP 2:** PAYMENT MUDITHAVUDAN SCREENSHOT EDUKKAVUM.\n"
            "**STEP 3:** SCREENSHOT-AH ADMIN-KU ANUPPI PREMIUM ACTIVE PANNAVUM.\n\n"
            "**⚠️ NOTE: DYNAMIC QR-IL AMOUNT AUTOMATIC-AGA VARUM.**"
        )
        
        # UI Flow: Delete old message and send photo with new menu
        await cb.message.delete()
        await client.send_photo(
            chat_id=cb.message.chat.id,
            photo=qr_code,
            caption=caption,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 BACK", callback_data="view_plans")]])
        )

    elif data == "gen_mail":
        # Inga unga Mail.tm logic add pannikalam
        await cb.answer("🔄 Generating your mail...", show_alert=True)
        # Dummy Example for UI Flow
        await cb.edit_message_text(
            "**✅ NEW MAIL CREATED!**\n\n"
            "**📧 MAIL:** `testuser77@mail.tm`\n"
            "**⏳ EXPIRES IN:** **10 MINS (FREE)**",
            reply_markup=main_menu_kb(has_mail=True)
        )

    elif data == "del_mail":
        await cb.answer("🗑️ Mail Deleted!", show_alert=True)
        await cb.edit_message_text(
            "**👋 👋 VANKKAM! TEMP MAIL PRO-VIRKU VARAVEK KIROM.**\n\n"
            "**📧 CURRENT MAIL:** `NONE`\n"
            "**👑 STATUS:** **FREE USER**",
            reply_markup=main_menu_kb(has_mail=False)
        )

print("🚀 Bot Started Successfully!")
app.run()
    
