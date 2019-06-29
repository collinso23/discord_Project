from utils import dnd_scraper
from dnd_scraper import DnDScraper

class Monster():
    """A template for a monster to be filled in with the user request from dndDB and stored"""


    name = "Generic Monster"
    description = ""
    challenge_rating = 0
    armor_class = 0
    skills = "Perception +3, Stealth +4"
    senses = ""
    languages = ""
    strength = Abilities()
    dexterity = Abilities()
    constitution = Abilities()
    intelligence = Abilities()
    wisdom = Abilities()
    charisma = Abilities()
    speed = 30
    swim_speed = 0
    fly_speed = 0
    hp_max = 10
    hit_dice = '1d6'
