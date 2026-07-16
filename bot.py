import telebot
import os
from flask import Flask

TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@app.route("/")
def home():
    return "ربات تفسیر فال تبسم فعال است."

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        """🌸 سلام، به ربات تفسیر فال تبسم خوش اومدی.

لطفاً یکی از گزینه‌های زیر را انتخاب کن:

☕ فال قهوه
🃏 فال تاروت
📖 استخاره با قرآن
💖 مشاوره اختصاصی"""
    )

if __name__ == "__main__":
    bot.infinity_polling()
