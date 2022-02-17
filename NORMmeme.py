from .. import loader, utils

class HacksssMod(loader.Module):
    strings = {"name": "sudo hack cat"}
    async def hackcatcmd(self, message):
        await message.edit("Вы взломали котика")
        await asyncio.sleep(3)
        await message.edit("Вы взломали котика...")
        await asyncio.sleep(3)
        await message.edit("Вы взломали котика... зачем...")
