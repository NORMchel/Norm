import random
from .. import loader, utils
from datetime import timedelta
from telethon import functions
from telethon.tl.types import Message


@loader.tds
class Rand(loader.Module):

    def __init__(self):
        self.name = self.strings["name"]

    async def client_ready(self, client, db):
        self.client = client
        self.db = db
        self.myid = (await client.get_me()).id

    async def randcmd(self, message):
        """ все просто пиши так: rand <число1> <число2>
        автор: @nn_michail"""
        args = utils.get_args(message)
        count = int(args[0].strip())
        count1 = int(args[1].strip())
        count2 = count1 + 1
        result = random(count, count2)
        await message.edit("Ваше рандомное число:", result)