import discord
from discord.ext import commands
from utils.dice_class import SuperDice


class RollDice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx, dice, modifer="0"):
        """
        For rolling dice in discord
        $roll <#>d<#> <modifer>
        """
        my_dice = SuperDice()
        result = my_dice.make_roll(dice, modifer)

        await ctx.send(result)
        #if ctx.invoked_subcommand is None:
        #    await ctx.send_help(str(ctx.command))


def setup(bot):
    bot.add_cog(RollDice(bot))
