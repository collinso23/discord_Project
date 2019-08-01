import os, sys

#'/home/user/example/parent/child'
current_path = os.path.abspath('.')

#'/home/user/example/parent'
parent_path = os.path.dirname(current_path)

sys.path.append(parent_path)


import character_stats
from utils import dice

class Adventurer(object):
    """
    """
    def __init__(self,character_details,race,class_,level = 1,xp = 0):
        self.character_details = character_details
        self.race = race
        self.class_ = class_
        self.level = level
        self.xp = xp

class Character(Adventurer):

    """
    """
    def __init__(self,character_details,race,class_,user_name,level,xp):
        Adventurer.__init__(self,character_details,race,class_)
        self.user_name = user_name

        """All the die the user will ever need to use in dnd"""
        self.d2 = dice.Die(2)
        self.d4 = dice.Die(4)
        self.d6 = dice.Die(6)
        self.d8 =  dice.Die(8)
        self.d12 = dice.Die(12)
        self.d20 = dice.Die(20)
        self.d100 = dice.Die(100)
