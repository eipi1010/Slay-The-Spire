import random
from effects.player_effects import *

class Card:
    def __init__(self, name:str, mana:int, effects: CardEffects):
        self.name = name
        self.mana = mana
        self.effects = effects

    def __repr__(self):
        return self.name
    
    def play(self, card_index:int, player, enemies, target_enemy):
        self.effects.apply(card_index, player, enemies, target_enemy)

