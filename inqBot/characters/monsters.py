import os, sys

#'/home/user/example/parent/child'
current_path = os.path.abspath('.')

#'/home/user/example/parent'
parent_path = os.path.dirname(current_path)


import json

class Ability(object):
    """A simple Ability class which calculates the modifier and actual score"""

    def __init__(self, score=10):
        self.score = score
        self.modifier = int((self.score-10)/2)

    def __set__(self, score):
        self.score = score
        self.modifier = int((self.score-10)/2)

    def __str__(self):
        return_string = str(self.score) + "({:+})".format(self.modifier)
        return return_string

class Monster(object):
    """A template for a monster to be filled in with the user request from dndDB and stored"""

    def __init__(self):
        self.name = "Generic Monster"
        self.description = ""
        self.challenge_rating = 0
        self.armor_class = 0
        self.skills = "Perception +3, Stealth +4"
        self.senses = ""
        self.languages = ""
        strength = Ability()
        dexterity = Ability()
        constitution = Ability()
        intelligence = Ability()
        wisdom = Ability()
        charisma = Ability()
        self.speed = 30
        self.swim_speed = 0
        self.fly_speed = 0
        self.hp_max = 10
        self.hit_dice = '1d6'
        self.saving_throws = "Dex +0"
        self.features = {}
        self.actions = {}
        self.reactions = {}
    def updateAbilityScores(self, scores_list):
        strength = scores_list[0]
        dexterity = scores_list[1]
        constitution = scores_list[2]
        intelligence = scores_list[3]
        wisdom = scores_list[4]
        charisma = scores_list[5]

    def printInformation(self):
        print("Languges:\n")
        print(self.languages)
        print("-----------------------------------------\n")

        print("Skills:\n")
        print(self.skills)
        print("-----------------------------------------\n")

        print("Description:\n")
        print(self.description)
        print("-----------------------------------------\n")

        print("Hit Dice:\n")
        print(self.hit_dice)
        print("-----------------------------------------\n")

        print("Armor Class:\n")
        print(str(self.armor_class))
        print("-----------------------------------------\n")

        print("Max HP:\n")
        print(str(self.hp_max))
        print("-----------------------------------------\n")

        print("Speed:\n")
        print(str(self.speed))
        print("-----------------------------------------\n")

        print("Fly Speed:\n")
        print(str(self.fly_speed))
        print("-----------------------------------------\n")

        print("Swim Speed:\n")
        print(str(self.swim_speed))
        print("-----------------------------------------\n")

        print("Saving Throws:\n")
        print(self.saving_throws)
        print("-----------------------------------------\n")

        print("Features:\n")
        print(json.dumps(self.features,indent = 4))
        print("-----------------------------------------\n")

        print("Actions:\n")
        print(json.dumps(self.actions,indent = 4))
        print("-----------------------------------------\n")

        print("Reactions:\n")
        print(json.dumps(self.reactions,indent = 4))
        print("-----------------------------------------\n")
