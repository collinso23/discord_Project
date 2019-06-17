import discord
from discord.ext import commands
from utils import default, wiki_scrape
from wiki_scrape import Scraper

class Search(commands.Cog):
        def __init__(self,bot):
            self.bot = bot

        @commands.command()
        async def search(self,ctx):
            """Searches DnD wiki for various params and returns them to chat."""
            if ctx.invoked_subcommand is None:
                await ctx.send("Error: Input subcommand [--race,--class,--spell]") #send_help(str(ctx.command))

        @search.command(name="--race", alias="-r")
        async def search_race(self,ctx,race_name):
            information = Scraper.getRaceInformation(race_name)
            await ctx.send("{}".format(information))

        """
        @search.command(name="--class",alias="-c")
        async def search_class():
            return None
        @search.command(name="--spell",alias="-s")
        async def search_spell():
            return None
        """
def setup():
    bot.add_cog(Search(bot))
