import random
from .. import loader, utils
from datetime import timedelta
from telethon import functions
from telethon.tl.types import Message


@loader.tds
class Rand(loader.Module):
    strings = {"name": "NORMrand"}
    async def randcmd(self, message):
        args = utils.get_args(message)
        count = int(args[0].strip())
        count1 = int(args[1].strip())
        count2 = count1 + 1
        result = random(count, count2)
        await message.edit("Ваше рандомное число:", result)
