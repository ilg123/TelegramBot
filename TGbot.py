import asyncio
import os
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
from handlers import GPT, LLmapp
from aiogram.filters.command import Command

FILENAME = "/data/todo.json" if "AMVERA" in os.environ else "todo.json"

logging.basicConfig(level=logging.INFO)


load_dotenv()
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

@dp.message(Command('start')) # Старотовая команда выводит приветвистее и краткая интусркиция
async def start(message: types.Message):
    await message.reply(
        '''Вас приветствует GPT-bot, для взаимодействия с GPT пропишите команду /gpt
Также данный бот умеет работать с файлами .pdf(пока только это) отправьте боту файл(до 20мб)
и пропишите команду /llma  и он ответит на основание этого файла'''
    )

async def main():
    # Майн-фунукция
    dp.include_routers(GPT.router)
    dp.include_router(LLmapp.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

@dp.message(F.document)
async def download_photo(message: types.Message, bot: Bot):
    # Функция для скличвание pdf файлов
    await bot.download(
        message.document,
        destination=f"handlers/data/{message.document.file_id}.pdf"
    )

if __name__ == '__main__':
    asyncio.run(main())

