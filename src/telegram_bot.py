from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token="6526749723:AAEDtiEKNgwZj4yyFcfUoF8MRbo01OGYQTY")
dp = Dispatcher(bot)

async def start(message: Message):
    update.message.reply_text("Welcome! Please enter the certilogo.")

async def handle_code(message: types.Message):
    auth_code = message.text
    await message.reply(f"Reveived code: {auth_code}")

if __name__ = "__main__":
    executor.start_polling(dp, skip_updates=True)