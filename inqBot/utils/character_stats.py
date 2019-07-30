

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
    """The Skill class is to be used in conjunction with the Ability class.
    As in, will only be created in conjunction with int,cha,wis,don,str,or con
    """
    def __init__(self, name):
        self.name = name
        self.proficiencies = 0

    def __get__(self):
        return self.proficiencies*2

class Race(object):
    """Here is the base race class. Here is where the
    general information about races, such as speed,size,age,etc
    will be stored"""
    def __init__(self,name = "Human"):
        self.name = name

        self.age_range = ""
        self.age = 30

        self.ability_score_increase = {}
        self.allignment = ""
        self.size = ""
        self.speed = 30
        self.languages = []

        self.has_darkvision = False
        self.darkvision_text = ""
        self.darkvision_length = 60

        self.class_features = {}

class Class(object):

    class Class_Feature(object):
        """Because each feature has a name, description,
        as well as level it is unlocked (can be multiple levels)
        this class was created to contian all the information in one"""
        def __init__(self,name = "blank stare",levels = [1,2],feature_text = "does nothing"):
            self.name = name
            self.levels = []
            self.levels.extend(levels)
            self.feature_text = feature_text
    """The class object. Because most of the information
    used in this bot will be scrapped from the internet
    at time of request, not too much information is needed
    for the class object. However, what should be loaded into
    the class object instantly is information such as
    at what level you get certain features, as well as the
    the names of the class features"""
    def __init__(self, name):
        self.name = name
        self.class_features = []
        self.hit_points = {}
        self.proficiencies = {}
        self.equipment = {}

class Character_Details(object):

    def __init__(self,allignment = "",faith = "", lifestyle = "",
    hair = "blue",skin = "green",eyes = "blue",height = "10 feet"
    weight = "211", age = "20yo",gender = ""):
        self.allignment = allignment
        self.faith = faith
        self.lifestyle = lifestyle
        self.hair = hair
        self.skin = skin
        self.eyes =  eyes
        self.height = height
        self.weight = weight
        self.age = age
        self.gender = gender
