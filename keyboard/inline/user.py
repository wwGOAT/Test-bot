from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

user_like_data = CallbackData('like', 'act', 'photo_id')
user_dislike_data = CallbackData('dislike', 'act', 'photo_id')


async def user_like_button_def(likes, dislikes, photo_id):
    user_like_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f"{likes} 👍",
                                     callback_data=user_like_data.new(act="like", photo_id=photo_id)),
                InlineKeyboardButton(text=f"{dislikes} 👎",
                                     callback_data=user_dislike_data.new(act="dislike", photo_id=photo_id)),
            ]
        ]
    )
    return user_like_button


async def follow_inline_button(chat_id):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f"Follow", callback_data=chat_id)
            ]
        ]
    )
    return markup


async def yes_or_no(chat_id):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f"Ha", callback_data=chat_id),
                InlineKeyboardButton(text=f"Yo'q", callback_data=chat_id),
            ]
        ]
    )
    return markup


contact_admin = CallbackData('reply', 'act', 'chat_id')
async def contact_admin_def(chat_id):
    contact_admin_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Reply", callback_data=contact_admin.new(act="reply", chat_id=chat_id))
            ]
        ]
    )
    return contact_admin_button
