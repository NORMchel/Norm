from .. import loader, utils

class HacksssMod(loader.Module):
    strings = {"name": "NORMmeme"}
    async def HackCatcmd(self, message):
        await message.edit("Вы взломали котика")
      
