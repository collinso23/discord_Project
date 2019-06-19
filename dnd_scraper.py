from bs4 import BeautifulSoup, SoupStrainer, Tag
import requests
import lxml
import re
import urllib
import textwrap
from nltk import tokenize

"""
Scrapes from the offical Dnd Page
"""
class DnD_Scraper(object):

    """Constructor
    """
    def __init__(self):
        self.HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}


    """
    param: url
    return the Entire HTML code fo the website
    """
    def getEntireHTMLPage(self,url):
        page = requests.get(url,headers=self.HEADERS).text
        soup = BeautifulSoup(page,features ="lxml")
        return soup

    """

    """
    def requestIdentifier(self, command, section, nameOfSearch, specifier):
        if command == "$search":
            self.searchDNDWebsite(command, section, specifier)
        """
        elif command == "$SOMETHINGELSE":
            #self.search()
        else:
            #return "Not an actual command"
        """
    """
    param: section, nameOfSearch
        section: specifies if user is looking for imformation about items, race, class, etc.
        nameOfSearch: what to be searched for on the search bar
    If user calls the search function on the bot, then the bot will perofrm a search on
    the search bar on dndbeyond according to the requested section
    """
    def searchDNDWebsite(self, section, nameOfSearch,specifier=""):
        nameOfSearch = re.sub('[^\w]', '%20', nameOfSearch)
        url = "https://www.dndbeyond.com/search?q=" + nameOfSearch
        print(url)
        soup = self.getEntireHTMLPage(url)
        if section == "items":
            soup = self.getEntireHTMLPage(url+"&f=equipment,magic-items&c=items")
            self.searchItems(soup)
        elif section == "class":
            soup = self.getEntireHTMLPage(url+"&f=backgrounds,classes,feats,races&c=characters")
            self.searchClass(soup,specifier)
        elif section == "race":
            soup = self.getEntireHTMLPage(url+"&f=backgrounds,classes,feats,races&c=characters")
            self.searchRace(soup,specifier)
        elif section == "spell":
            soup = self.getEntireHTMLPage(url+"&f=spells&c=spells")
            self.searchSpell(soup,specifier)

    """
    param: itemName
        name of the Item to be searched

    """
    def searchItems(self, soup):
        searchListing = soup.find('div',{'class':'ddb-search-results-listing'})
        searches = soup.find_all('div',{'class':'ddb-search-results-listing-item'})
        for search in searches:
            if search is not None:
                if search.find('span', {'class':'magic-items'}) is not None:
                    link = search.find('a')['href']
                    url = "https://www.dndbeyond.com" + link
                    soup = self.getEntireHTMLPage(url)
                    self.extractInformationFromItemPage(soup)
                    break

    def extractInformationFromItemPage(self,soup):
        mainInformation = soup.find('div',{'class','more-info-content'})
        print(self.breakTextByLength(mainInformation.text))

    """
    param: soup, specifier
    soup of search page
    specifier is what you are specifically looking for
    Name of class to be searched
    """
    def searchClass(self, soup, specifier):
        searchListing = soup.find('div',{'class':'ddb-search-results-listing'})
        searches = soup.find_all('div',{'class':'ddb-search-results-listing-item'})
        for search in searches:
            if search is not None:
                if search.find('span', {'class':'classes'}) is not None:
                    link = search.find('a')['href']
                    url = "https://www.dndbeyond.com" + link
                    soup = self.getEntireHTMLPage(url)
                    self.extractInformationFromClassPage(soup,specifier)
                    break


    """Extracts from class page and a subsection being the specifier"""
    def extractInformationFromClassPage(self, soup, specifier):
        mainInformation = soup.find('div',{'id','content'})
        bigHeaders = soup.find_all(re.compile('^h[1-6]$'))
        smallHeaders = soup.find_all('dl')
        headers = bigHeaders+smallHeaders
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
                            if nextNode.name == "p":
                                info += self.breakTextByLength(nextNode.text)
                            else:
                                break
                    allInfo = allInfo + info + "\n"
        print(allInfo)


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
                    self.extractInformationFromRacePage(soup,specifier)
                    break

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
        print(allInfo)

    """
    param: spellName
        Name of Spell to be searched
    """
    def searchSpell(self, soup):
        print(soup)

    """
    If given a list of strings, this method concatenates the lists into
    a single string and makes it look pretty.
    """
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
        if text is not None:
            text_by_line = re.split('[\r\n]',text)
            rstring = ""
            for t in text_by_line:
                if t is not None:
                    if len(t) > 149:
                        dividedText = textwrap.wrap(t,length)
                        dividedText = '\n'.join(dividedText)
                        rstring = rstring + dividedText + '\n'
                    else:
                        rstring = rstring + t + '\n'
            return rstring
    """
    titlize method
    Gives a text title format
    most words are capitalized, simply words like -> is,of,in,a,an,the, etc are not
    """
    def titlize(self, text):
        splitText = text.split()
        specialCaseWords = ["from","so","is","of","in","a","an","the","but","for"]
        returnString = []
        for w in splitText:
            if w not in specialCaseWords:
                returnString.append(w.capitalize())
            else:
                returnString.append(w)
        return ' '.join(map(str, returnString))



scrap = DnD_Scraper()
scrap.searchDNDWebsite("items", "potion of healing")
scrap.searchDNDWebsite("class", "Barbarian","Rage")
scrap.searchDNDWebsite("race","Human","Human Traits")
