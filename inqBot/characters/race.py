from collections import defaultdict


class Race():
    name = "Unknown"
    size = "medium"
    speed = 30
    owner = None
    languages = ('Common', )
    subrace = "None"
    proficiencies_text = []
    weapon_proficiences = []
    skill_proficiencies = ()
    skill_choices = ()
    num_skill_choices = 0
    features = ()
    features_by_level = defaultdict(list)
    spells_known = ()

    def __init__(self, owner=None):
        self.owner = owner
        cls = type(self)
        # Instantiate the features
        self.features = tuple([f(owner=self.owner) for f in cls.features])
        self.features_by_level = defaultdict(list)
        for i in range(1, 21):
            self.features_by_level[i] = [
                f(owner=self.owner) for f in cls.features_by_level[i]
            ]
        self.spells_known = [S() for S in cls.spells_known]

    @property
    def spells_prepared(self):
        return self.spells_known

    def __str__(self):
        return self.name

    def __repr__(self):
        return "\"{:s}\"".format(self.name)


"""Below inforamtion is for testing character generation will need to be replaced with scraped information"""
# Humans for testing purpose


class Human(Race):
    name = "Human"
    size = "medium"
    speed = 30
    strength_bonus = 1
    dexterity_bonus = 1
    constitution_bonus = 1
    intelligence_bonus = 1
    wisdom_bonus = 1
    charisma_bonus = 1
    languages = ("Common", '[choose one]')


"""


available_races = [Human]

__all__ = tuple([r.name for r in available_races] + ('available_races'))
"""
