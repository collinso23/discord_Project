import discord

from discord.ext import commands
from utils import default, wiki_scrape, repo

class Search_Wiki(commands.Cog):
        def __init__(self,bot):
            self.bot = bot


        @commands.group(pass_context=True)
        async def tomes(self,ctx):
            """
            Scrapes DND wiki: https://www.dandwiki.com/ for various dnd related
            features and returns them to the chat so that users may quickly resume

            Commands: [$tomes]

            Subcommands: [--race,--class,--spell]

            Command syntax: $tomes --race 'race_Name'
            """
            if ctx.invoked_subcommand is None:
                await ctx.send_help(str(ctx.command))
        """
        "--race" params: ["race_Name"]
        """
        @tomes.command(name="--race",aliases=["-r"])
        async def _searchRace(self,ctx,race_Name):
            scraper = wiki_scrape.Scraper()
            try:
                race_info = scraper.getRaceInformation(race_Name)
                await ctx.send("{}".format(race_info))
            except Exception as err:
                error_message= '{}: {}'.format(type(err).__name__,err)
                print(error_message)
                await ctx.send("Error, something went wrong with the --race method") #send("Error, something went wrong with the --race method")
        """
        "--class" params: ["class_Name" && "class_Feature"]
        """
        @tomes.command(name="--class",aliases=["-c"])
        async def _searchClass(self,ctx,class_Name,class_Feature):
            scraper = wiki_scrape.Scraper()
            try:
                class_info = scraper.getClassInformation(class_Name,class_Feature)
                await ctx.send("{}".format(class_info))
            except Exception as err:
                error_message= '{}: {}'.format(type(err).__name__,err)
                print(error_message)
                await ctx.send("Error, something went wrong with the --class method") #send("Error, something went wrong with the --class method")
        """
        "--spells" params: ["spell_Name"]
        """
        @tomes.command(name="--spell",aliases=["-s"])
        async def _searchSpell(self,ctx,spell_Name):
            scraper = wiki_scrape.Scraper()
            try:
                spell_information = scraper.getSpelInformation(spell_Name)
                await ctx.send("{}".format(information))
            except Exception as err:
                error_message= '{}: {}'.format(type(err).__name__,err)
                print(error_message)
                await ctx.send("Error, something went wrong with the --spell method")

def setup(bot):
    bot.add_cog(Search_Wiki(bot))
