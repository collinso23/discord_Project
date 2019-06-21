import discord
from discord.ext import commands
from utils import default, dnd_scraper, repo
import textwrap

class Search_DnD(commands.Cog):

        def __init__(self,bot):
            self.bot = bot

        @commands.group(pass_context=True)
        async def tomes(self,ctx,*args):
            """
            Scrapes DND beyond: https://www.dndbeyond.com/search?q= for various dnd related
            features and returns them to the chat so that users may quickly resume

            Commands: [$tomes]

            Subcommands: [race,class,spell,item]

            Command syntax: $tomes --subcommand 'name_of_search' 'specifier'
            """
            scraper = dnd_scraper.DnD_Scraper()
            arguments = []
            for a in args:
                arguments.append(a)

            arguments_as_string = " ".join(arguments)
            rstring = scraper.searchDNDWebsite(arguments[0],arguments[1],arguments[2])
            rstring_as_list = textwrap.wrap(rstring, 1500, break_long_words=False)

            for message in rstring_as_list:
                await ctx.send(message)
            #if ctx.invoked_subcommand is None:
            #    await ctx.send_help(str(ctx.command))

        @tomes.command(name="--race",aliases=["-r"])
        async def _tomesRace(self,ctx,name_of_search,specifier=""):

            await ctx.send("Here!!: {}, {}".format(name_of_search,specifier))

def setup(bot):
    bot.add_cog(Search_DnD(bot))
