from .. import loader, utils

import logging

from requests import get

import io

@loader.tds

class NORM_screenshotMod(loader.Module):

 """Ссылка для скрина"""

 strings = {

  "name": "Screen"

 }

  

  

 @loader.sudo

 async def NORM_screenshotcmd(self, message):

  reply = None

  link = utils.get_args_raw(message)

  if not link:

   reply = await message.get_reply_message()

   if not reply:

    await message.delete()

    return

   link = reply.raw_text

  await message.edit("<b>📸Фоткаю...</b>")

  url = "https://mini.s-shot.ru/1024x768/JPEG/1024/Z100/?{}"

  file = get(url.format(link))

  file = io.BytesIO(file.content)

  file.name = "webshot.png"

  file.seek(0)

  await message.client.send_file(message.to_id, file, reply_to=reply)

  await message.delete()
