class Weapon():
    name = ""
    cost = "0 gp"
    base_damage = "1d4"
    damage_bonus = 0
    attack_bonus = 0
    damage_type = "p"
    weight = 1  # In lbs
    properties = ""
    ability = 'strength'
    is_finesse = False
    features_applied = False

    def __init__(self, wielder=None):
        self.wielder = wielder

    @classmethod
    def improved_version(cls, bonus):
        bonus = int(bonus)

        class NewWeapon(cls):
            name = f'+{bonus} ' + cls.name
            damage_bonus = bonus
            attack_bonus = bonus

        return NewWeapon

    def apply_features(self):
        if (not self.features_applied) and (self.wielder is not None):
            self.features_applied = True
            for f in self.wielder.features:
                f.weapon_func(self)

    @property
    def ability_mod(self):
        if self.wielder is None:
            return 0
        else:
            if self.is_finesse:
                return max(self.wielder.strength.modifier,
                           self.wielder.dexterity.modifier)
            else:
                return getattr(self.wielder, self.ability).modifier

    @property
    def attack_modifier(self):
        self.apply_features()
        mod = self.attack_bonus
        if self.wielder is not None:
            mod += self.ability_mod
            if self.wielder.is_proficient(self):
                mod += self.wielder.proficiency_bonus
        return mod

    @property
    def damage(self):
        self.apply_features()
        dam_str = str(self.base_damage)
        bonus = self.damage_bonus
        if self.wielder is not None:
            bonus += self.ability_mod
        if bonus != 0:
            dam_str += '{:+d}'.format(bonus)
        return dam_str

    def __str__(self):
        return self.name

    def __repr__(self):
        return "\"{:s}\"".format(self.name)


class MeleeWeapon(Weapon):
    name = "Melee Weapons"
    ability = 'strength'


class RangedWeapon(Weapon):
    name = "Ranged Weapons"
    ability = 'dexterity'


class SimpleWeapon(Weapon):
    name = "Simple Weapons"


class MartialWeapon(Weapon):
    name = "Martial Weapons"


class Quarterstaff(SimpleWeapon, MeleeWeapon):
    name = "Quarterstaff"
    cost = "2 sp"
    base_damage = "1d6"
    damage_type = "b"
    weight = 4
    properties = "Versatile (1d8)"
    ability = 'strength'
