import discord

from utils import repo
from discord.ext import commands


async def check_permissions(ctx, perms, *, check=all):
    if ctx.author.id in repo.owners:
        return True

    resolved = ctx.channel.permissions_for(ctx.author)
    return check(getattr(resolved, name, None) == value for name, value in perms.items())

def has_permissions(*, check=all, **perms):
    async def pred(ctx):
        return await check_permissions(ctx, perms, check=check)
    return commands.check(pred)
