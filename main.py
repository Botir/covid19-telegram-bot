# -*- coding: utf-8 -*-

# Copyright (C) 2020 Botir Ziyatov <botirziyatov@gmail.com>
# This program is free software: you can redistribute it and/or modify

from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from covid19 import Covid19

buttons = ReplyKeyboardMarkup([['Statistika'], ['Dunyo']], resize_keyboard=True)
covid = Covid19()

def start(update, context):
    update.message.reply_html(
        '<b>Assalomu alaykum, {}</b>\n \nMen Koronovirus statistikasi haqida ma`lumot beruvchi botman'.format(update.message.from_user.first_name), reply_markup=buttons)
    return 1

def stats(update, context):
    data = covid.getByCountryCode('UZ')
    update.message.reply_html(
        '🇺🇿 <b>O‘zbekistonda</b>\n \n<b>Yuqtirganlar:</b> {}\n<b>Sog‘ayganlar:</b> {}\n<b>Vafot etganlar:</b> {}'.
            format(
            data['confirmed'],
            data['recovered'],
            data['deaths']), reply_markup=buttons)

def world(update, context):
    data = covid.getLatest()
    update.message.reply_html(
        '🌎 <b>Dunyoda</b>\n \n<b>Yuqtirganlar:</b> {}\n<b>Sog‘ayganlar:</b> {}\n<b>Vafot etganlar:</b> {}'.format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths'])
        ), reply_markup=buttons)

updater = Updater('TOKEN', use_context=True)
conv_handler = ConversationHandler(
    entry_points = [CommandHandler('start', start)],
    states={
        1: [MessageHandler(Filters.regex('^(Statistika)$'), stats),
            MessageHandler(Filters.regex('^(Dunyo)$'), world),
            ]
    },
    fallbacks=[MessageHandler(Filters.text, start)]
)

updater.dispatcher.add_handler(conv_handler)
updater.start_polling()
updater.idle()
