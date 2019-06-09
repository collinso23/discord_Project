import discord
import logging

class Logging(commands.cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    async def on_ready(self):
        log.info("Bot Connected!")

    def init_logging(self):
	logger = logging.getLogger('discord')
	logger.setLevel(logging.INFO)
	handler = logging.FileHandler(filename='discord.log', encoding='utf-8',mode='w')
	hanlder.setFormatter(logging.Formater('%(asctime)s:%(levelname)s:%(name)s:%(message)s'))
	logger.addHandler(handler)
def setup(bot):
    bot.add_cog(Logging(bot))

