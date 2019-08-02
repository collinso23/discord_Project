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
#from characters import character as c
"""
"""
class Character_Generator(object):

    def __init__(self):
        self.chracter_creation_time = 'Created On: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now())
        self.race_list = ["Human","Half-Elf","Elf","Dwarf","Gnome","Hafling",
        "Dragonborn","Tiefling","Half-Orc"]
        self.class_list = ["Barbarian","Bard","Cleric","Druid","Fighter",
        "Monk","Paladin","Ranger","Rogue","Sorcerer","Warlock","Wizard"]
        self.ability_list = {"Strenth":None,"Constitution":None,"Dexterity":None,"Wisdom":None,"intelligence":None,"Charisma":None}

    def create_new_character(self,user):

        """Creates the list for the output of the ui"""
        race_pref = input("What race would you prefer to be?\n" + self.race_list_output() + "\n")
        class_pref = input("\n-----------------------------------\nwhat class would you prefer to be?\n" + self.class_list_output() + "\n")
        ability_pref = input(self.ability_list_output())

        """
        race_pref = input("\n1) Human\n2) Half-Elf\n3) Elf\n4) Dwarf\n5) Gnome\n6) Hafling\n7) Dragonborn\n8) Tiefling\n9) Half-Orc)
        class_pref = input("what class do you prefer to be?\n")
        race./character_details
        class./level./equipment
        abilityscores 15,14,13,12,10,8 or custom"""
        #return race_pref_question

    def race_list_output(self):
        return '\n'.join(list((str(i) + ") " + self.race_list[i-1] for i in range(1,len(self.race_list)+1))))

    def class_list_output(self):
        return '\n'.join(list((str(i) + ") " + self.class_list[i-1] for i in range(1,len(self.class_list)+1))))

    """This function needs to contain some logic.
    It needs to first loop through all the ability scores
    and update the value according to user input and output that on
    the selection"""
    def ability_list_output(self):
        standard_array = [15,14,13,12,10,8]

        standard_array_commas_str = ' , '.join(list(map(str, standard_array)))
        arrow = " -> "
        counter  = 0
        ability_value = 1
        while True:
            print("Choose ability score values for standard array.\n")
            print("----------"+ standard_array_commas_str + "----------")
            for x, y in self.ability_list.items():
                counter += 1
                item_pr = str(counter)+") "+ x
                if y is None:
                    item_pr += "\n"
                else:
                    item_pr += arrow + str(y)+"\n"
                print(item_pr)
            while True:
                try:
                    ability_choice = int(input())-1
                    break
                except:
                    print("Please enter a proper value")

            """At this point, we have outprinted the selection
            of abilities as well as taken in the user's preference
            for which ability should the highest available value
            belong to. At this point we have to check these scenarios:
            if: the  value of key is None, then place next highest available
            value to key
            if: value of the key is not None, take the value on the key,
            place it in the available values list, and rank it greatest to least
            if: user inputted 0, check if all keys have a proper value and if so
            exit."""
            counter = 0
            if ability_choice == -1:
                if not standard_array:
                    break
                else:
                    print("All the abilities do not have a value yet!")

            try:
                value_ability = list(self.ability_list.values())[ability_choice]
            except IndexError:
                print("incorrect input. please choose between 1-6")

            if value_ability == None:
                self.ability_list[list(self.ability_list.keys())[ability_choice]] = standard_array[0]
                del standard_array[0]

            elif value_ability != None:
                standard_array.append(ability_list[self.ability_list.keys()[ability_choice]])
                standard_array.sort()
                ability_list[list(self.ability_list.keys())[ability_choice]] = None













c = Character_Generator()
print(c.create_new_character("boo"))
