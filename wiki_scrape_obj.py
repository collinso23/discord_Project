import requests
from bs4 import BeautifulSoup, SoupStrainer
import lxml
import re
import textwrap
from nltk import tokenize
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
    def getClassInformation(self,className,specificClassTrait):
        className = self.titlize(className)
        specificClassTrait = self.titlize(specificClassTrait)
        print(className)
        print(specificClassTrait)
        soup = self.getEntireHTMLPage("https://www.dandwiki.com/wiki/5e_SRD:Classes")
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
                 if className in title:
                     self.extractFromClassPage(link['href'],specificClassTrait,className)

    """
    Gets information specified by user about the chosen class
    """
    def extractFromClassPage(self,href,title,className):
        soup = self.getEntireHTMLPage("https://www.dandwiki.com" + href)
        mainTitle = soup.find('span',{'class','mw-headline'})
        #underMainTitleText = mainTitle.find_all_next()
        #print(underMainTitleText)
        #for header in underMainTitleText.find_all("h1"):
        #   print(header.get_text())
        #print(underMainTitleText)
        bigHeaders = soup.find_all(re.compile('^h[1-6]$'))
        smallHeaders = soup.find_all('dl')
        headers = bigHeaders+smallHeaders
        for header in headers:
            if header is not None:
                if title in header.text:
                    #print(header.find_next())
                    print(self.breakTextByLength(header.find_next('p').text))
        #print(headers)
    """
    getRaceInformation method
    given race name, It finds the link that holds the information about the race we are searching for
    and then calls the extractFromRacePage method to extract information about the race
    """
    def getRaceInformation(self,raceName):
        raceName = self.titlize(raceName)
        print(raceName)
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
                self.printListOfText(allText[x])
        
    """
    Given a spell name, this function will find all the useful information of that spell
    """
    def getSpellInformation(self,spellName):
        spellName = self.titlize(spellName)
        print(spellName)
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
        print(table_of_basic_information.text)
        paragraphs = table_of_basic_information.find_all_next()
        for p in paragraphs:
            tag_type = p.name
            if tag_type == 'hr':
                break
            elif tag_type == 'p':
                print(p.text)
            

    
    """
    If given a list of strings, this method concatenates the lists into 
    a single string and makes it look pretty.
    """
    def printListOfText(self,listText):
        lines = ""
        for l in listText:
            lines += l
        #textDividedBySentence = self.breakTextIntoSentences(lines)
        textDividedByLength = self.breakTextByLength(lines)
        print(textDividedByLength)
        """for t in textDividedBySentence:
            print(t)
            print('\n')
        """
        

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
        #print("before \n" + ('[%s]' % ' '.join(map(str, splitText))))
        specialCaseWords = ["s","is","of","in","a","an","the","but","for"]
        #returnString = ' '.join([w.capitalize() for w in splitText if w not in specialCaseWords])
        returnString = []
        for w in splitText:
            if w not in specialCaseWords:
                returnString.append(w.capitalize())
            else:
                returnString.append(w)
        print(' '.join(map(str, returnString)))

        #print(returnString)
        #print("before \n" + ('[%s]' % ' '.join(map(str, splitText))))
        #return " ".join(splitText)

  
#for row, tr in enumerate
wc = Wiki_Scraper()
#race = input("What Race should I search for? ")
#wc.getRaceInformation(race)
#className = input("What Class should I search for? ")
#classFeature = input("What feature of that class should I search for? ")
#wc.getClassInformation(className,classFeature)
#spellName = input("What is the name of the Spell I should search for?")
#wc.getSpellInformation(spellName)
