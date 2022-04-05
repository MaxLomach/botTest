import telebot
from telebot import types

bot = telebot.TeleBot('5237161541:AAH5llNPZkSRWLH0iWBzjiRfc6vX5lmqMYk')

@bot.message_handler(commands=['start'])
def start(message):
  mess = f'Hello,<b> {message.from_user.first_name} {message.from_user.last_name}</b>'
  bot.send_message(message.chat.id, mess, parse_mode='html')


# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#   if message.text == 'Hello':
#     bot.send_message(message.chat.id, 'И тебе привет!', parse_mode='html')
#   elif message.text == 'id':
#     bot.send_message(message.chat.id, f'Твой ID: <b>{message.from_user.id}</b>', parse_mode='html')
#   elif message.text=='photo':
#     photo = open('python/bot/icon.png','rb')
#     bot.send_photo(message.chat.id, photo)
#   else:
#     bot.send_message(message.chat.id, 'Я тебя не понимаю', parse_mode='html')

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
  bot.send_message(message.chat.id, 'Крутое фото!')

@bot.message_handler(commands=['website'])
def website(message):
  markup = types.InlineKeyboardMarkup()
  markup.add(types.InlineKeyboardButton('WebSite', url='https://pypi.org/project/pyTelegramBotAPI/'))
  bot.send_message(message.chat.id, 'WebSite', reply_markup=markup)

@bot.message_handler(commands=['help'])
def website(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)
  website = types.KeyboardButton('WebSite')
  start = types.KeyboardButton('Start')

  markup.add(website, start)
  bot.send_message(message.chat.id,'WebSite', reply_markup=markup)


bot.polling(none_stop = True)