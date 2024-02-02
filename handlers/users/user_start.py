from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.user import *
from keyboards.inline.user import *
from loader import dp, db_manager
from states.states import RegisterState


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user = db_manager.get_user(message.chat.id)
    if user:
        text = f"Hello {message.from_user.full_name}"
        await message.answer(text=text, reply_markup=user_main_menu)
    else:
        text = f"Telefon raqamingizni tugmani bosip kiriting"
        await message.answer(text=text, reply_markup=phone_number_keyboard)
        await RegisterState.phone_number.set()


@dp.message_handler(state=RegisterState.phone_number, content_types=types.ContentType.CONTACT)
async def get_full_name_handler(message: types.Message, state: FSMContext):
    await state.update_data({
        "phone_number": message.contact.phone_number,
        "full_name": message.from_user.full_name,
        "telegram_id": message.chat.id
    })
    data = await state.get_data()
    user = db_manager.register_user(data=data)
    if user:
        text = "Siz ro'yxatdan o'tdingiz ✅"
    else:
        text = "Botda muammo mavjud! ❌"
    await message.answer(text=text, reply_markup=user_main_menu)
    await state.finish()

