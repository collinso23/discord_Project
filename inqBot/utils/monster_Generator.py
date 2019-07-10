import os
import sys

current_path = os.path.abspath('.')

parent_path = os.path.dirname(current_path)

sys.path.append(parent_path)

from bs4 import BeautifulSoup
import re
from inqBot.characters import monsters as mon
from inqBot.utils import srdDB_Scraper as dnds
import json


class MonsterGenerator(object):

    def __init__(self, soup=None):
        self.soup = soup

    """Given the main information of a monster page in the
    DnD database, this will generate that specific monster
    """

    def generate_from_soup(self, soup=None):
        scrapper = dnds.DnD_DB_Scrapper()
        main_header = soup.find_all("h1")[0]
        table = soup.find_all('table')[0]

        """Gets information such as ac, hp, speed,senses,languages, and features"""
        general_information_p1 = scrapper.getInformationUntilNextTable(main_header)
        general_information_p2 = scrapper.getInformationUntilNextH3(table)
        general_information = general_information_p1 + general_information_p2

        # print(general_information)

        """Gets actions of monster"""
        actions_header = soup.find('h3', {'id': 'actions'})
        monster_actions = scrapper.getInformationUntilNextH3(actions_header)
        """Gets Reactions of monster"""
        reactions_header = soup.find('h3', {'id': 'reactions'})
        monster_reactions = scrapper.getInformationUntilNextH3(reactions_header)
        """Gets Description of monster"""
        description_header = soup.find('h3', {'id': 'description'})
        monster_description = scrapper.getInformationUntilNextH3(description_header)

        """creates soups of the general information, monster actions, reactions, and description"""
        general_information_soup = BeautifulSoup(general_information, features="lxml")
        monster_actions_soup = BeautifulSoup(monster_actions, features="lxml")
        monster_reactions_soup = BeautifulSoup(monster_reactions, features="lxml")
        monster_description_soup = BeautifulSoup(monster_description, features="lxml")

        monster = self.createMonster(main_header, general_information_soup, table,
                                     monster_actions_soup, monster_reactions_soup, monster_description_soup)
        monster.printInformation()

    """
    createMonster function
    creates a monster class containing the information extracted from page
    """

    def createMonster(self, name, general_information, table_information, actions, reactions, description):
        monster = mon.Monster()
        scrapper = dnds.DnD_DB_Scrapper()
        monster.name = name.text

        """Extracts proper information from hp info scrapped from database"""

        def extractHPInformation(hp_info):
            maxhp_and_die = hp_info.split()
            die_information = ''.join(maxhp_and_die[1:])
            die_information = re.sub('[()]', '', die_information)
            maxhp_and_die = [maxhp_and_die[0], die_information]
            return maxhp_and_die

        """From the scrapped information concerning speed, we malliluate
        it to best fit the monster class"""

        def extractSpeedInformation(speed_info):
            speed_swim_fly = speed_info.split(",")
            speed = int(re.findall('\d+', speed_swim_fly[0])[0])
            swim = 0
            fly = 0
            for component in speed_swim_fly:
                if "swim" in component:
                    swim = int(re.findall('\d+', component)[0])
                elif "fly" in component:
                    fly = int(re.findall('\d+', component)[0])
            speed_swim_fly_dict = {"speed": speed, "swim": swim, "fly": fly}
            return speed_swim_fly_dict

        def extractAbilityInformation(ability_info):
            td_scores = ability_info.find_all("tr")[1].find_all("td")
            scores = []
            for s in td_scores:
                scores.append(int(s.text.split()[0]))
            return scores

        """This section of the createMonster function takes the scrapped
        general information from the database and applies it to the monster
        class
        General information is: Name, Armor Class, Hit Points, Speeds, Saving Throws,
        Senses, Languages, Challenge"""
        counter = 0
        all_paragraphs = general_information.find_all("p")
        for p in all_paragraphs:
            if counter == 0:
                monster.description = p.text
            elif counter == 1:
                for strong in p.find_all("strong"):
                    if strong.text == "Armor Class":
                        monster.armor_class = int(strong.nextSibling.split()[0])
                    elif strong.text == "Hit Points":
                        hp_information = extractHPInformation(strong.nextSibling)
                        monster.hp_max = int(hp_information[0])
                        monster.hit_dice = hp_information[1]
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
                    elif strong.text == "Saving Throws":
                        monster.saving_throws = strong.nextSibling.lstrip()
            elif counter == 3:
                for strong in p.find_all("strong"):
                    monster.features.update({strong.text: strong.nextSibling})

            counter += 1

        """This section extracts the information from the table and puts the
        ability information to the monster"""
        ability_scores = extractAbilityInformation(table_information)
        monster.updateAbilityScores(ability_scores)

        all_actions = actions.find_all("strong")
        """This gets all the actions BUT the last one"""
        for action in range(len(all_actions) - 1):
            action_description = scrapper.getInformationBetweenTwoTags(
                all_actions[action], all_actions[action + 1])
            action_description_soup = BeautifulSoup(action_description, features="lxml")
            monster.actions.update({all_actions[action].text: action_description_soup.text.strip()})

        """Adds the last actions"""
        last_action = all_actions[-1]
        last_action_description_soup = BeautifulSoup(
            scrapper.getAllInformationFromTag(last_action), features="lxml")
        last_action_description = last_action_description_soup.text

        monster.actions.update({last_action.text: last_action_description.strip()})
        """Sets Reactions of Monster"""
        if reactions is not None:
            for strong in reactions.find_all("strong"):
                monster.reactions.update({strong.text: strong.nextSibling.strip()})

        """Adds to description if there is description header"""
        monster.description = monster.description + "\n" + description.text.strip()
        return monster


dd = dnds.DnD_DB_Scrapper()
nameOfMonster = input("What is the name of the monster?")
soup = dd.getMonsterInformation(nameOfMonster, 1)
mg = MonsterGenerator()
mg.generate_from_soup(soup)
