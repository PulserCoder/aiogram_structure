from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message

from loader import dp


@dp.message_handler(CommandStart(), state='*')
async def start(message: Message) -> None:
    await message.answer('Hi, world!')