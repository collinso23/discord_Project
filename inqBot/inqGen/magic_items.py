class MagicItem():
    """
    Generic Magic Item. Add description here.
    """
    name = ''
    ac_bonus = 0
    requires_attunement = False
    needs_implementation = False
    rarity = ''

    def __init__(self, owner=None):
        self.owner = owner

    def __str__(self):
        return self.name

    def __repr__(self):
        return '\"{:s}\"'.format(str(self))

class RingOfProtection(MagicItem):
    """
    You gain a +1 bonus to AC and Saving Throws while wearing this ring.
    """
    name = "Ring of Protection"
    ac_bonus = 1
    requires_attunement = True
    rarity = 'Rare'
