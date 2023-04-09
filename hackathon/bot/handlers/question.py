from aiogram import types
from aiogram.dispatcher import FSMContext
from django.contrib.auth.models import User
from django.db.models import Q
from home.models import Question, Comment
from ai.apps import AiConfig
from bot.apps import BotConfig

bot = BotConfig.bot
dp = BotConfig.dp
co = AiConfig.co
openai = AiConfig.openai


@dp.message_handler()
async def ask_question(message: types.Message, state: FSMContext):
    user = User.objects.filter(Q(username=message.from_user.username) | Q(username=message.from_user.id)).first()
    question = Question.objects.create(
        author=user,
        title=message.text
    )
    response = co.generate(
        model='command-xlarge-nightly',
        prompt=message.text,
        max_tokens=40,
        temperature=0.6,
        stop_sequences=["--"])
    # response = openai.Completion.create(engine='text-davinci-003', prompt=message.text, max_tokens=5)
    answer = response.generations[0].text
    Comment.objects.create(
        author=user,
        question=question,
        description=answer
    )
    await message.answer(answer)
