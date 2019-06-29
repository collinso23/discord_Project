from .stats import Ability, Skill, findattr, ArmorClass, Speed, Initiative
from . import race,armor,monsters
from .armor import Armor,NoArmor,Shield,NoShield

multiclass_spellslots_by_level = {
    # char_lvl: (cantrips, 1st, 2nd, 3rd, ...)
    1:  (0, 2, 0, 0, 0, 0, 0, 0, 0, 0),
    2:  (0, 3, 0, 0, 0, 0, 0, 0, 0, 0),
    3:  (0, 4, 2, 0, 0, 0, 0, 0, 0, 0),
    4:  (0, 4, 3, 0, 0, 0, 0, 0, 0, 0),
    5:  (0, 4, 3, 2, 0, 0, 0, 0, 0, 0),
    6:  (0, 4, 3, 3, 0, 0, 0, 0, 0, 0),
    7:  (0, 4, 3, 3, 1, 0, 0, 0, 0, 0),
    8:  (0, 4, 3, 3, 2, 0, 0, 0, 0, 0),
    9:  (0, 4, 3, 3, 3, 1, 0, 0, 0, 0),
    10: (0, 4, 3, 3, 3, 2, 0, 0, 0, 0),
    11: (0, 4, 3, 3, 3, 2, 1, 0, 0, 0),
    12: (0, 4, 3, 3, 3, 2, 1, 0, 0, 0),
    13: (0, 4, 3, 3, 3, 2, 1, 1, 0, 0),
    14: (0, 4, 3, 3, 3, 2, 1, 1, 0, 0),
    15: (0, 4, 3, 3, 3, 2, 1, 1, 1, 0),
    16: (0, 4, 3, 3, 3, 2, 1, 1, 1, 0),
    17: (0, 4, 3, 3, 3, 2, 1, 1, 1, 1),
    18: (0, 4, 3, 3, 3, 3, 1, 1, 1, 1),
    19: (0, 4, 3, 3, 3, 3, 2, 1, 1, 1),
    20: (0, 4, 3, 3, 3, 3, 2, 2, 1, 1),
}

class Character(object):
    name = ""
    player_name = ""
    alignment = "Neutral"
    class_list = list()
    _race = None
    _background = None
    xp = 0
    level = 0

    # Hit points
    hp_max = 10

    # Base stats (ability scores)
    strength = Ability()
    dexterity = Ability()
    constitution = Ability()
    intelligence = Ability()
    wisdom = Ability()
    charisma = Ability()
    armor_class = ArmorClass()
    initiative = Initiative()
    speed = Speed()
    inspiration = 0
    _saving_throw_proficiencies = tuple()  # use to overwrite class proficiencies
    other_weapon_proficiencies = tuple()  # add to class/race proficiencies
    skill_proficiencies = list()
    skill_expertise = list()
    languages = ""

    # Skills
    acrobatics = Skill(ability='dexterity')
    animal_handling = Skill(ability='wisdom')
    arcana = Skill(ability='intelligence')
    athletics = Skill(ability='strength')
    deception = Skill(ability='charisma')
    history = Skill(ability='intelligence')
    insight = Skill(ability='wisdom')
    intimidation = Skill(ability='charisma')
    investigation = Skill(ability='intelligence')
    medicine = Skill(ability='wisdom')
    nature = Skill(ability='intelligence')
    perception = Skill(ability='wisdom')
    performance = Skill(ability='charisma')
    persuasion = Skill(ability='charisma')
    religion = Skill(ability='intelligence')
    sleight_of_hand = Skill(ability='dexterity')
    stealth = Skill(ability='dexterity')
    survival = Skill(ability='wisdom')

    # Characteristics
    attacks_and_spellcasting = ""
    personality_traits = "TODO: Describe how your character behaves, interacts with others"
    ideals = "TODO: Describe what values your character believes in."
    bonds = "TODO: Describe your character's commitments or ongoing quests."
    flaws = "TODO: Describe your character's interesting flaws."
    features_and_traits = "Describe any other features and abilities."

    # Inventory
    cp = 0
    sp = 0
    ep = 0
    gp = 0
    pp = 0
    equipment = ""
    weapons = list()
    magic_items = list()
    armor = None
    shield = None
    _proficiencies_text = list()
    # Magic
    spellcasting_ability = None
    _spells = list()
    _spells_prepared = list()
    # Features IN MAJOR DEVELOPMENT
    custom_features = list()
    feature_choices = list()

    def __init__(self,**attrs):
        """Take a variable number of attriubutes and pass them to set_attrs function """
        self.clear()
        my_classes = attrs.pop('classes',[])
        my_levels = attrs.pop('levels',[])
        my_subclasses = attrs.pop('subclasses',[])
        if (len(my_classes) == 0):
            if ('class' in attrs):
                my_classes = [attrs.pop('class')]
                my_levels = [attrs.pop('level', 1)]
                my_subclasses = [attrs.pop('subclass', None)]
            else:
                my_classes = ['Fighter']
                my_levels = [1]
                my_subclasses = [None]

        self.race = attrs.pop('race', None)
        self.background = attrs.pop('background', None)
        # parse all other attributes
        self.set_attrs(**attrs)

     def clear(self):
        # reset class-definied items
        self.class_list = list()
        self.weapons = list()
        self.magic_items = list()
        self._saving_throw_proficiencies = tuple()
        self.other_weapon_proficiencies = tuple()
        self.skill_proficiencies = list()
        self.skill_expertise = list()
        self._proficiencies_text = list()
        self._spells = list()
        self._spells_prepared = list()
        self.custom_features = list()
        self.feature_choices = list()

    @property
    def race(self):
        return self._race

    @property
    def background(self):
        return self._background

    @property
    def class_name(self):
        if self.num_classes >= 1:
            return self.primary_class.name
        else:
            return ""

    @property
    def classes_and_levels(self):
        return ' / '.join([f'{c.name} {c.level}'
                           for c in self.class_list])

    @property
    def class_names(self):
        return [c.name for c in self.class_list]

    @property
    def levels(self):
        return [c.level for c in self.class_list]

    @property
    def subclasses(self):
        return list([c.subclass or '' for c in self.class_list])

    @property
    def level(self):
        return sum(c.level for c in self.class_list)

    @property
    def num_classes(self):
        return len(self.class_list)

    @property
    def has_class(self):
        return (self.num_classes > 0)

    @property
    def primary_class(self):
        # for now, assume first class given must be primary class
        if self.has_class:
            return self.class_list[0]
        else:
            return None
    @property
    def weapon_proficiencies(self):
        wp = set(self.other_weapon_proficiencies)
        if self.num_classes > 0:
            wp |= set(self.primary_class.weapon_proficiencies)
        if self.num_classes > 1:
            for c in self.class_list[1:]:
                wp |= set(c.multiclass_weapon_proficiencies)
        if self.race is not None:
            wp |= set(getattr(self.race, 'weapon_proficiencies', ()))
        if self.background is not None:
            wp |= set(getattr(self.background, 'weapon_proficiencies', ()))
            return tuple(wp)

    @property
    def saving_throw_proficiencies(self):
        if self.primary_class is None:
            return self._saving_throw_proficiencies
        else:
            return (self._saving_throw_proficiencies or
                    self.primary_class.saving_throw_proficiencies)






"""
    ability_info = {
        "strength": "",
        "dexterity": "",
        "intelligence":"",
        "wisdom":"",
        "charisma":"",
        "skill_proficiencies":[],
        "weapon_proficiencies":[]
    }

    player_info = {
        "player_name":"",
        "level": [],
        "race":"",
        "class":[],
        "subclass":[],
        "background":"",
        "allignment":"",
        "xp":""
    }

    inventory_info={
        "weapons":[],
        "magic_weapons":[],
        "armor": "",
        "shield": "",
        "currency":[],
        "equipment":""
    }

    spell_info={
        "spell_list":[],
        "prepared_spells":[],
        "spell_slots":{"spell_level":""},

    }
"""
