import requests
from bs4 import BeautifulSoup, SoupStrainer
import lxml
import re
import textwrap
from nltk import tokenize
from utils import default

class Scraper(object):

    def __init__:
        self.HEADERS=default.get("config.json").HEADERS

    def getEntireHTMLPage(self,url):
            page = requests.get(url,headers=self.HEADERS).text
            soup = BeautifulSoup(page,features ="lxml")
            return soup

    def listOfText(self,listText):
        lines = ""
        for l in listText:
            lines += l
        textDividedByLength = self.breakTextByLength(lines)
        return textDividedByLength

    """
    breaks a text by sentences.
    Beta version, does not take into account all instances
    """
    def breakTextIntoSentences(self,text):
        textBySentence = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', text)
        return textBySentence

    """
    breaks text up by length we would like on each line
    If word exceeds length, then new line is processed before
    """
    def breakTextByLength(self,text,length = 150):
        textByLength = textwrap.wrap(text, length)
        return '\n'.join(textByLength)

    """
    searches for titles of keyword in function
    """
    def titlize(self, text):
        splitText = text.split()
        specialCaseWords = ["from","s","is","of","in","a","an","the","but","for"]
        returnString = []
        for w in splitText:
            if w not in specialCaseWords:
                return String.append(w.capitalize())
            else:
                return String.append(w)
        return ' '.join(map(str, returnString))


    """
    param:className
    returns the class information of the character
    Cannot Handle: Incorrectly spelled name
    """
    def getClassInformation(self,className,specificClassTrait):
        className = self.titlize(className)
        specificClassTrait = self.titlize(specificClassTrait)
        #print(className)
        #print(specificClassTrait)
        soup = self.getEntireHTMLPage("https://www.dandwiki.com/wiki/5e_SRD:Classes")
        mainTable = soup.find('table',{'class':'5e mw-collapsible'})
        mainDiv = soup.find('div',{'class','mw-parser-output'})
        rows = mainTable.findAll('tr')
        links = mainDiv.findAll('a')
        for link in links:
            title = link.get('title')
            if title is not None:
                 if className in title:
                     self.extractFromClassPage(link['href'],specificClassTrait,className)
    """
    Gets information specified by user about the chosen class
    """
    def extractFromClassPage(self,href,title,className):
        soup = self.getEntireHTMLPage("https://www.dandwiki.com" + href)
        mainTitle = soup.find('span',{'class','mw-headline'})
        bigHeaders = soup.find_all(re.compile('^h[1-6]$'))
        smallHeaders = soup.find_all('dl')
        headers = bigHeaders+smallHeaders
        for header in headers:
            if header is not None:
                if title in header.text:
                    return self.breakTextByLength(header.find_next('p').text)

    """
    getRaceInformation method
    given race name, It finds the link that holds the information about the race we are searching for
    and then calls the extractFromRacePage method to extract information about the race
    """
    def getRaceInformation(self,raceName):
        raceName = self.titlize(raceName)
        #print(raceName)
        soup = self.getEntireHTMLPage("https://www.dandwiki.com/wiki/5e_SRD:Races")
        mainTable = soup.find('table',{'class':'5e mw-collapsible'})
        mainDiv = soup.find('div',{'class','mw-parser-output'})
        rows = mainTable.findAll('tr')
        links = mainDiv.findAll('a')
        for link in links:
            title = link.get('title')
            if title is not None:
                if raceName in title:
                    self.extractFromRacePage(link['href'])


    """
    extractFromRacePage
    Gets all information about a race in dnd found on the dandwiki.com page and prints it out
    Updated method will be able to specify which sentences
    """
    def extractFromRacePage(self,href):
        soup = self.getEntireHTMLPage("https://www.dandwiki.com" + href)
        mainDiv = soup.find('div',{'class','mw-parser-output'})
        for a in soup.findAll('a'):
            a.replaceWithChildren()
        allParagraphs = mainDiv.findAll('p')
        allText = [p.find_all(text=True,recursive=False) for p in allParagraphs]
        totalCharsInTextFields = []
        totalCharacters = 0
        #To find out if the information found in each <p> is even worth printing out
        for section in allText:
            totalCharacters = 0
            for l in section:
                totalCharacters += len(l)
            totalCharsInTextFields.append(totalCharacters)
        for x in range(len(allText)):
            if totalCharsInTextFields[x] > 60:
                self.ListOfText(allText[x])

    """
    Given a spell name, this function will find all the useful information of that spell
    """
    def getSpellInformation(self,spellName):
        spellName = self.titlize(spellName)
        #print(spellName)
        soup = self.getEntireHTMLPage("https://www.dandwiki.com/wiki/5e_SRD:Spells")
        mainDiv = soup.find('div',{'class','mw-parser-output'})
        links = mainDiv.findAll('a')
        for link in links:
            title = link.get('title')
            if title is not None:
                if spellName in title:
                    self.extractFromSpellPage(link['href'])
                    break

    """
    Extracts all useful imformation from the specified spell name page
    """
    def extractFromSpellPage(self,href):
        soup = self.getEntireHTMLPage("https://www.dandwiki.com" + href)
        for a in soup.findAll('a'):
            a.replaceWithChildren()
        table_of_basic_information = soup.find('table',{'class','d20 dragon monstats'})
        #print(table_of_basic_information.text)
        paragraphs = table_of_basic_information.find_all_next()
        for p in paragraphs:
            tag_type = p.name
            if tag_type == 'hr':
                break
            elif tag_type == 'p':
                return p.text
