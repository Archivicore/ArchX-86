"""Emoji
Available Commands:
.support
"""


import asyncio

from Archxbot import CMD_HELP
from Archxbot.utils import Archx_on_cmd


@Archx.on(Archx_on_cmd("Archxbot"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 36)
    # input_str = event.pattern_match.group(1)
    # if input_str == "Read This Telegraph Whole info here":
    await event.edit("Thanks")
    animation_chars = [
        "Click here to Go to our Official Website",
        "[Click Here For Guide](https://techwizardent.com/blog/twe_blog_userbot.php)",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])


CMD_HELP.update(
    {
        "Archxbot": "**Archxbot**\
\n\n** Congragulations **\
\n ` You have Successfully installed the Archxbot`\
\n\n Now you can find all new features in Whats New\
\n\n In this Help menu You can find all the available commands with .help\
\n `If you need more plugins contact @Archivicore`\
\n Updates Channel:  @ArchivicoreOfficial\
\n Bot Support: @ArchivicoreOfficial\
\n Developed By: @Starkgang for Humans\
\n Owners: @Midhun_xD , @meisnub , @chsaiujwal, @inuka_asith\
\n `Full Respect to Archx Devs`\
\n\n\n**Try : **`.Archxbot`\
\n**For :** full Archxbot's guide."
    }
)
