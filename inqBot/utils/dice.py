from random import randint
import datetime

class Die(object):
    previous_dice_rolls = {}

    def __init__(self,sides):
        self.sides = sides

    def roll(self,how_many_rolls = 1):
        time_stamp = 'Time: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now())
        if how_many_rolls == 1:
            rolls_values = randint(1,self.sides)
        else:
            rolls_values = []
            for i in range(how_many_rolls):
                rolls_values.append(randint(1,self.sides))

        self.previous_dice_roll.update({time_stamp:rolls_values})
        return rolls_values
