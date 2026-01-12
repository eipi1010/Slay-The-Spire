from enemy_effects import *
from ironclad import *

class Monstor:
    def __init__(self,health:int,effects:EnemyEffects):
        self.health = health
        self.effects = effects
    def __str__(self):
        return(
            "---TestDummy Stats---\n"
            f"Health: {self.health}\n"
        )
    def lose_health(self, amount:int):
        self.health -= amount
    def attack(self,player):
        self.effects.apply(player,self)

    
    
    