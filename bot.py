import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '2140974579:AAHLVKtzqO6CKpCZUV8dhBqw6msxexMQ4DY'
wikipedia.set_lang('uz')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.answer("Assalomu Aleykum. Wikipedia botga xush kelibsiz!")


@dp.message_handler()
async def answerWiki(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    try:
        javob=wikipedia.summary(message.text)
        await message.answer(javob)
    except:
        await  message.answer("Bunday ma'lumot topilmadi.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)