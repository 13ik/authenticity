import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from src.config import BOT_TOKEN
from src.web_interaction import interact_with_webpage

bot = Bot(token="your_token_bot")
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    await message.reply("Welcome! Please enter the certilogo:")

@dp.message()
async def handle_code(message: Message):
    auth_code = message.text 

    result = await interact_with_webpage(auth_code)
    
    await message.reply(result)

async def on_startup(dp: Dispatcher):
    print("Bot has started")

async def main():
    await bot.delete_webhook()
    await dp.start_polling(bot, on_startup=on_startup)

if __name__ == "__main__":
    asyncio.run(main())
