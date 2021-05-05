from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


choose_theme = ReplyKeyboardMarkup(resize_keyboard=True)
choose_theme.row(KeyboardButton('Наруто 🍥'), KeyboardButton('Атака Титанов 👣'), KeyboardButton('Токийский Гуль ☕'))