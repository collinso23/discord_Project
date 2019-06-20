import discord
from discord.ext import commands
from utils import default, dnd_beyond_scrape,repo
from bs4 import BeautifulSoup, SoupStrainer, Tag
import requests
import lxml
import re
import urllib
import textwrap
from nltk import tokenize

class Search_DnD(commands.Cog):
        def __init__(self,bot):
            self.bot = bot
            self.HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
            #self.scraper = dnd_beyond_scrape.DnD_Scraper()

        """
        param: url
        return the Entire HTML code fo the website
        """
        def getEntireHTMLPage(self,url):
            page = requests.get(url,headers=self.HEADERS).text
            soup = BeautifulSoup(page,features ="lxml")
            return soup

        """
        breakTextByLength method
        breaks text up by length we would like on each line
        If word exceeds length, then new line is processed before
        """
        def breakTextByLength(self,text,length = 150):
            if text is not None:
                text_by_line = re.split('[\r\n]',text)
                return_String = ""
                for t in text_by_line:
                    if t is not None:
                        if len(t) > 149:
                            dividedText = textwrap.wrap(t,length)
                            dividedText = '\n'.join(dividedText)
                            return_String = return_String + dividedText + '\n'
                        else:
                            return_String = return_String + t + '\n'
                return return_String
        """
        titlize method
        Gives a text title format
        most words are capitalized, simply words like -> is,of,in,a,an,the, etc are not
        """
        def titlize(self, text):
            splitText = text.split()
            specialCaseWords = ["from","so","is","of","in","a","an","the","but","for"]
            return_String = []
            for w in splitText:
                if w not in specialCaseWords:
                    return_String.append(w.capitalize())
                else:
                    return_String.append(w)
            return ' '.join(map(str, return_String))

        @commands.group(pass_context=True)
        async def tomes(self,ctx):
            """
            Scrapes DND beyond: https://www.dndbeyond.com/search?q= for various dnd related
            features and returns them to the chat so that users may quickly resume

            Commands: [$tomes]

            Subcommands: [--race,--class,--spell]

            Command syntax: $tomes --subcommand 'name_of_search' 'specifier'
            """
            if ctx.invoked_subcommand is None:
                await ctx.send_help(str(ctx.command))

        @tomes.command(name="--race",aliases=["-r"])
        async def _tomesRace(self,ctx,name_of_search,specifier=""):
            #scraper = dnd_beyond_scrape.DnD_Scraper()
            name_of_search = re.sub('[^\w]', '%20', name_of_search)
            url = "https://www.dndbeyond.com/search?q="+name_of_search+"&f=backgrounds,classes,feats,races&c=characters"
            soup = self.getEntireHTMLPage(url)
            soup_2 = self.searchRace(soup,specifier)
            self.extractInformationFromRacePage(soup_2,specifier)

            await ctx.send("Here!!: {}".format(type(info)))

        """
        param: raceName
            Name of race to be searched
        """
        def searchRace(self, soup, specifier):
            searchListing = soup.find('div',{'class':'ddb-search-results-listing'})
            searches = soup.find_all('div',{'class':'ddb-search-results-listing-item'})
            for search in searches:
                if search is not None:
                    if search.find('span', {'class':'races'}) is not None:
                        link = search.find('a')['href']
                        url = "https://www.dndbeyond.com" + link
                        soup = self.getEntireHTMLPage(url)
                        return soup
                        #self.extractInformationFromRacePage(soup,specifier)
                        #break

        "extacts information from Race Page"
        def extractInformationFromRacePage(self,soup,specifier):
            mainInformation = soup.find('div',{'id','content'})
            headers = soup.find_all("h2")
            info = ""
            allInfo = ""
            for header in headers:
                if header is not None:
                    if specifier in header.text:
                        nextNode = header
                        info = ""
                        """/42820342/get-text-in-between-two-h2-headers-using-beautifulsoup"""
                        while True:
                            nextNode = nextNode.nextSibling
                            if nextNode is None:
                                break
                            if isinstance(nextNode, Tag):
                                if nextNode.name == "span":
                                    info = info + self.breakTextByLength(nextNode.text) + "\n"
                                if nextNode.name == "h4":
                                    info = info + nextNode.text + "\n"
                                elif nextNode.name == "h2":
                                    break
                                elif nextNode.name == "h3":
                                    break
                        allInfo = allInfo + info + "\n"
            return allInfo
        """
        @commands.command()
        async def tomes(self,ctx,section,name_of_search,specifier=""):
            scraper = dnd_beyond_scrape.DnD_Scraper()
            if section =="--class":
                race_info = scraper.searchDNDWebsite(section,name_of_search,specifier)
            elif section == "--items":
                item_info = scraper.searchDNDWebsite(section,name_of_search,specifier)
                #return_string = scraper.extractInformationFromItemPage(item_info)
                await ctx.send("THE TOMES SPEAK {}".format(type(item_info)))
            #if ctx.invoked_subcommand is None:
            #    await ctx.send_help(str(ctx.command))
        """
def setup(bot):
    bot.add_cog(Search_DnD(bot))
