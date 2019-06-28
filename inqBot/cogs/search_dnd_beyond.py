import discord
from discord.ext import commands
from utils import dnd_scraper
import textwrap

class SearchDnD(commands.Cog):

        def __init__(self,bot):
            self.bot = bot

        @commands.group(pass_context=True)
        async def tomes(self,ctx,*args):
            """
            Scrapes DND beyond: https://www.dndbeyond.com/search?q= for various dnd related
            features and returns them to the chat so that users may quickly resume

            # Make sure to encapluslate multi-word queries with "quotes"

            Commands: [$tomes]

            Subcommands/search_type: [race,class,spell,item]

            Command syntax: $tomes 'search_type' 'name_of_search' 'specifier'
                ie: $tomes spells fireball,
                    $tomes items "potion of healing"
                    $tomes class barbarian "class features"
            """
            try:
                scraper = dnd_scraper.DnDScraper()
                arguments = []
                for a in args:
                    arguments.append(a)

                rstring = scraper.searchDNDWebsite(*arguments)
                rstring_as_list = textwrap.wrap(rstring, 1500, break_long_words=False)

                for message in rstring_as_list:
                    await ctx.send(message)
            except Exception as err:
                exc= '{}: {}'.format(type(err).__name__,err)
                print('Failed: {}\n'.format(exc))
                await ctx.send_help(ctx.command)


def setup(bot):
    bot.add_cog(SearchDnD(bot))
