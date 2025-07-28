from aiogram import Bot, F, types, Dispatcher
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.client.default import  DefaultBotProperties
from aiogram.filters import Command
from dotenv import load_dotenv

import aiohttp
import asyncio
import os

from api.binance import aget
import core.texts as text
import core.keyboards as kbitem
load_dotenv()

_TOKEN_ = os.getenv("TOKEN")
_URL_ = os.getenv("URL")

bot = Bot(
    token=_TOKEN_,
    default=DefaultBotProperties(parse_mode="HTML")
)
dp = Dispatcher()

class Input(StatesGroup):
    waiter = State()

@dp.message(Command("start"))
async def _cmd_start_(msg: types.Message):
    uid = msg.from_user.id
    fn = msg.from_user.first_name

    await msg.reply(text.welcome.format(
        FN=fn
    ), reply_markup=kbitem.wkb)

@dp.callback_query(F.data == "_crypto_")
async def _call_crypto_(call: CallbackQuery, state: FSMContext):
    await call.message.reply(text.ask1)
    await state.set_state(Input.waiter)

@dp.message(Input.waiter)
async def _state_process_(msg: types.Message, state: FSMContext):
    state = msg.text
    finall = state.split()

    if len(finall) == 2:
        ans = await aget(finall[0] + finall[1])
        if ans != -1:
            await msg.reply(text.result.format(
                TICK1=finall[0],
                TICK2=finall[1],
                _res_=ans
            ))
        else:
            await msg.reply(text.err2)
    else:
        await msg.reply(text.err)


async def setup():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(setup())
    except  KeyboardInterrupt:
        print("Stopped.")