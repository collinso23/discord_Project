import discord
from discord.ext import commands
import config
import requests 
import greetings
from bs4 import BeautifulSoup

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
   """ url = 'https://roll20.net/compendium/dnd5e/BookIndex'"""

    wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
    page = request.urlopen(url, headers=HEADERS)
    soup = BeautifulSoup(page)
    print soup

    await ctx.send(soup.prettify())
    
    
    
HEADERS = config.HEADER    
@bot.command()
async def bitcoin(ctx):
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    resp = requests.get(url,headers=HEADERS)
    value = resp.json()['bpi']['USD']['rate']
    await ctx.send("Bitcoin price is: $"+value)

bot.add_cog(Greetings(bot))    
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
