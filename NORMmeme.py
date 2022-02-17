from .. import loader, utils

class HacksssMod(loader.Module):
    strings = {"name": "NORMmeme"}
    async def sudo hack catcmd(self, message):
        await message.edit("Вы взломали котика")
        await asyncio.sleep(3)
        await message.edit("Вы взломали котика...")
        await asyncio.sleep(6)
        await message.edit("Вы взломали котика... зачем..")
