from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import db_manager

admin_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Products 💻"),
            KeyboardButton(text="Zakazlar 🛍")
        ],
    ], resize_keyboard=True
)

product_info = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Category"),
            KeyboardButton(text="Product")
        ],
        [
            KeyboardButton(text="🔙 Back To Main Menu")
        ]
    ], resize_keyboard=True
)


async def admin_category_inside_menu_def():
    categories = db_manager.get_all_categories()
    cat_markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    add_cat = KeyboardButton(text="➕ Add Category")
    back = KeyboardButton(text="🔙 Back")
    cat_markup.insert(add_cat)
    cat_markup.insert(back)

    for cat in categories:
        button = KeyboardButton(text=cat[1])
        cat_markup.insert(button)

    return cat_markup


async def admin_product_inside_menu_def():
    products = db_manager.get_all_product()
    products_markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    add_cat = KeyboardButton(text="➕ Add Product")
    back = KeyboardButton(text="🔙 Back")
    products_markup.insert(add_cat)
    products_markup.insert(back)

    for cat in products:
        button = KeyboardButton(text=cat[1])
        products_markup.insert(button)

    return products_markup


async def admin_categories_menu_def():
    categories = db_manager.get_all_categories()
    cat_markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    for cat in categories:
        button = KeyboardButton(text=cat[1])
        cat_markup.insert(button)

    return cat_markup
