from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove

from data.config import ADMINS
from keyboards.default.admin import *
from loader import dp
from states.states import *


@dp.message_handler(text="🔙 Back To Main Menu", chat_id=ADMINS, state="*")
async def admin_product_handler(message: types.Message, state: FSMContext):
    text = "Welcome to main menu"
    await message.answer(text=text, reply_markup=admin_main_menu)
    await state.finish()


@dp.message_handler(text="🔙 Back", chat_id=ADMINS, state="*")
async def admin_product_handler(message: types.Message, state: FSMContext):
    text = "Welcome to Products menu"
    await message.answer(text=text, reply_markup=product_info)
    await state.finish()
