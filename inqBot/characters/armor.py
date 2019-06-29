class Shield():
    name = "Shield"
    base_armor_class = 2

class Armor():
    name = "Unknown Armor"
    cost = "0 gp"
    base_armor_class = 10
    dexterity_mod_max = None
    strength_required = None
    stealth_disadvantage = False
    weight = 0 # In lb


class NoArmor(Armor):
    name = "No Armor"


class LightArmor(Armor):
    name = "Light Armor"


class MediumArmor(Armor):
    name = "Medium Armor"


class HeavyArmor(Armor):
    name = "Heavy Armor"
    stealth_disadvantage=True
