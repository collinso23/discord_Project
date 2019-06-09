import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import lxml
import config

class Wiki_Scraper(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.HEADERS = config.HEADERS

    @commands.command()
    async def searchClass(self,ctx,className):
        """ Scrapes dndnwiki for class based on input arg"""
        url = "https://www.dandwiki.com/wiki/5e_Classes"
        page = requests.get(url,headers=self.HEADERS).text
        soup = BeautifulSoup(page,features ="lxml")
        mainDiv = soup.find('div',{'class': 'mw-parser-output'})
        allLinks = mainDiv.findAll('a')
       
        for link in allLinks:
            title = link.get('title')
            if title is not None:
                if className in title:
                    await ctx.send("The class: {}".format(title))
