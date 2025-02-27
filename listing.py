import telebot
import requests
import json
from telebot import types



bot = telebot.TeleBot('BOT-TOKEN')



# USD
url_usd = 'https://api.nbrb.by/exrates/rates/USD?parammode=2'
# EUR
url_eur = 'https://api.nbrb.by/exrates/rates/EUR?parammode=2'
# RUB
url_rub = 'https://api.nbrb.by/exrates/rates/RUB?parammode=2'

r_usd = requests.get(url_usd)
r_eur = requests.get(url_eur)
r_rub = requests.get(url_rub)


obj_usd = json.loads(r_usd.text)
obj_eur = json.loads(r_eur.text)
obj_rub = json.loads(r_rub.text)

s = obj_usd["Date"]


@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Курсы валют")
    markup.add(btn1)
    bot.send_message(message.from_user.id, '👋 Привет! Я твой бот-помощник! Я получаю курсы валют с НБРБ', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Курсы валют':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Курсы валют')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Курсы валют в Беларуси на ' + str(s[0:10])+'\n'+'\n'+'$ USD: '+str(obj_usd["Cur_OfficialRate"])+' за 1 USD'+'\n'+'€ EUR: '+str(obj_eur["Cur_OfficialRate"])+' за 1 EUR'+'\n'+'₽ RUB: '+str(obj_rub["Cur_OfficialRate"])+' за 100 RUB' , reply_markup=markup) #ответ бота

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Курсы валют')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Курсы валют в Беларуси на ' + str(s[0:10])+'\n'+'\n'+'$ USD: '+str(obj_usd["Cur_OfficialRate"])+' за 1 USD'+'\n'+'€ EUR: '+str(obj_eur["Cur_OfficialRate"])+' за 1 EUR'+'\n'+'₽ RUB: '+str(obj_rub["Cur_OfficialRate"])+' за 100 RUB' , reply_markup=markup) #ответ бота


bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть
