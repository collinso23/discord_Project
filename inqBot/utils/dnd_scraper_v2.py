import logging
import pdb
import re
import textwrap

import requests
import urllib3
from bs4 import BeautifulSoup, Tag

import inqBot.constants as _constants

logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s',
                    level=logging.DEBUG)
"""
breakTextByLength method
breaks text up by length we would like on each line
If word exceeds length, then new line is processed before
"""


def breakTextByLength(text, length=150):
    try:
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
    except Exception as err:
        return logging.debug(f"Error breaking text:\n {err}")


def fixSpacingOnText(self, text):
    try:
        text_by_line = text.split('\n')
        finaltext = ""
        for line in text_by_line:
            if len(line) > 2:
                line = re.sub(r'^\s+', '', line)
                finaltext = finaltext + line + "\n"
        return finaltext
    except Exception as err:
        return logging.debug(f"Error fixing spacing on text:\n {err}")


"""
titlize method
Gives a text title format
most words are capitalized, simple words like -> is,of,in,a,an,the, etc are not
"""


def titlize(self, text):
    try:
        splitText = text.split()
        specialCaseWords = [
            "from", "so", "is", "of", "in", "a", "an", "the", "but", "for"
        ]
        returnString = []
        for w in splitText:
            if w not in specialCaseWords:
                returnString.append(w.capitalize())
            else:
                returnString.append(w)
        return ' '.join(map(str, returnString))
    except Exception as err:
        return logging.debug(f"Error titlizing text:\n {err}")


"""
Scrapes from dnd beyond for races to input into player race class
"""

pdb.set_trace()


class beyondScraper():
    """Constructor"""

    def __init__(self):
        self.HEADERS = _constants.HEADERS

    def gen_Page_HTML(self, url):
        try:
            page = requests.get(url, headers=self.HEADERS).text
            soup = BeautifulSoup(page, features="lxml")
            return soup
        except Exception as err:
            return logging.debug(f"Error getting page html:\n {err}")

    """
    param: section, nameOfSearch
        section: specifies if user is looking for imformation about items, race, class, etc.
        nameOfSearch: what to be searched for on the search bar
    If user calls the search function on the bot, then the bot will perofrm a search on
    the search bar on dndbeyond according to the requested section
    """

    def beyond_Search(self, section, search_name, specifier=""):
        rstring = f"unable to complete search: {search_name}, opps!"
        _section = section.lower()
        if _section == "race":
            rstring = self.get_Race_Information(search_name)
        return logging.debug(f"{rstring}")

    def get_Race_Information(self, _search_name, textOrSoup=False):
        """Go to page"""
        url = "https://www.dndbeyond.com/races/"
        _search_name = re.sub('[^\w]', "-", _search_name.lower())
        indexed_page = url + _search_name

        http = urllib3.PoolManager()
        """Verify Page exists"""
        try:
            page = http.request('GET', indexed_page)
        except urllib3.exceptions.HTTPError:
            _error = logging.debug(f"Unable to find page: \n")
            return f"{_error}"
        soup = BeautifulSoup(page.data, 'lxml')
        main_content = soup.find('div', {'id': 'content'})
        if main_content is not None:
            return breakTextByLength(main_content.text)
        else:
            _error = logging.debug("unable to find main_content\n")
            return f"{_error}"


dd = beyondScraper()
inp = []
inp.append("RACE")
inp.append(input("Name of race: "))
inp.append(input("specifier (leave blank for none): "))
soup = dd.beyond_Search(inp[0], inp[1], inp[2])
