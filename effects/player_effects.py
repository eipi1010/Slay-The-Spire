from math import floor

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities.players.player import Player
    from entities.creatures.monster_class import Monster

class CardEffects:
    def __init__(self,effects:list):
        self.effects = effects
    def apply(self, card_index:int, player:"Player",enemies:list["Monster"], enemy_index:int):
        for effect in self.effects:
            effect.apply(card_index, player, enemies, enemy_index)

class DamageEffect:
    def __init__(self,amount:int):
        self.amount = amount
    def apply(self,card_index:int, player:"Player", enemies:list["Monster"], enemy_index:int):
        if player.weak > 0:
            self.amount = floor(self.amount * 0.75)
        enemies[enemy_index].lose_health(self.amount)

class BlockEffect:
    def __init__(self,amount:int):
        self.amount = amount
    def apply(self,card_index:int, player:"Player", enemies:list["Monster"] , enemy_index:int):
        player.block += self.amount

class SelfDiscardEffect:
    def __init__(self):
        pass
    def apply(self, card_index:int, player:"Player", enemies:list["Monster"], enemy_index:int):
        player.discard_pile.append(player.hand[card_index])
        player.hand.pop(card_index)

class SelfExhaustEffect:
    def __init__(self):
        pass
    def apply(self, card_index:int, player:"Player",enemies:list["Monster"], enemy_index:int):
        player.exhaust_pile.append(player.hand[card_index])
        player.hand.pop(card_index)





   # '''
    #class BlockEffect:
    #    def __init__(self,amount:int):
    #        self.amount = amount


   # '''



    
