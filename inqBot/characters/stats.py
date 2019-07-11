class Ability(object):
    """A simple Ability class which calculates the modifier and actual score"""

    def __init__(self, name, score=10):
        self.name = name

        self.score = score
        self.modifier = int((self.score - 10) / 2)
        self.list_of_skills = self.createAbilities(self.name)

    def __set__(self, score):
        self.score = score
        self.modifier = int((self.score - 10) / 2)

    def __str__(self):
        return_string = str(self.score) + "({:+})".format(self.modifier)
        return return_string

    def createAbilities(self, name):
        list_of_skills = {}
        if name == "str":
            list_of_skills.update("atheltics", Skill("atheltics", self.modifier))
        elif name == "dex":

            # make ab fpr dex
        return dictionary


class Skill():
    def __init__(self, name, bonus):
        self.name = ""
        self.ability = ability
        self.prof_bonus = [False, False]
