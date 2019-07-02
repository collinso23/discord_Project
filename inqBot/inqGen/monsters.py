from .stats import Abilities

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

class GiantEagle(Monster):
    """A giant eagle is a noble creature that speaks its own language and
    understands Speech in the Common tongue. A mated pair of giant
    eagles typically has up to four eggs or young in their nest (treat
    the young as normal eagles).

    **Keen Sight:** The eagle has advantage on Wisdom (Perception)
      checks that rely on sight.

    **Multiattack:** The eagle makes two attacks: one with its beak
      and one with its talons.

    **Beak:** *Melee Weapon Attack:* +5 to hit, reach 5 ft., one
      target. *Hit:* 6 (1d6 + 3) piercing damage.

    **Talons:** *Melee Weapon Attack:* +5 to hit, reach 5 ft., one
      target. *Hit:* 10 (2d6 + 3) slashing damage.

    """
    name = "Giant eagle"
    description = "Large beast, neutral good"
    challenge_rating = 1
    armor_class = 13
    skills = "Perception +4"
    senses = "Passive perception 14"
    languages = "Giant Eagle, understands common and Auran but can't speak."
    strength = Abilities(16)
    dexterity = Abilities(17)
    constitution = Abilities(13)
    intelligence = Abilities(8)
    wisdom = Abilities(14)
    charisma = Abilities(10)
    speed = 10
    swim_speed = 0
    fly_speed = 80
    hp_max = 26
    hit_dice = '4d10+4'
