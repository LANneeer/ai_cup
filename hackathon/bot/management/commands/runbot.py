from django.core.management.base import BaseCommand
import django
from aiogram.utils.executor import start_webhook
from bot.handlers import dp
from bot.apps import BotConfig
from bot.management.commands._private import on_startup, on_shutdown
import asyncio
import os


class Command(BaseCommand):
    def handle(self, *args, **options):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hackathon.hackathon.settings')
        os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
        django.setup()
        asyncio.run(
            start_webhook(
                dispatcher=dp,
                webhook_path=BotConfig.webhook_path,
                on_startup=on_startup,
                on_shutdown=on_shutdown,
                skip_updates=True,
                host=BotConfig.webapp_host,
                port=BotConfig.webapp_port,
            )
        )
