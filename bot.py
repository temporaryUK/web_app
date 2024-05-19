import asyncio


from aiogram import Router, Bot, Dispatcher
from aiogram.types import Message, WebAppInfo
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config.py import BOT_TOKEN
from app_battles import ft, main as flet_main


def webapp_builder() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button(
        text='Click', web_app=WebAppInfo(url='https://1315-5-142-110-50.ngrok-free.app')
    )
    return builder.as_markup()


router = Router()


@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.reply('Click!', reply_markup=webapp_builder())


async def main_bot() -> None:
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)

    await bot.delete_webhook(True)
    await dp.start_polling(bot)


async def run_bot():
    await main_bot()

if __name__ == '__main__':
    asyncio.run(run_bot())