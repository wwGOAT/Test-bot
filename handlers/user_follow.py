from aiogram.dispatcher import FSMContext

from keyboard.default.user import user_main_menu
from keyboard.inline.user import user_like_button_def, follow_inline_button, yes_or_no
from loader import dp, db, bot
from aiogram import types

from states.user import RegisterState


@dp.message_handler(commands='search')
async def user_search(message: types.Message, state: FSMContext):
    text = "Id ni kirit"
    await message.answer(text=text)
    await state.set_state('user-search')


@dp.message_handler(state="user-search")
async def get_user_by_id(message: types.Message, state: FSMContext):
    user = db.get_user_by_chat_id(chat_id=int(message.text))
    if user:
        text = "Id ni kirit"
        await message.answer(text=text, reply_markup=await follow_inline_button(chat_id=user[1]))
    else:
        text = "User topilmadi"
        await message.answer(text=text)
    await state.finish()


@dp.callback_query_handler()
async def follow_user(call: types.CallbackQuery, state: FSMContext):
    user_chat_id = call.data
    chat_id = call.message.chat.id

    await bot.send_message(chat_id=user_chat_id, text=f"Ushbu foydalanuvchi sizga follow bosdi {chat_id}",
                           reply_markup=await yes_or_no(chat_id))