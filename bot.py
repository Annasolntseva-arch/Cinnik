import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "8428920702:AAEA-P2xsZ8tRIeVIp7UE3JKKc3St2iZPcg"
API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.reply("Привет, я Циник Pro — твой умный дерзкий ассистент!")


@dp.message_handler()
async def reply(message: types.Message):
    await message.answer("Я уже в разработке. Скоро буду умнее 😉")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
