import telebot
from telebot import types
import os
import random
import glob



TOKEN = "5051483690:AAH3bPHJAqShgDhDeLmjzkbeYxU2tk8vsqQ"

bot = telebot.TeleBot(TOKEN)

#@bot.message_handler(content_types=['text'])
@bot.message_handler(commands=['start'])
def start_command(message):
#def start_message(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет, если ты тут, значит что-то случилось, напиши комманду /help")

@bot.message_handler(commands=['help'])
def help_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Пикчи', callback_data='Пикчи')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Сообщения', callback_data='Сообщения')
    )

    bot.send_message(
        message.chat.id,
        'Выбери, что на данный момент тебе нужно:',
        reply_markup=keyboard
    )
photo=open('Photo/' + random.choice(os.listdir('Photo')), 'rb')
@bot.callback_query_handler(func=lambda call: True)
# Создаём функцию
def callback_inline(call):
    if call.message:
        # Если значение кнопки равно одному то
        if call.data == "Пикчи":
            photo=open('Photo/' + random.choice(os.listdir('Photo')), 'rb')
            bot.send_photo(call.message.chat.id, photo)
        elif call.data=='Сообщения':
            f=open('hor.txt', 'r', encoding='UTF-8')
            g=f.read().split('\n')
            f.close()
            a=random.choice(g)
            bot.send_message(call.message.chat.id, a)

bot.polling(none_stop=True, interval=0)