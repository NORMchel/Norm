from .. import loader, utils

class HacksssMod(loader.Module):
    strings = {"name": "HackCat"}
    async def hackcatcmd(self, message):
        await message.edit("You gay")
