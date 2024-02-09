import telebot
import config
import random
import message_generator

TOKEN = config.TELEGRAM_BOT_TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def echo_all(message):
    text = message.text.strip().lower()
    if 'лида' in text or '?' in text or random.randint(1, 2) == 1:
        try:
            text = message_generator.message_genarator(message.text, mode=1)
        except:
            text = message_generator.message_genarator(message.text, mode=0)
        print(text)
        bot.send_message(message.chat.id, text)


if __name__ == "__main__":
    bot.infinity_polling()
