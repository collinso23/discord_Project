import random

class SuperDice(object):

    def make_roll(self,dice,modifer): #,num_dice
        """
        params: dice (ie,d6,d8,d10...)
                modifer (ie [INT +2], saving throws, prof bonus...)
                number of dice (1,2,3...)

        """
        try:
            rolls,max_roll = map(int,dice.split('d'))
        except Exception:
            error ="format has to be NdN"
            return error

        result = []
        for num in range(rolls):
            r = random.randint(1,max_roll) + int(modifer)
            result.append(r)
        total = sum(result)
        
        return_str="dice: {} results {}={} Mod: +{} per roll".format(dice,result,total,modifer)
        return return_str
