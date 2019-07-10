import re
import textwrap
import requests
import urllib3
from bs4 import BeautifulSoup, Tag

import inqBot.constants as _constants


class DB_Scraper():

    """
    Constructor
    """

    def __init__(self):
        self.HEADERS = _constants.HEADERS

    """
    param: url
    return the Entire HTML code fo the website
    """

    def getEntireHTMLPage(self, url):
        page = requests.get(url, headers=self.HEADERS).text
        soup = BeautifulSoup(page, features="lxml")
        return soup

    """
    param: section, nameOfSearch
        section: specifies if user is looking for imformation about items, race, class, etc.
        nameOfSearch: what to be searched for on the search bar
    If user calls the search function on the bot, then the bot will perofrm a search on
    the search bar on dndbeyond according to the requested section
    """

    def searchDNDWebsite(self, section, nameOfSearch, specifier=""):
        rstring = "fool"
        if section == "item":
            rstring = self.getItemInformation(nameOfSearch)
        elif section == "class":
            rstring = self.getClassInformation(nameOfSearch, specifier)
        elif section == "race":
            rstring = self.getRaceInformation(nameOfSearch)
        elif section == "spell":
            rstring = self.getSpellInformation(nameOfSearch)
        elif section == "monster":
            rstring = self.getMonsterInformation(nameOfSearch)
        return rstring

    def searchDnDWebsite(self, input_list):
        return self.searchDNDWebsite(input_list[0], input_list[1], input_list[2])

    def getMonsterInformation(self, name, textOrSoup=False):
        """Go to proper page"""
        url = "https://www.5thsrd.org/gamemaster_rules/monsters/"
        name = re.sub('[^\w]', "_", name.lower())
        info_page = url + name + "/"

        http = urllib3.PoolManager()

        """Check to see if its an ACTUAL PAGE"""
        try:
            page = http.request('GET', info_page)
        except urllib3.exceptions.HTTPError:
            return "Monster Not Found"

        soup = BeautifulSoup(page.data, 'lxml')
        main_content = soup.find('div', {'role': 'main'})
        if main_content is not None:
            if textOrSoup is not False:
                return self.breakTextByLength(main_content.text)
            else:
                return main_content
        else:
            return "Monster Not Found"

    def getItemInformation(self, name):
        """Go to proper page"""
        url = "https://www.5thsrd.org/gamemaster_rules/magic_items/"
        name = re.sub('[^\w]', "_", name.lower())
        info_page = url + name + "/"

        http = urllib3.PoolManager()

        """Check to see if its an ACTUAL PAGE"""
        try:
            page = http.request('GET', info_page)
        except urllib3.exceptions.HTTPError:
            return "Monster Not Found"

        soup = BeautifulSoup(page.data, 'lxml')
        main_content = soup.find('div', {'role': 'main'})
        if main_content is not None:
            return self.breakTextByLength(main_content.text)
        else:
            return "Item Not Found"

    def getRaceInformation(self, name):
        """Go to proper page"""
        url = "https://www.5thsrd.org/character/races/"
        name = re.sub('[^\w]', "_", name.lower())
        info_page = url + name + "/"

        http = urllib3.PoolManager()

        """Check to see if its an ACTUAL PAGE"""
        try:
            page = http.request('GET', info_page)
        except urllib3.exceptions.HTTPError:
            return "Race Not Found"

        soup = BeautifulSoup(page.data, 'lxml')
        main_content = soup.find('div', {'role': 'main'})
        if main_content is not None:
            return self.breakTextByLength(main_content.text)
        else:
            return "Race Not Found"

    def getSpellInformation(self, name):
        """Go to proper page"""
        url = "http://5thsrd.org/spellcasting/spells/"
        name = re.sub('[^\w]', "_", name.lower())
        info_page = url + name + "/"

        http = urllib3.PoolManager()

        """Check to see if its an ACTUAL PAGE"""
        try:
            page = http.request('GET', info_page)
        except urllib3.exceptions.HTTPError:
            return "Spell Not Found"

        soup = BeautifulSoup(page.data, 'lxml')
        main_content = soup.find('div', {'role': 'main'})
        if main_content is not None:
            return self.breakTextByLength(main_content.text)
        else:
            return "Spell Not Found"

    def getClassInformation(self, name, specifier):
        """Go to proper page"""
        url = "https://www.5thsrd.org/character/classes/"
        name = re.sub('[^\w]', "_", name.lower())
        info_page = url + name + "/"
        specifier = self.titlize(specifier)
        info = ""
        http = urllib3.PoolManager()

        """Check to see if its an ACTUAL PAGE"""
        try:
            page = http.request('GET', info_page)
        except urllib3.exceptions.HTTPError:
            return "Class Not Found"

        soup = BeautifulSoup(page.data, 'lxml')
        main_content = soup.find('div', {'role': 'main'})
        if main_content is not None:
            headers = main_content.find_all(re.compile('^h[1-6]$'))
            if specifier == "":
                return self.breakTextByLength(main_content.text)
            elif specifier == "basic feats":
                # basic_feat_start_point = headers.find("h2", {'id': 'class-features'})
                return self.getInformationUntilNextHR(self, headers)  # nextNode)
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
                                info = self.getInformationUntilNextH2(nextNode) + "\n"
                            elif original_header_tag == "h3":
                                info = self.getInformationUntilNextH3(nextNode) + "\n"
                            elif original_header_tag == "h4":
                                info = self.getInformationUntilNextH4(nextNode) + "\n"
                            break
                return info
        else:
            return "Class not found"

    def getInformationBetweenTwoTags(self, first_tag, second_tag):
        info = ""
        nextNode = first_tag.next_sibling
        while str(nextNode) != str(second_tag):
            info = info + str(nextNode)
            nextNode = nextNode.next_sibling
        return self.breakTextByLength(info)

    def getAllInformationFromTag(self, nextNode):
        info = ""
        while True:
            nextNode = nextNode.nextSibling
            # print(nextNode)
            # print("Boo")
            if nextNode is None:
                break
            else:
                info = info + self.breakTextByLength(str(nextNode))
        return info
    """
    These next couple of functions are very general. Basically, given a starting node, they
    will pull out all information found in p tags until reached a specified tag
    """

    def getInformationUntilNextStrong(self, nextNode):
        info = ""
        while True:
            nextNode = nextNode.nextSibling
            # print(nextNode)
            # print("Boo")
            if nextNode is None:
                break
            if isinstance(nextNode, Tag):
                if nextNode.name == "strong":
                    # print("SRRRRR")
                    break
                else:
                    info = info + self.breakTextByLength(str(nextNode))
        print(info)
        print("Skr")
        # bs = BeautifulSoup(info, features="lxml")

    def getInformationUntilNextHR(self, nextNode):
        info = ""
        info = nextNode.text + "\n\n"
        while True:
            nextNode = nextNode.nextSibling
            if nextNode is None:
                break
            if isinstance(nextNode, Tag):
                if nextNode.name == "hr":
                    break
                else:
                    info = info + self.breakTextByLength(str(nextNode)) + "\n"
        return info

    def getInformationUntilNextSpan(self, nextNode):
        info = ""
        stopAt = ["div", "h1", "h2", "h3", "h4", "span"]
        while True:
            nextNode = nextNode.nextSibling
            if nextNode is None:
                break
            if isinstance(nextNode, Tag):
                if nextNode.name in stopAt:
                    break
                else:
                    info = info + self.breakTextByLength(str(nextNode)) + "\n"
        return info

    def getInformationUntilNextH1(self, nextNode):
        info = ""
        stopAt = ["div", "h1"]
        while True:
            nextNode = nextNode.nextSibling
            if nextNode is None:
                break
            if isinstance(nextNode, Tag):
                if nextNode.name in stopAt:
                    break
                else:
                    info = info + self.breakTextByLength(str(nextNode)) + "\n"
        return info

    def getInformationUntilNextH2(self, nextNode):
        info = ""
        stopAt = ["div", "h2", "h1"]
        while True:
            nextNode = nextNode.nextSibling
            if nextNode is None:
                break
            if isinstance(nextNode, Tag):
                if nextNode.name in stopAt:
                    break
                else:
                    info = info + self.breakTextByLength(str(nextNode)) + "\n"
        return info

    def getInformationUntilNextH3(self, nextNode):
        info = ""
        stopAt = ["div", "h2", "h3", "h1"]
        if nextNode is None:
            return info
        else:
            while True:
                nextNode = nextNode.nextSibling
                if nextNode is None:
                    break
                if isinstance(nextNode, Tag):
                    if nextNode.name in stopAt:
                        break
                    else:
                        info = info + self.breakTextByLength(str(nextNode)) + "\n"
        return info

    def getInformationUntilNextTable(self, nextNode):
        info = ""
        stopAt = "table"
        while True:
            nextNode = nextNode.nextSibling
            if nextNode is None:
                break
            if isinstance(nextNode, Tag):
                if nextNode.name == stopAt:
                    break
                else:
                    info = info + self.breakTextByLength(str(nextNode)) + "\n"
        return info

    def getInformationUntilNextH4(self, nextNode):
        info = ""
        stopAt = ["div", "h2", "h3", "h1", "h4"]
        while True:
            nextNode = nextNode.nextSibling
            if nextNode is None:
                break
            if isinstance(nextNode, Tag):
                if nextNode.name in stopAt:
                    break
                else:
                    info = info + self.breakTextByLength(str(nextNode)) + "\n"
        return info

    """
    breakTextByLength method
    breaks text up by length we would like on each line
    If word exceeds length, then new line is processed before
    """

    def breakTextByLength(self, text, length=150):
        if text is not None:
            text_by_line = re.split('[\r\n]', text)
            rstring = ""
            for t in text_by_line:
                if t is not None:
                    if len(t) > 149:
                        dividedText = textwrap.wrap(t, length)
                        dividedText = '\n'.join(dividedText)
                        rstring = rstring + dividedText + '\n'
                    else:
                        rstring = rstring + t + '\n'
            return rstring

    def fixSpacingOnText(self, text):
        text_by_line = text.split('\n')
        finaltext = ""
        for line in text_by_line:
            if len(line) > 2:
                line = re.sub(r'^\s+', '', line)
                finaltext = finaltext + line + "\n"
        return finaltext

    """
    titlize method
    Gives a text title format
    most words are capitalized, simple words like -> is,of,in,a,an,the, etc are not
    """

    def titlize(self, text):
        splitText = text.split()
        specialCaseWords = ["from", "so", "is", "of", "in", "a", "an", "the", "but", "for"]
        returnString = []
        for w in splitText:
            if w not in specialCaseWords:
                returnString.append(w.capitalize())
            else:
                returnString.append(w)
        return ' '.join(map(str, returnString))


"""
dd = DB_Scraper()
inp = []
inp.append(input("Item,Monster,Spell,Class,Or Race? "))
inp.append(input("Name of your search: "))
inp.append(input("specifier (leave blank for none): "))

soup = dd.searchDnDWebsite(inp)

print(soup)
"""
