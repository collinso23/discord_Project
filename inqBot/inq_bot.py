import os
import discord
import logging

from log import DiscordHandler

from discord.ext.commands import Bot, when_mentioned_or

from utils import permissions, default

config = default.get("config.json")

logger = logging.getLogger(__name__)

bot = Bot(
    command_prefix=when_mentioned_or(config.prefix),

    activity=config.playing
)

logger.addHandler(DiscordHandler(bot))
logger.setLevel(logging.INFO)

bot.log = logger

# Load cogs
for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extensions(f"cogs.{name}")

bot.run(config.token)
