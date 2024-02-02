from aiogram.dispatcher.filters.state import State, StatesGroup


class CategoryState(StatesGroup):
    name = State()


class ProductState(StatesGroup):
    name = State()
    price = State()
    photo = State()
    about = State()
    category = State()


class RegisterState(StatesGroup):
    phone_number = State()
