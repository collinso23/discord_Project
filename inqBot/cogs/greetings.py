import discord
from discord.ext.commands
"""example cog to understand cog implementation so that search may be later implemented as a cog"""
class Greetings(commands.Cog):
    def __init__(self,bot):
            self.bot = bot
            self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self,member):
        """Greet Members when they join the server"""
        await self.bot.say('{0.name}' joined '{0.joined_at}'.format(member))

    @commands.command()
    async def hello(self,ctx,*,member: discord.Memeber=None):
        """ Says Hello"""
        member = member or ctx.author
        if self._last_memer is None or self._last_member.id != member.id:
            await ctx.send("Hello {0.name}~".format(member))
        else:
            await ctx.send("Hello {0.name}...This feels familiar".format(member))
        self._last_memeber = member

def setup(bot):
    bot.add_cog(Greetings(bot))
