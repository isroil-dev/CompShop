from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from keyboards.default.admin import *
from keyboards.inline.admin import admin_category_update_keyboards
from loader import dp


@dp.message_handler(CommandStart(), chat_id=ADMINS)
async def bot_start(message: types.Message):
    text = "Hi again Sir!"
    await message.answer(text=text, reply_markup=admin_main_menu)


@dp.message_handler(text='Products 💻', chat_id=ADMINS, state="*")
async def bot_start(message: types.Message):
    text = "Choose one"
    await message.answer(text=text, reply_markup=product_info)


@dp.message_handler(text="Category", chat_id=ADMINS, state="*")
async def admin_category_handler(message: types.Message, state: FSMContext):
    await state.set_state('admin-category-inside')
    text = "Welcome to categories menu"
    await message.answer(text=text, reply_markup=await admin_category_inside_menu_def())


@dp.message_handler(text="➕ Add Category", chat_id=ADMINS, state="admin-category-inside")
async def admin_category_handler(message: types.Message, state: FSMContext):
    text = "Enter name to new category."
    await message.answer(text=text)
    await state.set_state('admin-add-category-state')


@dp.message_handler(state="admin-add-category-state", chat_id=ADMINS)
async def admin_category_handler(message: types.Message, state: FSMContext):
    if db_manager.add_category(message.text):
        text = "Category is added ✅"
    else:
        text = "Bot has some problems ❌"

    await message.answer(text=text, reply_markup=await admin_category_inside_menu_def())
    await state.set_state('admin-category-inside')


@dp.message_handler(state="admin-category-inside", chat_id=ADMINS)
async def admin_category_handler(message: types.Message, state: FSMContext):
    name = message.text
    category = db_manager.get_category_by_name(name)

    if category:
        total = len(db_manager.get_products_by_cat_id(category[0]))
        text = f"Name: {category[1]}\nTotal Products: {total}"
        await message.answer(text=text, reply_markup=await admin_category_update_keyboards(category))
