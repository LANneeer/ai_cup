import logging
from bot.apps import BotConfig


async def on_startup(dp):
    await BotConfig.bot.set_webhook(BotConfig.webhook_url)
    # insert code here to run it after start


async def on_shutdown(dp):
    logging.warning('Shutting down..')

    # insert code here to run it before shutdown

    # Remove webhook (not acceptable in some cases)
    await BotConfig.bot.delete_webhook()

    # Close DB connection (if used)
    await dp.storage.close()
    await dp.storage.wait_closed()

    logging.warning('Bye!')
