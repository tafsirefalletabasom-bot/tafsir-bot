import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8928097513:AAH5X_XhBML7rY5hcE9CbGJDN77h5zCxddI"
bot = telebot.TeleBot(TOKEN)

CHANNEL = "https://t.me/tafsire_fale_tabasom"

def menu():
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("☕ فال قهوه", callback_data="coffee"),
        InlineKeyboardButton("🃏 فال تاروت", callback_data="tarot"),
    )
    kb.add(
        InlineKeyboardButton("📖 استخاره با قرآن", callback_data="estekhare"),
        InlineKeyboardButton("💖 سفارش فال شخصی", callback_data="order"),
    )
    kb.add(
        InlineKeyboardButton("📢 کانال تلگرام", url=CHANNEL),
        InlineKeyboardButton("📞 ارتباط با تبسم", callback_data="contact"),
    )
    return kb

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "🌸 به ربات رسمی تفسیر فال تبسم خوش آمدید.\n"
        "یکی از گزینه‌های زیر را انتخاب کنید:",
        reply_markup=menu()
    )

@bot.callback_query_handler(func=lambda c: True)
def callbacks(call):
    texts = {
        "coffee":"☕ بخش فال قهوه به‌زودی فعال می‌شود.",
        "tarot":"🃏 بخش فال تاروت به‌زودی فعال می‌شود.",
        "estekhare":"📖 بخش استخاره به‌زودی فعال می‌شود.",
        "order":"💖 برای سفارش با شماره 09010617614 در واتساپ، روبیکا یا بله در ارتباط باشید.",
        "contact":"📞 واتساپ: 09010617614\nروبیکا: @falle_banooo\nبله: @falle_banooo",
    }
    bot.answer_callback_query(call.id)
    bot.edit_message_text(
        texts.get(call.data,""),
        call.message.chat.id,
        call.message.message_id,
        reply_markup=menu()
    )

bot.infinity_polling()
