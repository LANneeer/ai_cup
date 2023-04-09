from aiogram import types
from aiogram.dispatcher import FSMContext
from django.contrib.auth.models import User
from ai.apps import AiConfig
from bot.apps import BotConfig

bot = BotConfig.bot
dp = BotConfig.dp
co = AiConfig.co
openai = AiConfig.openai


@dp.message_handler()
async def ask_question(message: types.Message, state: FSMContext):
    # response = co.generate(
    #     model='multilingual-22-12',
    #     prompt=message.text,
    #     max_tokens=40,
    #     temperature=0.6,
    #     stop_sequences=["--"])
    response = openai.Completion.create(engine='text-davinci-001', prompt=message.text, max_tokens=5)
    # answer = response.generations[0].text
    print(response)
    answer = response.choices
    await message.answer(answer)
