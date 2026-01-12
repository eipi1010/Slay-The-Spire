from card import *
from enemies import *

class CardEffects:
    def __init__(self,effects:list):
        self.effects = effects
    def apply(self, player,enemy):
        for effect in self.effects:
            effect.apply(player,enemy)

class DamageEffect:
    def __init__(self,amount:int):
        self.amount = amount
    def apply(self,enemies:list, target_enemy:int):
        enemies[target_enemy].lose_health(self.amount)




   # '''
    #class BlockEffect:
    #    def __init__(self,amount:int):
    #        self.amount = amount


   # '''



    
