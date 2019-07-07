from discord.ext import commands
import logging
import utils
from utils.dice_class import make_roll

log = logging.getLogger(__name__)

class CharGenerator(commands.Cog):
    """Random Character Generator"""
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name='char')
    async def randChar(self,ctx,level='0'):
        """Generates a random character as json file"""
        try:
            level = int(level)
        except:
            await ctx.send("invalid level")
            return

        if level == 0:
            rolls = [make_roll('1d20') for _ in range(6)]
            stats = '\n'.join(r for r in rolls)
            total = sum([r.total for r in rolls])
            await ctx.send(f"{ctx.message.author.mention}\n Generated random stats\n {stats}\n Total = '{total}'")
            return

        if level > 20 or level < 1:
            await ctx.send("Invalid level (must be 1-20)")
            return

        await self.genChar(ctx,level)
