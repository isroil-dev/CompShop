from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove

from data.config import ADMINS
from keyboards.default.admin import *
from keyboards.inline.admin import *
from loader import dp, db_manager
from states.states import ProductState


@dp.message_handler(text='Product')
async def bot_start(message: types.Message, state: FSMContext):
    await state.set_state('admin-product-inside')
    text = "You are in product"
    await message.answer(text=text, reply_markup=await admin_product_inside_menu_def())


@dp.message_handler(text='➕ Add Product', chat_id=ADMINS, state="admin-product-inside")
async def user_ctry_handler(message: types.Message, state: FSMContext):
    text = "Name your product"
    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
    await ProductState.name.set()


@dp.message_handler(state=ProductState.name)
async def user_ctry_handler(message: types.Message, state: FSMContext):
    await state.update_data({
        "name": message.text
    })
    text = "Give a price for your product"
    await message.answer(text=text)
    await ProductState.price.set()


@dp.message_handler(state=ProductState.price)
async def user_ctry_handler(message: types.Message, state: FSMContext):
    await state.update_data({
        "price": message.text
    })
    text = "Send a photo of your product"
    await message.answer(text=text)
    await ProductState.photo.set()


@dp.message_handler(state=ProductState.photo, content_types=types.ContentType.PHOTO)
async def user_ctry_handler(message: types.Message, state: FSMContext):
    await state.update_data({
        "photo": message.photo[-1].file_id
    })
    text = "Write about your product"
    await message.answer(text=text)
    await ProductState.about.set()


@dp.message_handler(chat_id=ADMINS, state=ProductState.about)
async def user_ctry_handler(message: types.Message, state: FSMContext):
    await state.update_data({
        "about": message.text
    })
    text = "Add category of your product"
    await message.answer(text=text, reply_markup=await admin_categories_menu_def())
    await ProductState.category.set()


@dp.message_handler(chat_id=ADMINS, state=ProductState.category)
async def user_ctry_handler(message: types.Message, state: FSMContext):
    await state.update_data(category=message.text, status=1, created_at=message.date)
    data = await state.get_data()
    if db_manager.add_product(data):
        text = "Successfully added ✅"
    else:
        text = "."
    await message.answer(text=text, reply_markup=await admin_product_inside_menu_def())


@dp.message_handler(state="admin-product-inside", chat_id=ADMINS)
async def admin_category_handler(message: types.Message, state: FSMContext):
    name = message.text
    product = db_manager.get_product_by_name(name)

    if product:
        text = f"""
{product[1]}\n{product[2]} $

{product[4]}
"""
        await message.answer_photo(photo=product[3], caption=text,
                                   reply_markup=await admin_product_update_keyboards(product))
