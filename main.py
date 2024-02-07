import telebot
import config
import random
import message_generator

TOKEN = config.TELEGRAM_BOT_TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def echo_all(message):
    if random.randint(1, 2) == 1:
        text = message_generator.message_genarator()
        print(text)
        bot.send_message(message.chat.id, text)


if __name__ == "__main__":
    bot.infinity_polling()
