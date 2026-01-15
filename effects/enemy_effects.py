from entities.players.player import *

class EnemyEffects:
    def __init__(self,effects:list):
        self.effects = effects
    def apply(self, player,enemy):
        for effect in self.effects:
            effect.apply(player,enemy)

class DamagePlayer:
    def __init__(self,amount:int):
        self.amount = amount
    def apply(self,player,enemy):
        player.lose_health(self.amount)

