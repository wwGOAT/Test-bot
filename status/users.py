from aiogram.dispatcher.filters.state import State, StatesGroup


class RegisterUser(StatesGroup):
    fullname = State()
    username = State()
    bio = State()


class Seacrh(StatesGroup):
    username = State()