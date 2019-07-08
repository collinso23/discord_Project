from discord import Game
import pdb
import logging
import discord
import os
from discord.ext.commands import Bot, when_mentioned_or
import constants
from utils import log
pdb.set_trace()


desc = """
A bot to help with the running of DND campaigns
Along with general administrative functions
"""

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(
    command_prefix=when_mentioned_or(constants.PREFIX),

    description=desc,

    activity=Game(name="Reading Tomes")
)

logger.addHandler(log.DiscordHandler(bot))
logger.setLevel(logging.INFO)
bot.log = logger


@bot.event
async def on_ready():
    print('Logged in as {}'.format(bot.user.name))
    print('-----')

if __name__ == "__main__":
    try:
        for file in os.listdir("cogs"):
            if file.endswith(".py"):
                name = file[:-3]
                bot.load_extension(f"cogs.{name}")
    except Exception as err:
        exc = '{}: {}'.format(type(err).__name__, err)
        print('Failed to load extension\n{}'.format(exc))
bot.run(constants.BOT_TOKEN)
