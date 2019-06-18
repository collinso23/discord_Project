import requests
from bs4 import BeautifulSoup, SoupStrainer
import lxml
import re
import textwrap
from nltk import tokenize
import discord
from discord.ext import commands
from utils import default

class Search(commands.Cog(name="search", alias=("-s")):
        def __init__(self,bot):
            self.bot = bot
            self.HEADERS=default.get("config.json").HEADERS
        
        def getEntireHTMLPage(self,url):
            page = requests.get(url,headers=self.HEADERS).text
            soup = BeautifulSoup(page,features ="lxml")
            return soup

        @commands.command()
        async def search(self,ctx):
            """Searches DnD wiki for various params and returns them to chat."""
            if ctx.invoked_subcommand is None:
                await ctx.send_help(str(ctx.command))
        
        def printListOfText(self,listText):
            lines = ""
            for l in listText:
                lines += l
            textDividedByLength = self.breakTextByLength(lines)
            print(textDividedByLength)
        
        """
        breakTextIntoSentences method
        breaks a text by sentences.
        Beta version, does not take into account all instances
        """
        def breakTextIntoSentences(self,text):
            textBySentence = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', text)
            return textBySentence

        """
        breakTextByLength method
        breaks text up by length we would like on each line
        If word exceeds length, then new line is processed before
        """
        def breakTextByLength(self,text,length = 150):
            textByLength = textwrap.wrap(text, length)
            return '\n'.join(textByLength)

        def titlize(self, text):
            splitText = text.split()
            specialCaseWords = ["from","s","is","of","in","a","an","the","but","for"]
            #returnString = ' '.join([w.capitalize() for w in splitText if w not in specialCaseWords])
            returnString = []
            for w in splitText:
                if w not in specialCaseWords:
                    returnString.append(w.capitalize())
                else:
                    returnString.append(w)
            return ' '.join(map(str, returnString))


        @search.command(name="-r", alias="--race")
        async def search_race(self,ctx,race_name,search:str):
            race_name= self.titlize(race_name)

        @search.command(name="-c",alias="--class")
        async def search_class():
        @search.command(name="-s",alias="--spell")
        async def search_spell():
def setup():
    bot.add_cog(Search(bot))
