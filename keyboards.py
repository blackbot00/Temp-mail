from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu(has_mail=False, is_premium=False):
    buttons = []
    
    # Mail row
    if not has_mail:
        buttons.append([InlineKeyboardButton("🆕 **CREATE MAIL**", callback_data="gen_mail")])
    else:
        buttons.append([InlineKeyboardButton("🗑️ **DELETE MAIL**", callback_data="del_mail")])
    
    # Premium & Features row
    buttons.append([InlineKeyboardButton("💎 **BUY PREMIUM**", callback_data="premium_plans")])
    
    if is_premium:
        buttons.append([InlineKeyboardButton("📤 **SEND MESSAGE**", callback_data="send_mail")])
    
    return InlineKeyboardMarkup(buttons)

def premium_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🗓️ **1 WEEK - ₹29**", callback_data="pay_29")],
        [InlineKeyboardButton("📅 **1 MONTH - ₹49**", callback_data="pay_49")],
        [InlineKeyboardButton("🏆 **3 MONTHS - ₹79**", callback_data="pay_79")],
        [InlineKeyboardButton("🔙 **BACK**", callback_data="start_back")]
    ])
  
