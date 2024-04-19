from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


user_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Rasmlar"),
            KeyboardButton(text="Rasm joylash"),
        ]
    ], resize_keyboard=True
)

phone_number_share = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Telefon raqam jo'natish", request_contact=True)
        ]
    ]
)

location_share = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Manzilni jo'natish", request_location=True)
        ]
    ]
)