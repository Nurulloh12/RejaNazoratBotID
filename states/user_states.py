from aiogram.fsm.state import State, StatesGroup

class UserSettingsState(StatesGroup):
    wake_time = State()
    review_time = State()
    category = State()