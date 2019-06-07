import requests
from bs4 import BeautifulSoup
import lxml

class Wiki_Scraper(object):
    def __init__(self):
        self.HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

    def getClassInformation(self,className):
        url = "https://www.dandwiki.com/wiki/5e_Classes"
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

wc = Wiki_Scraper()
wc.getClassInformation("Warlock")
    

