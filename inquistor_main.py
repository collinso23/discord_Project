import discord
from discord.ext import commands
import config
import requests 


bot = commands.Bot(command_prefix="$")
@bot.event
async def on_ready():
    print("Logged in as", bot.user)
"""     
@bot.event
async def on_message(msg):
    if message.author == bot.user:
        return
"""        
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command(
        name='search',
        description='search Roll20 compendium for arg',
        aliases=['-s','--search'])
async def search(ctx,arg):
    await ctx.send(arg)
    
HEADERS = config.HEADER    
@bot.command()
async def bitcoin(ctx):
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    resp = requests.get(url,headers=HEADERS)
    value = resp.json()['bpi']['USD']['rate']
    await ctx.send("Bitcoin price is: $"+value)
    
bot.run(config.BOT_TOKEN)

"""
async def list_servers():
    await bot.wait_until_ready()
    while not bot.is_closed:
        print("Current Servers:")
        for server in bot.servers:
            print(server.name)
        await asyncio.sleep(6)
bot.loop.create_task(list_servers())
"""
