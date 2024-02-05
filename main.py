import telebot
from telebot import types

bot = telebot.TeleBot('6975528056:AAF4pgiATC0a4wmKFhH152azLzojupfpj8c')


@bot.message_handler(content_types=['text'])
def echo_all(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == "__main__":
    bot.infinity_polling()
