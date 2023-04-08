from django.core.management.base import BaseCommand
from aiogram.utils.executor import start_webhook
from bot.handlers import dp
from bot.apps import BotConfig
from bot.management.commands._private import on_startup, on_shutdown
import os


class Command(BaseCommand):
    def handle(self, *args, **options):
        start_webhook(
            dispatcher=dp,
            webhook_path=BotConfig.webhook_path,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            skip_updates=True,
            host=BotConfig.webapp_host,
            port=BotConfig.webapp_port,
        )
