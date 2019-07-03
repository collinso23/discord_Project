from bs4 import BeautifulSoup, SoupStrainer, Tag
import requests
import lxml
import re
import urllib3
import textwrap
from nltk import tokenize
import constants

class DnD_DB_Scrapper(object):

    """
    Constructor
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

    def getMonsterInformation(self, name):

        """Go to proper page"""
        url = "https://www.5thsrd.org/gamemaster_rules/monsters/"
        name = re.sub('[^\w]', "_",name.lower())
        info_page = url + name + "/"

        http =  urllib3.PoolManager()

        """Check to see if its an ACTUAL PAGE"""
        try:
            page = http.request('GET',info_page)
        except urllib3.exceptions.HTTPError as e:
            return "Monster Not Found"

        soup = BeautifulSoup(page.data, 'lxml')
        main_content = soup.find('div',{'role':'main'})
        if main_content is not None:
            return self.breakTextByLength(main_content.text)
        else:
            return "Monster Not Found"



    def getItemInformation(self,name):
        """Go to proper page"""
        url = "https://www.5thsrd.org/gamemaster_rules/magic_items/"
        name = re.sub('[^\w]', "_",name.lower())
        info_page = url + name + "/"

        http =  urllib3.PoolManager()

        """Check to see if its an ACTUAL PAGE"""
        try:
            page = http.request('GET',info_page)
        except urllib3.exceptions.HTTPError as e:
            return "Monster Not Found"

        soup = BeautifulSoup(page.data, 'lxml')
        main_content = soup.find('div',{'role':'main'})
        if main_content is not None:
            return self.breakTextByLength(main_content.text)
        else:
            return "Item Not Found"

    def getRaceInformation(self, name):
        """Go to proper page"""
        url = "https://www.5thsrd.org/character/races/"
        name = re.sub('[^\w]', "_",name.lower())
        info_page = url + name + "/"

        http =  urllib3.PoolManager()

        """Check to see if its an ACTUAL PAGE"""
        try:
            page = http.request('GET',info_page)
        except urllib3.exceptions.HTTPError as e:
            return "Monster Not Found"

        soup = BeautifulSoup(page.data, 'lxml')
        main_content = soup.find('div',{'role':'main'})
        if main_content is not None:
            return self.breakTextByLength(main_content.text)
        else:
            return "Race Not Found"

    def getClassInformation(self,name,specifier):
        """Go to proper page"""
        url = "https://www.5thsrd.org/character/classes/"
        name = re.sub('[^\w]', "_",name.lower())
        info_page = url + name + "/"
        specifier = self.titlize(specifier)
        info = ""
        http =  urllib3.PoolManager()

        """Check to see if its an ACTUAL PAGE"""
        try:
            page = http.request('GET',info_page)
        except urllib3.exceptions.HTTPError as e:
            return "Class Not Found"

        soup = BeautifulSoup(page.data, 'lxml')
        main_content = soup.find('div',{'role':'main'})
        if main_content is not None:
            headers = main_content.find_all(re.compile('^h[1-6]$'))
            if specifier == "":
                return self.breakTextByLength(main_content.text)
            elif specifier == "basic feats":
                basic_feat_start_point = headers.find("h2",{'id':'class-features'})
                return self.getInformationUntilNextHR(self,nextNode)
            else:
                for header in headers:
                    if header is not None:
                        if specifier in header.text:
                            nextNode = header
                            original_header_tag = nextNode.name
                            if original_header_tag == "span":
                                info = self.getInformationUntilNextSpan(nextNode) + "\n"
                            elif original_header_tag == "h1":
                                info = self.getInformationUntilNextH1(nextNode) + "\n"
                            elif original_header_tag == "h2":
                                info = self.getInformationUntilNextHeader2(nextNode) + "\n"
                            elif original_header_tag == "h3":
                                info = self.getInformationUntilNextH3(nextNode) + "\n"
                            elif original_header_tag == "h4":
                                info = self.getInformationUntilNextH4(nextNode) + "\n"
                            break
                return info
        else:
            return "Class not found"




    """
    These next couple of functions are very general. Basically, given a starting node, they
    will pull out all information found in p tags until reached a specified tag
    """

    def getInformationUntilNextHR(self,nextNode):
        info = ""
        info = nextNode.text + "\n\n"
        while True:
            nextNode = nextNode.nextSiblin
            if nextNode is None:
                break
            if isinstance(nextNode, Tag):
                if nextNode.name == "hr":
                    break
                else:
                    info = info + self.breakTextByLength(nextNode.text) + "\n"
        return info

    def getInformationUntilNextspan(self, nextNode):
        info = ""
        stopAt = ["div","h1","h2","h3","h4","span"]
        while True:
            nextNode = nextNode.nextSibling
            if nextNode is None:
                break
            if isinstance(nextNode, Tag):
                if nextNode.name in stopAt:
                    break
                else:
                    info = info + self.breakTextByLength(nextNode.text) + "\n"
        return info

    def getInformationUntilNextH1(self, nextNode):
        info = ""
        stopAt = ["div","h1"]
        while True:
            nextNode = nextNode.nextSibling
            if nextNode is None:
                break
            if isinstance(nextNode, Tag):
                if nextNode.name in stopAt:
                    break
                else:
                    info = info + self.breakTextByLength(nextNode.text) + "\n"
        return info

    def getInformationUntilNextHeader2(self, nextNode):
        info = ""
        stopAt = ["div","h2","h1"]
        while True:
            nextNode = nextNode.nextSibling
            if nextNode is None:
                break
            if isinstance(nextNode, Tag):
                if nextNode.name in stopAt:
                    break
                else:
                    info = info + self.breakTextByLength(nextNode.text) + "\n"
        return info


    def getInformationUntilNextH3(self,nextNode):
        info = ""
        stopAt = ["div","h2","h3","h1"]
        while True:
            nextNode = nextNode.nextSibling
            if nextNode is None:
                break
            if isinstance(nextNode, Tag):
                if nextNode.name in stopAt:
                    break
                else:
                    info = info + self.breakTextByLength(nextNode.text) + "\n"
        return info

    def getInformationUntilNextH4(self,nextNode):
        info = ""
        stopAt = ["div","h2","h3","h1","h4"]
        while True:
            nextNode = nextNode.nextSibling
            if nextNode is None:
                break
            if isinstance(nextNode, Tag):
                if nextNode.name in stopAt:
                    break
                else:
                    info = info + self.breakTextByLength(nextNode.text) + "\n"
        return info

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


    def fixSpacingOnText(self,text):
        text_by_line = text.split('\n')
        finaltext = ""
        for line in text_by_line:
            if len(line) > 2:
                line = re.sub(r'^\s+','',line)
                finaltext = finaltext + line+ "\n"
        return finaltext



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


dd = DnD_DB_Scrapper()
"""nameOfMonster = input("What is the name of the monster?")
print(dd.getMonsterInformation(nameOfMonster))
nameOfRace = input("what is the name of the race?")
print(dd.getRaceInformation(nameOfRace))
className = input("what is the name of the class?")
sCI = input("what should i look up in the class page?")
print(dd.getClassInformation(className,sCI))
"""
itemName = input("what is the name of the item?")
print(dd.getItemInformation(itemName))