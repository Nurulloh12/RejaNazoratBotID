from aiogram.fsm.state import StatesGroup, State

class ChannelState(StatesGroup):
    waiting_for_channel_link = State()
