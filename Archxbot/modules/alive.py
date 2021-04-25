"""Check if Archxbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
# CREDITS: @WhySooSerious, @Sur_vivor
import time

from uniborg.util import Archx_on_cmd, sudo_cmd

from Archxbot import ALIVE_NAME, CMD_HELP, Lastupdate
from Archxbot.Configs import Config
from Archxbot.modules import currentversion


# Functions
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - Lastupdate))
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/d85c7eefaeeea3320818f.jpg"
pm_caption = "┏━━━━━━━━━━━━━━━━━━━━━━━━\n"
pm_caption += f"┣[ `Whoami: {DEFAULTUSER}`\n"
pm_caption += "┣[ `ArchX-86: @Archivicore`\n"
pm_caption = "┣━━━━━━━━━━━━━━━━━━━━━━━━\n"
pm_caption += "┣[ `Python: 3.9.5`\n"
pm_caption += "┣[ `Telethon Version: 1.21.1`\n"
pm_caption = "┣━━━━━━━━━━━━━━━━━━━━━━━━ \n"
pm_caption += f"┣[ **Version** : `{currentversion}`\n"
pm_caption += "┣[ **Database** : `AWS - Working Properly`\n\n"
pm_caption = "┗━━━━━━━━━━━━━━━━━━━━━━━━\n"


@Archx.on(Archx_on_cmd(pattern=r"alive"))
@Archx.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def Archx(alive):
    await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


CMD_HELP.update(
    {
        "alive": "**ALive**\
\n\n**Syntax : **`.alive`\
\n**Usage :** Check if UserBot is Alive"
    }
)
