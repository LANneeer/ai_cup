from django.apps import AppConfig
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging

import os


class BotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bot'
    bot_token = os.getenv('BOT_TOKEN')
    webhook_host = os.getenv('WEBHOOK_HOST')
    webhook_path = os.getenv('WEBHOOK_PATH')
    webhook_url = f'{webhook_host}{webhook_path}'
    webapp_host = 'localhost'
    webapp_port = 3001
    bot = Bot(token=bot_token, parse_mode=types.ParseMode.HTML)
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)


