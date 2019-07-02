from . import features as feats


class Background():
    name = "Generic background"
    owner = None
    skill_proficiencies = ()
    weapon_proficiencies = ()
    proficiencies_text = ()
    skill_choices = ()
    num_skill_choices = 0
    features = ()
    languages = ()

    def __init__(self, owner=None):
        self.owner = owner
        cls = type(self)
        self.features = tuple([f(owner=self.owner) for f in cls.features])

    def __str__(self):
        return self.name


class Acolyte(Background):
    name = "Acolyte"
    skill_proficiencies = ('insight', 'religion')
    languages = ("[choose one]", "[choose one]")
    features = (feats.ShelterOfTheFaithful,)
