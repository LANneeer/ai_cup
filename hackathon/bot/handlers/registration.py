from aiogram import types
from aiogram.dispatcher import FSMContext
from django.contrib.auth.models import User
from django.db.models import Q
from bot.apps import BotConfig
from asgiref.sync import sync_to_async

bot = BotConfig.bot
dp = BotConfig.dp


@dp.message_handler(commands='start')
async def hello(message: types.Message, state: FSMContext):
    user = User.objects.filter(Q(username=message.from_user.username) | Q(username=message.from_user.id))
    if user:
        await message.answer(text='<b>Привет! Это бот обсуждения в thread</b>\n'
                                  'Вы можете задать любой вопрос и ИИ на него ответит, а так же можете ответить на вопрос и получить фидбэк от ИИ:\n'
                                  'https://b9f2-89-250-83-36.ngrok-free.app/'
                             )
    else:
        await message.answer(text='<b>Привет! Это бот обсуждения в thread</b>\n'
                                  'Пред использованием бота зарегистрируйтесь написав ваш пароль\n\n'
                                  'Введите пароль для вашего аккаунта:',
                             )
        await state.set_state('password')


@dp.message_handler(state='password')
async def registration(message: types.Message, state: FSMContext):
    await state.finish()
    username = message.from_user.username
    if not username:
        username = message.from_user.id
    User.objects.create(username=username, password=message.text)
    await message.answer(text='<b>Вы успешно зарегистрировались!</b>\n'
                              'Вы можете задать вопрос по вашей услуге или написать этот же вопрос у нас на сайте:\n'
                              'https://b9f2-89-250-83-36.ngrok-free.app/'
                         )
