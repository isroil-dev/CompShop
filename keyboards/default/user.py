from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import types
from loader import db_manager

user_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💻 Compyuterlar"),
            KeyboardButton(text="📍 Manzil")
        ],
        [
            KeyboardButton(text="☎️ Contact"),
            KeyboardButton(text="⚙️ Sozlamalar")
        ],
    ], resize_keyboard=True
)

phone_number_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📞 Share a phone number", request_contact=True),
        ]
    ], resize_keyboard=True
)


async def user_categories_menu_def():
    categories = db_manager.get_all_categories()
    cat_markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    back = KeyboardButton(text="🔙 Back to main menu")
    cat_markup.insert(back)

    for cat in categories:
        button = KeyboardButton(text=cat[1])
        cat_markup.insert(button)

    return cat_markup


async def user_product_inside_menu_def(message: types.Message):
    prdct_name = message.text
    products = db_manager.get_product_by_category(prdct_name)
    product_markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    back = KeyboardButton(text="◀️ Back to categories")
    product_markup.insert(back)

    for cat in products:
        button = KeyboardButton(text=cat[1])
        product_markup.insert(button)

    return product_markup

