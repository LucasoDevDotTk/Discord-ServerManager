"""
MIT License

Copyright (c) 2021 lucaso60
Copyright (c) 2021 LEL Studios
Copyright (c) 2015-2021 Rapptz
Copyright (c) 2021-present Pycord Development

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import discord
from discord.ext import commands
from discord.commands import slash_command

import os
import json
import sys

from modules.functions import time_now, get_dir_config, get_dir_cogs
from modules.get_config_f import get_config
import modules.start

if not os.name == "nt" or os.name == "posix":
    print(
        f"{time_now()} [!] Warning, your operating system have not been tested, and may not be compatible with this program! The program may fail at any time.")
    print(f"{time_now()} [!] If you encounter any issues, please report them to us at GitHub")
    



CONFIG_FOLDER_PATH = get_dir_config(os.path.dirname(__file__))
COG_FOLDER_PATH = get_dir_cogs(os.path.dirname(__file__))

config_data = get_config(CONFIG_FOLDER_PATH)
TOKEN = config_data["Token"]
DEBUG_ID = config_data["Debug_id"]

INTENTS = discord.Intents.default()
INTENTS.members = True

bot = commands.Bot(
    debug_id=DEBUG_ID,
    intents=INTENTS
)


@bot.event
async def on_ready():
    print(f"{time_now()} Discord-ServerManager is online as {bot.user}")
    print(f"{time_now()} Discord-ServerManager is connected to {len(bot.guilds)} guild(s)")
    print(f"{time_now()} Discord-ServerManager is connected to {len(bot.users)} user(s)")
    print(f"{time_now()} Discord-ServerManager is running on OS ID: {os.name}")
    print(f"{time_now()} Discord-ServerManager is running on Python {sys.version} with Pycord Version {discord.__version__}")


for filename in os.listdir(COG_FOLDER_PATH):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")
        print(f"{time_now()} Cog {filename[:-3]} was loaded")
print()


bot.run(TOKEN)
