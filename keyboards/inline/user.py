from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

user_basket_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✔️ Zakaz berish", callback_data="order_basket"),
        ]
    ]
)