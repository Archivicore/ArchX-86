#    Copyright (C) Midhun KM 2020
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


from Archxbot import ALIVE_NAME
from Archxbot.modules import currentversion

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/d85c7eefaeeea3320818f.jpg"
pm_caption = "**ASSISTANT IS:** [ONLINE](https://t.me/ArchivicoreAssistantBot)\n\n"
pm_caption += "┏━━━━━━━━━━━━━━━━━━━━━━━━\n"
pm_caption += f"┣[ `Whoami: {DEFAULTUSER}`\n"
pm_caption += "┣[ `ArchX-86: @Archivicore`\n"
pm_caption += "┣━━━━━━━━━━━━━━━━━━━━━━━━\n"
pm_caption += "┣[ `Python: 3.9.5`\n"
pm_caption += "┣[ `Telethon Version: 1.21.1` \n"
pm_caption += "┣━━━━━━━━━━━━━━━━━━━━━━━━\n"
pm_caption += f"┣[ **Version** : `{currentversion}`\n"
pm_caption += "┣[ **Database** : `AWS - Working Properly`\n"
pm_caption += "┗━━━━━━━━━━━━━━━━━━━━━━━━\n"

# only Owner Can Use it
@assistant_cmd("alive", is_args=False)
@peru_only
async def Archx(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
