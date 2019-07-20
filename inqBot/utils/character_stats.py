

class Ability(object):
    """A simple Ability class which calculates the modifier and actual score as well as supplies appropriate skills
    for stats"""

    def __init__(self,name, score=10):
        self.score = score
        self.modifier = int((self.score-10)/2)
        if name == "Dex":
            self.name = "Dex"
            self.skills = {"Acrobatics":Skill("Acrobatics"),"Sleight of Hand":Skill("Sleight of Hand")
            "Stealth":Skill("Stealth")}
        elif name == "Str":
            self.name == "Str"
            self.skills = {"Athletics":Skill("Atheltics")}
        elif name == "Con":
            self.name == "Con"
        elif name == "Wis":
            self.name == "Wis"
            self.skills = {"Animal Handling":Skill("Animal Handling"),"Insight":Skill("Insight"),
            "Medicine":Skill("Medicine"),"Perception":Skill("Perception"),"Survival":Skill("Survival")}
        elif name == "Int":
            self.name == "Int"
            self.skills = {"Arcana":Skill("Arcana"),"History":Skill("History"),"Investigation":Skill("Investigation"),"Nature":Skill("Nature"),
            "Religion":Skill("Religion")}
        elif name == "Cha":
            self.name == "Cha"
            self.skills = {"Deception":Skill("Deception"),"Intimidation":Skill("Intimidation"),"Performance":Skill("Performance"),
            "Persuasion":Skill("Persuasion")}


    def __set__(self, score):
        self.score = score
        self.modifier = int((self.score-10)/2)

    def __str__(self):
        return_string = str(self.score) + "({:+})".format(self.modifier)
        return return_string


class Skill(object):
    """
