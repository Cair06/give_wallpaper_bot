import config
import logging
import keyboards as kb
from aiogram import Bot, Dispatcher, executor, types


path = r"F:\Python_projects\Telegram\give_wallpaper_bot\img"
#
logging.basicConfig(level=logging.INFO)

#
bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)


#choose walppaper
@dp.message_handler(commands=['wallpaper'])
async def choose_theme_func(message: types.Message):
    #await bot.send_photo(message.chat.id, types.InputFile(f'{path}\{random_filename}'))
    await bot.send_message(message.chat.id, 'Выбери тему обоев: ', reply_markup=kb.choose_theme)

#naruto
@dp.message_handler(lambda message: message.text == 'Наруто 🍥')
async def send_naruto_img(message: types.Message):
    path_naruto = f'{path}\\naruto'
    await bot.send_photo(message.chat.id, types.InputFile(fr'{path_naruto}\\{config.random_file(path_naruto)}'))

#attack on titan
@dp.message_handler(lambda message: message.text == 'Атака Титанов 👣')
async def send_naruto_img(message: types.Message):
    path_attack_on_titan = f'{path}\\attack_on_titan'
    await bot.send_photo(message.chat.id, types.InputFile(fr'{path_attack_on_titan}\\{config.random_file(path_attack_on_titan)}'))

#tokyo ghoul
@dp.message_handler(lambda message: message.text == 'Токийский Гуль ☕')
async def send_naruto_img(message: types.Message):
    path_tokyo_ghoul = f'{path}\\tokyo_ghoul'
    await bot.send_photo(message.chat.id, types.InputFile(fr'{path_tokyo_ghoul}\\{config.random_file(path_tokyo_ghoul)}'))

#
if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)
