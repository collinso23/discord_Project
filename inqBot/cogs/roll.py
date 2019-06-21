import discord
from discord.ext import commands
import random

class RollDice(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @command.group(pass_context=True,case_insensitive=True)
    async def roll(self,ctx):
        """
        For rolling dice in discord
        @roll --dice_type --num_o_dice
        """
        if ctx.invoked_subcommand is None:
            await ctx.send_help(str(ctx.command))

    @roll.commands(name="d4")
    async def _d4_roll(self,ctx,num_o_dice):
        result = ''.join(str(random.randrange(1,4)) for r in range(num_o_dice))
        await ctx.send(result)

    @roll.commands(name="d6")
    async def _d6_roll(self,ctx,num_o_dice):
        result = ''.join(str(random.randrange(1,6)) for r in range(num_o_dice))
        await ctx.send(result)

    @roll.commands(name="d8")
    async def _d8_roll(self,ctx,num_o_dice):
        result = ''.join(str(random.randrange(1,8)) for r in range(num_o_dice))
        await ctx.send(result)

    @roll.commands(name="d10")
    async def _d10_roll(self,ctx,num_o_dice):
        result = ''.join(str(random.randrange(1,10)) for r in range(num_o_dice))
        await ctx.send(result)

    @roll.commands(name="d12")
    async def _d12_roll(self,ctx,num_o_dice):
        result = ''.join(str(random.randrange(1,12)) for r in range(num_o_dice))
        await ctx.send(result)

    @roll.commands(name="d20")
    async def _d20_roll(self,ctx,num_o_dice):
        result = ''.join(str(random.randrange(1,20)) for r in range(num_o_dice))
        await ctx.send(result)

def setup(bot):
    bot.add_cog(RollDice(bot))
