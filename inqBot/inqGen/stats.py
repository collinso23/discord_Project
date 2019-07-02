import math
from collections import namedtuple
from math import ceil
from utils import DnD_DB_Scrapper
from DnD_DB_Scrapper import DnD_DB_Scrapper

def findattr(obj, name):
    """Similar to builtin getattr(obj, name) but more forgiving to
    whitespace and capitalization.

    """
    # Come up with several options
    name = name.strip()
    # check for +X weapons, armor, shields
    bonus = 0
    for i in range(1, 11):
        if (f'+{i}' in name) or (f'+ {i}' in name):
            bonus = i
            name = name.replace(f'+{i}', '').replace(f'+ {i}', '')
            break
    py_name = name.replace('-', '_').replace(' ', '_').replace("'", "")
    camel_case = "".join([s.capitalize() for s in py_name.split('_')])
    if hasattr(obj, py_name):
        # Direct lookup
        attr = getattr(obj, py_name)
    elif hasattr(obj, camel_case):
        # CamelCase lookup
        attr = getattr(obj, camel_case)
    else:
        raise AttributeError(f'{obj} has no attribute {name}')
    if bonus > 0:
        if issubclass(attr, Weapon) or issubclass(attr, Shield) or issubclass(attr, Armor):
            attr = attr.improved_version(bonus)
    return attr

def mod_str(modifier):
    """Converts a modifier to a string, eg 2 -> '+2'."""
    return '{:+d}'.format(modifier)
    if modifier == 0:
        return str(modifier)
    else:
        return '{:+}'.format(modifier)

AbilityScore = namedtuple('AbilityScore',
                          ('value', 'modifier', 'saving_throw'))

class Abilities():
    """abilities of a character"""
    ablitiy_name= None

    def __init__(self,default_stat=10):
        self.default_stat = default_stat

    def __set_name__(self,superplayer,name):
        self.ability_name = name

    def _check_dict(self, obj):
        if not hasattr(obj, '_ability_scores'):
            # No ability score dictionary exists
            obj._ability_scores = {
                self.ability_name: self.default_value
            }
        elif self.ability_name not in obj._ability_scores.keys():
            # ability score dictionary exists but doesn't have this ability
            obj._ability_scores[self.ability_name] = self.default_value

    def __get__(self,superplayer,Character):
        self._check_dict(superplayer)
        score = superplayer._ability_scores[self.ability_name]
        modifier = math.floor((score - 10)/2)
        saving_throw = modifier
        if self.ability_name is not None and hasattr(superplayer,'saving_throw_proficiencies'):
            is_proficient = (self.ability_name in superplayer.saving_throw_proficiencies)
            if is_proficient:
                saving_throw += superplayer.profenciey_bonus
            value = AbilityScore(modifier=modifier,value=score,saving_throw=saving_throw)
            return value

    def __set__(self,superplayer,val):
        self._check_dict(superplayer)
        superplayer._ability_scores[self.ability_name] = val
        self.value = val

class Skill():
    """skills of a character"""
    def __init__(self,ability):
        self.ability_name=ability

    def __set_name__(self,superplayer,name):
        self.skill_name=name.lower().replace('_',' ')
        self.superplayer = superplayer

    def __get__(self,superplayer,owner):
        ability = getattr(superplayer,self.ability_name)
        modifier = ability.modifier
        if is_proficient:
            modifier+=superplayer.profenciey_bonus
        has_expertise = self.skill_name in superplayer.skill_expertise
        if is_expert:
            modifier += superplayer.profenciey_bonus
        return modifier

class ArmorClass():
    """characters armor class"""
    def __get__(self,char,Character):
        armor = char.armor or NoArmor()
        ac = armor.base_armor_class
        # calculate and apply modifiers
        if armor.dexterity_mod_max is None:
            ac += char.dexterity.modifier
        else:
            ac += min(char.dexterity.modifier, armor.dexterity_mod_max)
        shield = char.shield or NoShield()
        ac += shield.base_armor_class

class Speed():
    """speed of character"""
    def __get__(self,char, Character):
        speed = char.race.speed
        other_speed = speed[2:]
        if isinstance(speed,str):
            other_speed = speed[2:]
            speed = int(speed[:2])
        return '{:d}{:s}'.format(speed, other_speed)

class Initiative():
    """ a characters Initiative"""
    def __get__(self,char,Character):
        initiative = char.dexterity.modifier
        return '{:+d}'.format(initiative)
