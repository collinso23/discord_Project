import discord

from discord.ext import commands
from utils import default, wiki_scrape, repo

class Search(commands.Cog):
        def __init__(self,bot):
            self.bot = bot
            self.Scraper = wiki_scrape.Scraper

        @commands.group(pass_context=True)
        async def tomes(self,ctx):
            """Searches DnD wiki for various params and returns them to chat."""
            if ctx.invoked_subcommand is None:
                await ctx.send("Error: Input subcommand [--race,--class,--spell]") #send_help(str(ctx.command))

        @tomes.command(name="--race")
        async def _search_race(self,ctx,race_name):
            raceName = race_name
            try:
                information = self.Scraper.getRaceInformation(raceName)
                await ctx.send("{}".format(information))
            except Exception as err:
                error_message= '{}: {}'.format(type(err).__name__,err)
                print(error_message)
                await ctx.send("Error, something went wrong with the --race method")

        """
        @search.command(name="--class",alias="-c")
        async def search_class():
            return None
        @search.command(name="--spell",alias="-s")
        async def search_spell():
            return None
        """
def setup(bot):
    bot.add_cog(Search(bot))
