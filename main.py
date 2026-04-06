import telebot
from telebot import types

# زانیارییێن تە یێن فەرمی
API_TOKEN = '8644773541:AAEk0_C9uZQkxYyM6Fmg1vE1WFK80k6cbiU'
MY_ID = '7894920188'

bot = telebot.TeleBot(API_TOKEN)

# دروستکرنا مێنیویا دوگمەیان
def main_menu():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('🐍 وانەیێن پایتۆن')
    btn2 = types.KeyboardButton('🌐 وێبسایتا من')
    btn3 = types.KeyboardButton('👨‍💻 دەربارەی نووح')
    btn4 = types.KeyboardButton('📁 پڕۆژەیێن گێت هەب')
    markup.add(btn1, btn2, btn3, btn4)
    return markup

# فەرمانا دەستپێکێ /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        f"سلاڤ ل تە بیت {message.from_user.first_name} 👋\n\n"
        "بخێر بێی بۆ بۆتێ فەرمی یێ **Cyber Noah**.\n"
        "ئەز یێ ل ڤێرەم دا تە فێری کۆدینگ و پایتۆن بکەم ب زمانێ کوردی."
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=main_menu())

# بەرسڤدان بۆ دوگمەیان
@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    if message.text == '🐍 وانەیێن پایتۆن':
        bot.reply_to(message, "کۆرسێ مە یێ پایتۆن ژ ١٨ وانەیان پێکدهێت. تو دشێی هەمییان د وێبسایتێ مە دا ببینی.")
    
    elif message.text == '🌐 وێبسایتا من':
        bot.reply_to(message, "فەرموو ئەڤە لینکا وێبسایتێ مە یێ فەرمی یە:\nhttps://muusamohammed.github.io/kurdish-dev-hub/")
    
    elif message.text == '👨‍💻 دەربارەی نووح':
        bot.reply_to(message, "ئەز نووح م، گەنجەکێ ١٨ ساڵیم ژ کوردستانێ. ئارمانجا من پێشخستنا جڤاکێ کوردی یە د بوارێ تەکنۆلۆژیایێ دا.")
        
    elif message.text == '📁 پڕۆژەیێن گێت هەب':
        bot.reply_to(message, "تەماشەی کۆدێن من بکە ل سەر GitHub:\nhttps://github.com/muusamohammed")
    
    else:
        bot.reply_to(message, "تکایە ئێک ژ دوگمەیێن خوارێ هەلبژێرە دا هاریکاریا تە بکەم.")

print("بۆتێ نووح نوکە یێ کار دکەت...")
bot.infinity_polling()
