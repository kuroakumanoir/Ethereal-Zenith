""""
Copyright © Kuroakumanoir 2022 - https://github.com/kuroakumanoir
Description:
This is a template to create your own discord bot in python.

Version: 1.0.0
"""

#The following code follows PEP8 (mostly)
import asyncio
import errors
import chunk
import datetime
import io
import json
import logging
import logging.handlers
import os
import re
import traceback
import platform
import sys
import aiohttp
import discord
import jishaku
from discord.ext import commands
from discord.ext.commands.errors import (
    ExtensionAlreadyLoaded,
    ExtensionFailed,
    ExtensionNotFound,
    NoEntryPointError
)

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
logging.getLogger('discord.http').setLevel(logging.INFO)

handler = logging.handlers.RotatingFileHandler(
    filename='discord.log',
    encoding='utf-8',
    maxBytes=32 * 1024 * 1024,  # 32 MiB
    backupCount=5,  # Rotate through 5 files
)
dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)


class Bot(commands.Bot):
    def _init_(self, *args, **kwargs):
         super ()._init_(*args, **kwargs)

    async def on_error(self, error): 
        traceback.print_exc()

class EtherealZenith(commands.Bot):
    def __init__(self) -> None:
        super().__init__(
            command_prefix =commands.when_mentioned_or(">>"),
            intents = discord.Intents.all(),
            case_insensitive=True,
            application_id = ,  # Your application id here
            chunk_guilds_at_startup=False,
            strip_after_prefix=True)
        self.synced = False
        self.session: aiohttp.ClientSession = None

    async def create_session(self):
        self.session = aiohttp.ClientSession()

    async def setup_hook(self):
        await self.load_extension("jishaku")
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await self.load_extension(f'cogs.{filename[:-3]}')
        if not self.synced:
            #await bot.tree.sync()
            await bot.tree.sync()
            self.synced = True

    async def on_ready(self):
        print(f"Logged in as {self.user.name}")
        print(f"discord.py API version: {discord.__version__}")
        print(f"Python Version: {sys.version}")
        print(f"Running on: {platform.system()} {platform.release()} ({os.name})")  

    async def close(self) -> None:
        await super().close()

if __name__ == "__main__":
    bot = EtherealZenith()
    TOKEN = ('') # Your Bot Token here
    bot.run(TOKEN, reconnect=True, log_handler=None)



#A section of this code is inspired by, Krypton 2022 - https://github.com/kkrypt0nn (https://krypton.ninja), Be sure to check out his repo too.
