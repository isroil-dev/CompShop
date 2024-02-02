from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.user import *
from loader import dp


@dp.message_handler(text="🔙 Back to main menu", state="*")
async def admin_product_handler(message: types.Message, state: FSMContext):
    text = "⏪ You go back to the main menu"
    await message.answer(text=text, reply_markup=user_main_menu)
    await state.finish()


@dp.message_handler(text="◀️ Back to categories", state="*")
async def admin_product_handler(message: types.Message, state: FSMContext):
    text = "⏪ You go back to the categories"
    await message.answer(text=text, reply_markup=await user_categories_menu_def())
    await state.set_state("user-category-inside")
