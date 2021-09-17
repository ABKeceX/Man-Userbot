# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

import asyncio

from userbot import ALIVE_NAME, CMD_HELP, ICON_HELP
from userbot.events import register

modules = CMD_HELP


@register(outgoing=True, pattern=r"^\.help(?: |$)(.*)")
async def help(event):
    """For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("**Masukan Perintah yang Bener Goblokkkk!!**")
            await asyncio.sleep(15)
            await event.delete()
    else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += f"`\t\t{ICON_HELP}\t\t"
        await event.edit(
            f"**乂 Daftar Perintah Untuk Cok-Userbot:**\n"
            f"**乂 Jumlah** `{len(modules)}` **Modules**\n"
            f"**乂 Owner:** `{ALIVE_NAME}`\n\n"
            f"{ICON_HELP}  {string}"
            "\n\nFor Support [𝐓𝐡𝐢𝐬 𝐏𝐞𝐫𝐬𝐨𝐧](https://t.me/yangmutebabi)"
        )
        await event.reply(
            "\n**Contoh Ketik** `.help afk` **Untuk Melihat Informasi Module**"
        )
