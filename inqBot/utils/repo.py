from utils import default

version = "v0.0.1"
invite ="https://discord.gg/gVE5HdJ"
owners = default.get("config.json").owners

def is_owner(ctx):
    return ctx.author.id in owners
