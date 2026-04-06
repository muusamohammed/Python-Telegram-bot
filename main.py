import telebot
from telebot import types

# توکنێ تە یێ نوو
API_TOKEN = '8736556946:AAHvSvyt6mH8V0LkVNgQ5SEQdD0RYk0dhjc'

bot = telebot.TeleBot(API_TOKEN)

# فەرمانا /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # دروستکرنا دوگمەیێن بن نامەیێ (Inline Keyboard)
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    btn_web = types.InlineKeyboardButton("🌐 وێبسایتێ من", url="https://muusamohammed.github.io/kurdish-dev-hub/")
    btn_github = types.InlineKeyboardButton("📁 GitHub یێ من", url="https://github.com/muusamohammed")
    btn_about = types.InlineKeyboardButton("👨‍💻 دەربارەی نووح", callback_data="about_noah")
    btn_contact = types.InlineKeyboardButton("💬 پەیوەندی", callback_data="contact_me")
    
    markup.add(btn_web, btn_github, btn_about, btn_contact)
    
    welcome_msg = (
        f"سلاڤ {message.from_user.first_name} 👋\n\n"
        "بخێر بێی بۆ بۆتێ فەرمی یێ **Cyber Noah**.\n"
        "ئەز یێ ل ڤێرەم دا تە بەرەڤ جیهانا پرۆگرامینگێ بەم."
    )
    
    bot.send_message(message.chat.id, welcome_msg, reply_markup=markup, parse_mode="Markdown")

# بەرسڤدان دەما کلیک ل سەر دوگمەیان دکەی (Callback Query)
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "about_noah":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "نووح گەنجەکێ ١٨ ساڵە ژ کوردستانێ، ئارمانجا وی ئەوە زانستێ تەکنۆلۆژیایێ ب زمانێ کوردی بەلاڤ بکەت.")
        
    elif call.data == "contact_me":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "بۆ هەر پرسیارەکێ دشێی ل سەر تیکتۆک یان دیسکۆردێ @cyber.noah پەیوەندیێ بکەی.")

# بەرسڤدانا نامەیێن ئاسایی
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "تکایە دوگمەیێن ل سەرێ بکاربینە دا مفا ژ خزمەتێن مە وەربگری.")

print("Cyber Noah Bot is Running...")
bot.infinity_polling()
