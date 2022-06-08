# @php_aleks

from .. import loader, utils

from telethon.errors.rpcerrorlist import UsernameOccupiedError

from telethon.tl.functions.account import UpdateProfileRequest, UpdateUsernameRequest

class UserDataMod(loader.Module):

    """Меняем данные аккаунта"""

    strings = {'name': 'UserData'}

    async def namecmd(self, message):

        """Изменить имя"""

        args = utils.get_args_raw(message).split('/')

        if not args:

            return await message.edit('❌ Нет аргументов!')

        if len(args) == 1:

            firstname = args[0]

            lastname = ' '

        elif len(args) == 2:

            firstname = args[0]

            lastname = args[1]

        await message.client(UpdateProfileRequest(first_name=firstname, last_name=lastname))

        await message.edit(f"✅ Данные изменены!\n Имя: {firstname}\n Фамилия: {lastname}")

    async def biocmd(self, message):

        """Изменить био"""

        args = utils.get_args_raw(message)

        if not args:

            return await message.edit('❌ Нет аргументов!')

        if args == "clear":

            await message.client(UpdateProfileRequest(about=""))

            await message.edit(f"🗑 Описание очищено!")

        else:

            await message.client(UpdateProfileRequest(about=args))

            await message.edit(f"✅ Описание изменено!\n 🗒 Описание:\n <code>{args}</code>")

    async def usernamecmd(self, message):

        """Изменить @username"""

        args = utils.get_args_raw(message)

        me = await (message.client.get_me())

        u = me.username

        if u == args:

            return await message.edit('❌  Введён тот же самый юзернейм!')

        if not args:

            return await message.edit('❌ Нет аргументов!')

        try:

            await message.client(UpdateUsernameRequest(args))

            await message.edit(f"✅ Юзернейм изменён на @{args}!")

        except UsernameOccupiedError:

            await message.edit(f"❌ Юзернейм @{args} уже занят!")
