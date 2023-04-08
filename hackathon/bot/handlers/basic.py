import aiohttp

from aiogram import types
from aiogram.dispatcher.webhook import SendMessage
from bot.apps import BotConfig

bot = BotConfig.bot
dp = BotConfig.dp


@dp.message_handler()
async def echo(message: types.Message):
    # Regular request
    # await bot.send_message(message.chat.id, message.text)
    # or reply INTO webhook
    return SendMessage(message.chat.id, message.text)


