import discord
from discord.ext import commands
import random

class RollDice(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.group(pass_context=True,case_insensitive=True)
    async def roll(self,ctx):
        """
        For rolling dice in discord
        $roll -mR <dice_type> <modifer> <num_dice>
        """
        if ctx.invoked_subcommand is None:
            await ctx.send_help(str(ctx.command))

    @roll.command(name="--make_roll", aliases =["-mR"])
    async def _make_roll(self,ctx,dice,modifer="0",num_dice="1"):
        """
        params: dice (ie,d6,d8,d10...)
                modifer (ie [INT +2], saving throws, prof bonus...)
                number of dice (1,2,3...)

        """
        dice_list=list(dice)
        if len(dice) >= 3:
            dice_type = dice[-2:]
        else:
            dice_type = dice[-1:]
        result = []
        for num in range(int(num_dice)):
            r = random.randint(1,int(dice_type)) + int(modifer)
            result.append(r)
        total = sum(result)
        await ctx.send("dice: d{} {}={} Mod: +{} on each roll".format(dice_type,result, total, modifer))

def setup(bot):
    bot.add_cog(RollDice(bot))
