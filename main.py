import logging
from aiogram import Bot, Dispatcher, executor, types
from googletrans import Translator
from dictionary import getDefinition
import requests

API_TOKEN = '6376425254:AAErZnHK7dnn_d5BfXBf0Hid1un6Y7Ty5Qc'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm translator bot!\nPowered by aiogram.")

@dp.message_handler()
async def tarjimon(message: types.Message):
    lang = Translator().detect(message.text).lang
    if len(message.text.split()) > 2:
        dest = 'uz' if lang == 'en' else 'en'
        await message.reply(translator.translate(message.text, dest).text)
    else:
        if lang=='en':
            word_id = message.text
        else:
            word_id = translator.translate(message.text, dest='en').text

        lookup = getDefinition(word_id)
        if lookup:
            await message.reply(f"Word: {word_id} \n Definition:\n{lookup['definition']}")
            if lookup.get('audio'):
                for i in lookup['audio']:
                    await message.reply(i)
        else:
            await message.reply("Bunday so'z topilmadi.")
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
