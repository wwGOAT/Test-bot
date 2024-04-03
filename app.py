from aiogram import types, executor, Dispatcher
from loader import bot, dp, db
import handlers


async def on_startup(dp: Dispatcher):
    db.create_table()
async def on_shutdown(dp: Dispatcher):
    db.session.close()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
