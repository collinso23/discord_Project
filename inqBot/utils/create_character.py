#!/usr/bin/env python3

"""
    util for creating a character will be called by cog when
    it is time to implement the cog into the bot
"""
import logging
log = logging.getLogger(__name__)

import math
import numpy as np
import os
from random import randint
import subprocess
import jinja2

import inqGen
from inqGen import (superplayer, race, dice, background, testingFiles, weapons, armor)
from testingFiles import testingClasses

def read_version():
    version = open(os.path.join(os.path.dirname(__file__), '../VERSION')).read()
    version = version.replace('\n','')
    return version

char_classes = {c.name: c for c in testingClasses.available_classes}

races = {r.name: r for r in race.available_races}

backgrounds = {b.name: b for b in background.available_backgrounds}

all_weapons = (weapons.simple_melee_weapons + weapons.martial_melee_weapons +
                weapons.simple_ranged_weapons + weapons.martial_ranged_weapons)

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
