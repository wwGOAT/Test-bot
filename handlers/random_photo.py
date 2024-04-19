from aiogram.dispatcher import FSMContext

from keyboard.inline.user import user_like_button_def
from loader import dp, db
from aiogram import types


@dp.message_handler(text="Rasmlar")
async def get_random_photo_handler(message: types.Message, state: FSMContext):
    photo = db.get_random_photo(message.chat.id)
    if photo is False:
        text = "Hamma rasmlarni ko'rib bo'ldingiz"
        await message.answer(text=text)
    else:
        if photo:
            await state.update_data(photo_id=photo[0])
            likes, dislikes = db.get_photo_likes(photo_id=photo[0])
            likes = likes[0][0]
            dislikes = dislikes[0][0]
            await message.answer_photo(photo=photo[2], reply_markup=await user_like_button_def(likes, dislikes, photo[0]))
        else:
            text = "Aktiv rasm mavjud emas"
            await message.answer(text=text)