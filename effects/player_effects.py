from cards.cards_class import *
from entities.players.player import *

class CardEffects:
    def __init__(self,effects:list):
        self.effects = effects
    def apply(self, card_index, player,enemies, target_enemy:int):
        for effect in self.effects:
            effect.apply(card_index, player, enemies, target_enemy)

class DamageEffect:
    def __init__(self,amount:int):
        self.amount = amount
    def apply(self,card_index, player, enemies:list, target_enemy:int):
        enemies[target_enemy].lose_health(self.amount)

class BlockEffect:
    def __init__(self,amount:int):
        self.amount = amount
    def apply(self,card_index, player, enemies:list , target_enemy:int):
        player.block += self.amount

class SelfDiscardEffect:
    def __init__(self):
        pass
    def apply(self, card_index, player, enemies:list, target_enemy:int):
        player.discard_pile.append(player.hand[card_index])
        player.hand.pop(card_index)

class SelfExhaustEffect:
    def __init__(self):
        pass
    def apply(self, card_index, player,enemies:list, target_enemy:int):
        self.exhaust_pile.append(player.hand[card_index])
        player.hand.pop(card_index)





   # '''
    #class BlockEffect:
    #    def __init__(self,amount:int):
    #        self.amount = amount


   # '''



    
