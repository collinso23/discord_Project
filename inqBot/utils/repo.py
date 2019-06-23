import constants

version = "v0.0.1"
invite ="https://discord.gg/gVE5HdJ"
owners = constants.OWNERS

def is_owner(ctx):
    return ctx.author.id in owners
