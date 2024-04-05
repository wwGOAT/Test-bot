from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboard.default import default
from status.users import RegisterUser, Seacrh
from loader import dp, db


@dp.message_handler(commands="start")
async def users_start(message: types.Message):
    if db.chat_id_cheakc(chat_id=message.chat.id):
        await message.answer("Assalomu alaykum xush kelibsiz !!", reply_markup=default.about_profile)

        @dp.message_handler(text="Orqaga qaytish")
        async def back(message: types.Message):
            await users_start(message)


        @dp.message_handler(text="About")
        async def about(message: types.Message):
            a = db.get_users_data()
            await message.reply(text=f"""
Telegram Username: {message.from_user.username}
Full Name: {a[2]}
Bot Username: {a[3]}
Bio: {a[4]}
            """, reply_markup=default.back)

        @dp.message_handler(commands="search")
        async def search(message: types.Message):
            await message.answer("Qidirmoqchi bolgan odamni Username ni kiriting !!")
            await Seacrh.username.set()


    else:
        await message.answer("Salom alaykum xush kelibsiz Iltimos Ismingizni va Familangizni kiriting!!")
        await RegisterUser.fullname.set()

@dp.message_handler(state=RegisterUser.fullname)
async def get_fullname(message: types.Message, state: FSMContext):
    await state.update_data(fullname=message.text, chat_id=message.chat.id)
    await message.answer("Username ni kiriting !!!")
    await RegisterUser.username.set()


@dp.message_handler(state=RegisterUser.username)
async def get_username(message: types.Message, state: FSMContext):
    await state.update_data(username=message.text)
    await message.answer("Bio ni kiriting !!!")
    await RegisterUser.bio.set()

@dp.message_handler(state=RegisterUser.bio)
async def get_bio(message: types.Message, state: FSMContext):
    await state.update_data(bio=message.text)

    data = await state.get_data()
    print(data)
    if db.add_users(data):
        await message.answer("Muvafaqiatli yakunlandi !!")
    else:
        await message.answer("Xatolik bor !!")
    await state.finish()



@dp.message_handler(state=Seacrh.username)
async def process_search_username(message: types.Message, state: FSMContext):
    username = message.text
    query = f"SELECT * FROM users WHERE username = '{username}'"
    db.cursor.execute(query)
    results = db.cursor.fetchall()
    print(results)
    if results:
        await message.answer(text=f"Bunday User topildi: {results[0][3]}")
    else:
        await message.answer("Bunday user toplimadi kechirasiz !!")
    # Reset the state
    await state.finish()