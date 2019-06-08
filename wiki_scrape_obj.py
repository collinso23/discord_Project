import requests
from bs4 import BeautifulSoup, SoupStrainer
import lxml

class Wiki_Scraper(object):
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
    param:className
    returns the class information of the character
    Cannot Handle: Incorrectly spelled name
    """
    def getClassInformation(self,className):
        soup = self.getEntireHTMLPage("https://www.dandwiki.com/wiki/5e_SRD:Classes")
        mainDiv = soup.find('div',{'class': 'mw-parser-output'})
        allLinks = mainDiv.findAll('a')
        #table = soup.find('table', {'class': 'column'})
        #print(allLinks)
        for link in allLinks:
            title = link.get('title')
            #print(title)
            #print("\n")
            if title is not None:
                if className in title:
                    print(title)

    def getRaceInformation(self,raceName):
        soup = self.getEntireHTMLPage("https://www.dandwiki.com/wiki/5e_SRD:Races")
        mainTable = soup.find('table',{'class':'5e mw-collapsible'})
        mainDiv = soup.find('div',{'class','mw-parser-output'})
        rows = mainTable.findAll('tr')
        #print(rows)
        #links = rows.findAll('a')
        links = mainDiv.findAll('a')
        #print(links)
        for link in links:
            title = link.get('title')
            if title is not None:
                if raceName in title:
                    self.extractFromRacePage(link['href'])
                    #print(link['href'])

    
    def extractFromRacePage(self,href):
        soup = self.getEntireHTMLPage("https://www.dandwiki.com" + href)
        mainDiv = soup.find('div',{'class','mw-parser-output'})
        allParagraphs = mainDiv.findAll('p')
        allText = [p.find_all(text=True,recursive=False) for p in allParagraphs]
        #returnText

        """ for index in allText:
            if len(index.text) > 3:
                returnText = returnText + index.text

        print(returnText)"""
        print(allText)
        returnText = ""
        dividedText = ''.join(map(str, allText))
        for l in dividedText:
            if len(l) > 1:
                for sentence in l:
                    returnText = returnText + sentence
            else:
                returnText = returnText + "\n"
        #print(returnText)
        #print(''.join(allText))
        #print('\n'.join(allTextList)) 
        #for row, tr in enumerate
wc = Wiki_Scraper()
race = input("What Race should I search for? ")
#print("What Race should I search For?")
#wc.getClassInformation("Warlock")
wc.getRaceInformation(race)

