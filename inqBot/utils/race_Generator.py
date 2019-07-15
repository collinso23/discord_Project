import re

import urllib3
from bs4 import BeautifulSoup

# from inqBot.characters import race as _RACE
from inqBot.utils import srdDB_Scraper as dnds


class RaceGenerator():
    def __init__(self, soup=None):
        self.soup = soup

    """Given the main information of race page in srd DB collect that race
    information and fill race object"""

    def generate_from_page(self, _race_name):
        scraper = dnds.DB_Scraper()
        soup = self.get_race_page(_race_name)
        sub_header = soup.find_all('h1')[0]
        sub_table = soup.find_all('table')[0]
        general_information_p1 = scraper.getInformationUntilNextTable(
            sub_header)
        general_information_p2 = scraper.getInformationUntilNextH3(sub_table)
        general_information = general_information_p1 + general_information_p2

        return f"{general_information}"

    def get_race_page(self, _race_name):
        """Go to proper page"""
        scraper = dnds.DB_Scraper()
        url = "https://www.5thsrd.org/character/races/"
        name = re.sub('[^\w]', "-", _race_name.lower())
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
            return scraper.breakTextByLength(main_content.text)
        else:
            return "Race Not Found"


rg = RaceGenerator()
race_name = input("what is the name of the race: ")
rg.generate_from_page(race_name)
