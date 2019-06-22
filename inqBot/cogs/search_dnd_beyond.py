import discord
from discord.ext import commands
from utils import default, dnd_scraper,repo

class Search_DnD(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        #scraper = DnD_Scraper()

        @commands.group(pass_context=True)
        async def tomes(self,ctx):
            """
            Scrapes DND beyond: https://www.dndbeyond.com/search?q= for various dnd related
            features and returns them to the chat so that users may quickly resume

            Commands: [$tomes]

            Subcommands: [--race,--class,--spell]

            Command syntax: $tomes --subcommand 'name_of_search' 'specifier'
            """
            if ctx.invoked_subcommand is None:
                await ctx.send_help(str(ctx.command))

        @tomes.command(name="--race",aliases=["-r"])
        async def _tomesRace(self,ctx,name_of_search,specifier=""):
           
            await ctx.send("Here!!: {}, {}".format(name_of_search,specifier))

def setup(bot):
    bot.add_cog(Search_DnD(bot))
    

