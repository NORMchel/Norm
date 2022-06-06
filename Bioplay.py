from .. import loader, utils

from telethon import events

from telethon.errors.rpcerrorlist import YouBlockedUserError

@loader.tds

class IrisToolsMod(loader.Module):

    """Ирис тулс"""

    

    strings = {

        "name": "IrisTools"

    }

    async def labcmd(self, message):

        """ Смотрим лабу """

        state = ".лаба"

        msg = await utils.answer(message, "<b>Чекаю...</b>")

        chat = "@iris_cm_bot"

        async with message.client.conversation(chat) as conv:

            try:

                response = conv.wait_event(

                    events.NewMessage(incoming=True, from_users=707693258)

                )

                bot_send_message = await message.client.send_message(

                    chat, format(state)

                )

                bot_response = response = await response

            except YouBlockedUserError:

                await utils.answer(message, f"<b>Бот</b> {chat} <b>в черном списке</b>\n Убери из черного списка и попробуй снова!")

                return

            await bot_send_message.delete()

            await utils.answer(msg, response.text)

            await bot_response.delete()

    async def jcmd(self, message):

        """ Смотрим жертв"""

        state = "мои жертвы"

        msg = await utils.answer(message, "<b>Чекаю...</b>")

        chat = "@iris_cm_bot"

        async with message.client.conversation(chat) as conv:

            try:

                response = conv.wait_event(

                    events.NewMessage(incoming=True, from_users=707693258)

                )

                bot_send_message = await message.client.send_message(

                    chat, format(state)

                )

                bot_response = response = await response

            except YouBlockedUserError:

                await utils.answer(message, f"<b>Бот</b> {chat} <b>в черном списке</b>\n Убери из черного списка и попробуй снова!")

                return

            await bot_send_message.delete()

            await utils.answer(msg, response.text)

            await bot_response.delete()

    async def healcmd(self, message):

        """ Покупаем вакцину """

        state = ".купить вакцину"

        msg = await utils.answer(message, "<b>Покупаю.</b>")

        chat = "@iris_cm_bot"

        async with message.client.conversation(chat) as conv:

            try:

                response = conv.wait_event(

                    events.NewMessage(incoming=True, from_users=707693258)

                )

                bot_send_message = await message.client.send_message(

                    chat, format(state)

                )

                bot_response = response = await response

            except YouBlockedUserError:

                await utils.answer(message, f"<b>Бот</b> {chat} <b>в черном списке</b>\n Убери из черного списка и попробуй снова!")

                return

            await bot_send_message.delete()

            await utils.answer(msg, response.text)

            await bot_response.delete()

    async def biotopcmd(self, message):

        """ Смотрим общий биотоп """

        state = "биотоп"

        msg = await utils.answer(message, "<b>Чекаю...</b>")

        chat = "@iris_cm_bot"

        async with message.client.conversation(chat) as conv:

            try:

                response = conv.wait_event(

                    events.NewMessage(incoming=True, from_users=707693258)

                )

                bot_send_message = await message.client.send_message(

                    chat, format(state)

                )

                bot_response = response = await response

            except YouBlockedUserError:

                await utils.answer(message, f"<b>Бот</b> {chat} <b>в черном списке</b>\n Убери из черного списка и попробуй снова!")

                return

            await bot_send_message.delete()

            await utils.answer(msg, response.text)

            await bot_response.delete()
