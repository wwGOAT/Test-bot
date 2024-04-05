from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

about_profile = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton('About'), KeyboardButton('Followers')]
],
    resize_keyboard=True,
    one_time_keyboard=True

)

back = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton('Orqaga qaytish')]
],
resize_keyboard=True,
one_time_keyboard=True
)