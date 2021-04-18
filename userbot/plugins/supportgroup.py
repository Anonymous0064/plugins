"""
Don't Edit This If you Dont Give Crdeit
(C) @Godhakerzuserbot------------------------------- Written by @hackelite01 -------------------------------------For @Marcususerbot--------------------------
USAGE : Indicates user to Redirect The Support group 
credits 
@Rohithaditya
@Private_45
"""
import asyncio
# (C) @Godhakerzuserbot------------------------------- Written by @hackelite01 -------------------------------------For @Marcususerbot--------------------------
from userbot.utils import admin_cmd
# (C) @Godhakerzuserbot------------------------------- Written by @hackelite01 -------------------------------------For @Marcususerbot--------------------------
@borg.on(admin_cmd("support"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 36)
    # input_str = event.pattern_match.group(1)
    # if input_str == "support":
    await event.edit("for our support group")
    animation_chars = [
        "Click here",
        "[Support Group](https://t.me/Marcususerbot)",
    ]
# (C) @Godhakerzuserbot------------------------------- Written by @hackelite01 -------------------------------------For @Marcususerbot--------------------------
    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
		
# (C) @Godhakerzuserbot------------------------------- Written by @hackelite01 -------------------------------------For @Marcususerbot--------------------------
