import telebot

BOT_TOKEN = "7454419772:AAGARFKf64_1kNvGUOuNkV77QjaYxZCbHZ4"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать в магазин FBaking_team!")

bot.infinity_polling()
