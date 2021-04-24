"""Restart or Terminate the bot from any chat
Available Commands:
.restart
.shutdown"""
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html
import os
import sys

from Archxbot import CMD_HELP
from Archxbot.utils import Archx_on_cmd


@Archx.on(Archx_on_cmd("restart"))
async def _(event):
    if event.fwd_from:
        return
    # await asyncio.sleep(2)
    # await event.edit("Restarting [██░] ...\n`.ping` me or `.help` to check if I am online after a lil bit.")
    # await asyncio.sleep(2)
    # await event.edit("Restarting [███]...\n`.ping` me or `.help` to check if I am online after a lil bit.")
    # await asyncio.sleep(2)
    await event.edit("`Restarted.`\nketik `.ping` setelah 5 menit untuk memeriksa kembali.")
    await borg.disconnect()
    # https://archive.is/im3rt
    os.execl(sys.executable, sys.executable, *sys.argv)
    # You probably don't need it but whatever
    quit()


@Archx.on(Archx_on_cmd("shutdown"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Turning off ...Hidupkan saya secara manual nanti.")
    await borg.disconnect()


CMD_HELP.update(
    {
        "power_tools": "**Power Tools**\
\n\n**Syntax : **`.restart`\
\n**Usage :** restarts your Friday userbot.\
\n\n**Syntax : **`.shutdown`\
\n**Usage :** Shuts down your Friday userbot."
    }
)
