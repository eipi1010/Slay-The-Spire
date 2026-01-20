from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities.players.player import Player
    from entities.creatures.monster import Monster



class Card:
    def __init__(self, name, mana,type,exhaust=False,upgraded=False):
        self.name = name
        self.mana = mana
        self.type = type
        self.exhaust=exhaust 
        self.upgraded = upgraded

    def __repr__(self):
        return self.name

    def upgrade(self):
        if not self.upgraded:
            self.upgraded = True
            self.name += "+"
            # This is where you trigger the stat change
            self._on_upgrade()

    def _on_upgrade(self):
        """Override this in subclasses to change damage/block values"""
        pass

    def play(self, player, enemies, target_index):
        """Standard interface for all cards"""
        pass

