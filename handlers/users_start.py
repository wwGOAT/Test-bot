from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from loader import dp, db


class RegisterState(StatesGroup):
    phone_number = State()
    location = State()
    get_location = State()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if await db.get_user_by_chat_id(chat_id=message):
        text = "Nma gap"
        await message.answer(text=text)
    else:
        text = "Assalomu alaykum, ismingizni kiriting"
        await message.answer(text=text)
        await RegisterState.phone_number.set()


@dp.message_handler(state=RegisterState.phone_number)
async def get_phone_number(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    text = "Telefon Raqam"
    await message.answer(text=text)
    await RegisterState.location.set()


@dp.message_handler(state=RegisterState.location)
async def get_location(message: types.Message, state: FSMContext):
    await state.update_data(location=message.text)
    text = "Manzilni kiriting"
    await message.answer(text=text)
    await RegisterState.get_location.set()


@dp.message_handler(state=RegisterState.get_location)
async def get_location_final(message: types.Message, state: FSMContext):
    await state.update_data(location=message.text)

    data = await state.get_data()
    if db.add_user(data):
        text = "Muvoffaqiyatli yakunlandi"
    else:
        text = "Xato"
    await message.answer(text=text)
    await state.finish()