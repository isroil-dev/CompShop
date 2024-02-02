from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.user import *
from keyboards.inline.user import *
from loader import dp, db_manager
from states.states import RegisterState


@dp.message_handler(text='💻 Compyuterlar')
async def get_full_name_handler(message: types.Message, state: FSMContext):
    text = "Wellcome"
    await message.answer(text=text, reply_markup=await user_categories_menu_def())
    await state.set_state("user-category-inside")


@dp.message_handler(state='user-category-inside')
async def admin_category_handler(message: types.Message, state: FSMContext):
    text = "Great choice"
    await message.answer(text=text, reply_markup=await user_product_inside_menu_def(message))
    await state.set_state('user-category-prdct-inside')


@dp.message_handler(state="user-category-prdct-inside")
async def user_category_prdct_handler(message: types.Message, state: FSMContext):
    name = message.text
    product = db_manager.get_product_by_name(name)

    if product:
        text = f"""
    {product[1]}\n
{product[2]} $\n
    
{product[4]}
    """
        await message.answer_photo(photo=product[3], caption=text)


@dp.message_handler(text='📍 Manzil')
async def get_full_name_handler(message: types.Message, state: FSMContext):
    photo = "https://yt3.googleusercontent.com/Ixm-wYcgQiMd1DiDAKZSdZ7VRs5fV19jymOBx_V0WOjeB_sLrFGBad3zNYtgkHRW885MUwi83w=s900-c-k-c0x00ffffff-no-rj"
    text = "📍 Bizni manzil. Alisher Navoiy, 37 Tashkent, Uzbekistan"
    await message.answer_photo(photo=photo, caption=text)


@dp.message_handler(text='☎️ Contact')
async def get_full_name_handler(message: types.Message, state: FSMContext):
    photo = "https://yt3.googleusercontent.com/Ixm-wYcgQiMd1DiDAKZSdZ7VRs5fV19jymOBx_V0WOjeB_sLrFGBad3zNYtgkHRW885MUwi83w=s900-c-k-c0x00ffffff-no-rj"
    text = "☎️ Contact: +998 99 999 77 77"
    await message.answer_photo(photo=photo, caption=text)


@dp.message_handler(text='⚙️ Sozlamalar')
async def get_full_name_handler(message: types.Message, state: FSMContext):
    text = f"""
Ism: {message.from_user.full_name}
Username: @{message.from_user.username}
Til: {message.from_user.language_code}
Id: {message.from_user.id}
"""
    await message.answer(text=text)
