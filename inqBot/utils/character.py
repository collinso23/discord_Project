from characters import player_class
from . import dice_class, dnd_scraper

class CreateCharacter(object):
    def create(self):
        """
        will be called by the character cog form discord and will take a variety of user inputs and construct
        a dnd character based upon a few specifications[player name, race, class, desired level], and save
        that character in an accessible form that will be able to be retreived by owners and the creator of the
        original file. The user should later be able to access that file with additional commands and edit the data stored.
        """
        return

    def edit_file(self):
        """called when a player would like to edit information stored in their character sheet"""
        return

    def save(self):
    """ will save character information and creator to file<?pdf,xml,json,txt?>"""
        return
    pass


class Character(object):
        pass
