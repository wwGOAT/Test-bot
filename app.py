from aiogram import types, Dispatcher
from aiogram.types import Message
from loader import bot, dp, db
import handlers


async def on_startup(dp: Dispatcher):
    db.create_table()


async def on_shutdown(dp: Dispatcher):
    db.session.close()


@dp.message_handler(commands=['start'])
async def start_command(message: Message):
    try:
        # Your command logic here
        await message.answer("Starting...")
    except Exception as e:
        # Handle exceptions here
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    dp.skip_updates = True
    dp.register_message_handler(on_startup, on_shutdown)
