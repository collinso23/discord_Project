import os, sys

#'/home/user/example/parent/child'
current_path = os.path.abspath('.')

#'/home/user/example/parent'
parent_path = os.path.dirname(current_path)

sys.path.append(parent_path)

import DnD_DB_Scrapper as dnds
from bs4 import BeautifulSoup, SoupStrainer, Tag
import requests
import lxml
import json
import datetime
from characters import character as c
"""
"""
class Character_Generator(object):

    def __init__(self):
        self.chracter_creation_time = 'Created On: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now())
        self.race_list = ["Human","Half-Elf","Elf","Dwarf","Gnome","Hafling",
        "Dragonborn","Tiefling","Half-Orc"]

    def create_new_character(self,user):

        """Creates the list for the output of the ui"""
        generator_fun_race = list((str(i) + ") " + self.race_list[i] for i in range(len(self.race_list))))
        race_pref_question = f"what race do you prefer to be?\n{'\n'.join(generator_fun_race)}"
        race_pref = input("\n1) Human\n2) Half-Elf\n3) Elf\n4) Dwarf\n5) Gnome\n6) Hafling\n7) Dragonborn\n8) Tiefling\n9) Half-Orc)
        class_pref = input("what class do you prefer to be?\n")
        race./character_details
        class./level./equipment
        abilityscores 15,14,13,12,10,8 or custom
