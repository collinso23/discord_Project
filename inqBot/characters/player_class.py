class SuperPlayer(object):

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

    def __init__(self,player_info,ability_info,inventory_info):
        self.stats=ability_info
        self.player=player_info
        self.inventory=inventory_info

    def get_modifier(self):
        return

    def _get_passive_wisdom(self):
        passive_Wisdom = 8 + profenciey_bonus + widsom
