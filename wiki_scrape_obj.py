import requests
from bs4 import BeautifulSoup
import lxml

class Wiki_Scraper(object):
    def __init__(self):
        self.HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

    def getClassInformation(self,className):
        url = "https://www.dandwiki.com/wiki/5e_SRD:Classes"
        page = requests.get(url,headers=self.HEADERS).text
        soup = BeautifulSoup(page,features ="lxml")
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
        url = "https://www.dandwiki.com/wiki/5e_SRD:Races"
        page = requests.get(url, headers=self.HEADERS).text
        soup = BeautifulSoup(page,features="lxml")
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

    def extractFromRacePage(self,url):
        page = requests.get(url,headers=self.HEADERS).text
        soup = BeauitfulSoup(page,features="lxml")
        mainDiv = soup.find('div',{'class','mw-parser-output'})
        allParagraphs = mainDiv.findAll('p')
        print(allParagraphs)

        #for row, tr in enumerate
wc = Wiki_Scraper()
wc.getClassInformation("Warlock")
wc.getRaceInformation("Human")
    

