from pyrogram import Client, filters
from config import Config
import keyboards as kb

app = Client("temp_mail_bot", api_id=Config.API_ID, api_hash=Config.API_HASH, bot_token=Config.BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start_cmd(client, message):
    text = (
        "**👋 👋 VANKKAM! TEMP MAIL PRO-VIRKU VARAVEK KIROM.**\n\n"
        "**📧 CURRENT MAIL:** `NONE`\n"
        "**👑 STATUS:** **FREE USER**\n\n"
        "**BELOW BUTTONS-AH PAYANPADUTHI MAIL-AH MANAGE PANNAVUM.**"
    )
    await message.reply_text(text, reply_markup=kb.main_menu())

@app.on_callback_query()
async def handle_callback(client, cb):
    if cb.data == "start_back":
        await cb.edit_message_text(
            "**👋 👋 VANKKAM! TEMP MAIL PRO-VIRKU VARAVEK KIROM.**\n\n"
            "**📧 CURRENT MAIL:** `NONE`\n"
            "**👑 STATUS:** **FREE USER**",
            reply_markup=kb.main_menu()
        )

    elif cb.data == "premium_plans":
        await cb.edit_message_text(
            "**💎 PREMIUM PLANS SELECT PANNAVUM:**\n\n"
            "**✅ CUSTOM DOMAIN**\n"
            "**✅ PERMANENT MAIL**\n"
            "**✅ SEND MESSAGE FEATURE**\n"
            "**✅ MANUAL DELETE OPTION**",
            reply_markup=kb.premium_menu()
        )

    elif cb.data.startswith("pay_"):
        amount = cb.data.split("_")[1]
        payment_text = (
            f"**💳 PAYMENT FOR ₹{amount}**\n\n"
            f"**UPI ID:** `{Config.UPI_ID}`\n\n"
            "**QR CODE-AH SCAN PANNI PAY PANNAVUM. PAYMENT MUDINTHATHUM SCREENSHOT-AH ADMIN-KU ANUPPAVUM.**"
        )
        # Inga Edit panni QR image anuppalam illa text-ah edit pannalam
        await cb.edit_message_text(payment_text, reply_markup=kb.premium_menu())

app.run()
      
