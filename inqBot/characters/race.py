from collections import defaultdict

class Race():
    name = "Unknown"
    size = "medium"
    speed = 30
    owner = None
    languages = ('Common', )
    proficiencies_text = tuple()
    weapon_proficiences = tuple()
    skill_proficiencies = ()
    skill_choices = ()
    num_skill_choices = 0
    features = tuple()
    features_by_level = defaultdict(list)
    strength_bonus = 0
    dexterity_bonus = 0
    constitution_bonus = 0
    intelligence_bonus = 0
    wisdom_bonus = 0
    charisma_bonus = 0
    hit_point_bonus = 0
    spells_known = ()

    def __init__(self, owner=None):
        self.owner = owner
        cls = type(self)
        # Instantiate the features
        self.features = tuple([f(owner=self.owner) for f in cls.features])
        self.features_by_level = defaultdict(list)
        for i in range(1, 21):
            self.features_by_level[i] = [f(owner=self.owner)for f in
                                         cls.features_by_level[i]]
        self.spells_known = [S() for S in cls.spells_known]

    @property
    def spells_prepared(self):
        return self.spells_known

    def __str__(self):
        return self.name

    def __repr__(self):
        return "\"{:s}\"".format(self.name)
