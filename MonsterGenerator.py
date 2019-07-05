from bs4 import BeautifulSoup, SoupStrainer, Tag
import requests
import lxml
import re
import urllib3
import textwrap
from nltk import tokenize
import constants
from inqBot import characters
import monsters as m
import DnD_DB_Scrapper as dnds

class MonsterGenerator(object):

    def __init__(self,soup=None):
        self.soup = soup

    """Given the main information of a monster page in the
    DnD database, this will generate that specific monster
    """
    def generate_from_soup(self,soup=None):
        scrapper = dnds.DnD_DB_Scrapper()
        main_header = soup.find_all("h1")[0]
        table = soup.find_all('table')[0]

        """Gets information such as ac, hp, speed,senses,languages, and features"""
        general_information_p1 = scrapper.getInformationUntilNextTable(main_header)
        general_information_p2 = scrapper.getInformationUntilNextH3(table)
        general_information = general_information_p1 + general_information_p2

        #print(general_information)

        """Gets actions of monster"""
        actions_header = soup.find('h3',{'id':'actions'})
        monster_actions = scrapper.getInformationUntilNextH1(actions_header)

        """creates soups of the general information and monster actions"""
        general_information_soup = BeautifulSoup(general_information,features="lxml")
        monster_actions_soup = BeautifulSoup(monster_actions,features="lxml")

        monster = self.createMonster(main_header,general_information_soup,monster_actions_soup)
        print(monster.languages)
        print(monster.skills)
        print(monster.description)
        print(monster.hit_dice)
        print(str(monster.armor_class))
        print(str(monster.hp_max))
        print(str(monster.speed))
        print(str(monster.fly_speed))
        print(str(monster.swim_speed))


    """
    createMonster function
    creates a monster class containing the information extracted from page
    """
    def createMonster(self,name,general_information,actions):
        monster = m.Monster()
        monster.name = name.text

        def extractHPInformation(hp_info):
            maxhp_and_die = hp_info.split()
            maxhp_and_die[1] = re.sub('[()]','',maxhp_and_die[1])
            return maxhp_and_die

        def extractSpeedInformation(speed_info):
            speed_swim_fly = speed_info.split(",")
            speed = speed_swim_fly[0]
            swim = 0
            fly = 0
            for component in speed_swim_fly:
                if "swim" in component:
                    swim = int(re.findall('\d+',component)[0])
                elif "fly" in component:
                    fly = int(re.findall('\d+',component)[0])
            speed_swim_fly_dict = {"speed":speed,"swim":swim,"fly":fly}
            return speed_swim_fly_dict

        counter = 0
        for p in general_information.find_all("p"):
            if counter == 0:
                monster.description = p.text
            elif counter == 1:
                for strong in p.find_all("strong"):
                    if strong.text == "Armor Class":
                        monster.armor_class = strong.nextSibling
                    elif strong.text == "Hit Points":
                        hp_information = extractHPInformation(strong.nextSibling)
                        monster.hp_max = int(hp_information[0])
                        monster.hit_dice = hp_information[2]
                    elif strong.text == "Speed":
                        speed_information = extractSpeedInformation(strong.nextSibling)
                        monster.speed = speed_information["speed"]
                        monster.swim_speed = speed_information["swim"]
                        monster.fly_speed = speed_information["fly"]
            elif counter == 2:
                for strong in p.find_all("strong"):
                    if strong.text == "Skills":
                        monster.skills = strong.nextSibling
                    elif strong.text == "Senses":
                        monster.senses = strong.nextSibling
                    elif strong.text == "Languages":
                        monster.languages = strong.nextSibling
                    elif strong.text == "Challenge":
                        monster.challenge_rating = int(strong.nextSibling.split()[0])
            counter += 1
        return monster
dd = dnds.DnD_DB_Scrapper()
nameOfMonster = input("What is the name of the monster?")
soup = dd.getMonsterInformation(nameOfMonster,1)
mg = MonsterGenerator()
mg.generate_from_soup(soup)
