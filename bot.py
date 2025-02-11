from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, WebAppInfo

TOKEN = "7068865561:AAF_blTEFHWFsneZlR3FESrl4QWDtTnFPaY"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="🎮 Играть", web_app=WebAppInfo(url="https://yourwebsite.com")))
    await message.answer("Добро пожаловать в FPI Clicker!", reply_markup=keyboard)

if __name__ == "__main__":
    from aiogram import executor
    executor.start_polling(dp)
