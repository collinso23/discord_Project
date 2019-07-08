#from inqBot.inqGen.stats import Abilities
class Monster():
    """A template for a monster to be filled in with the user request from dndDB and stored"""

    def __init__(self):
        self.name = "Generic Monster"
        self.description = ""
        self.challenge_rating = 0
        self.armor_class = 0
        self.skills = "Perception +3, Stealth +4"
        self.senses = ""
        self.languages = ""
        """
        strength = Abilities()
        dexterity = Abilities()
        constitution = Abilities()
        intelligence = Abilities()
        wisdom = Abilities()
        charisma = Abilities()
        """
        self.speed = 30
        self.swim_speed = 0
        self.fly_speed = 0
        self.hp_max = 10
        self.hit_dice = '1d6'
