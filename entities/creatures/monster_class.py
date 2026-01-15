from effects.enemy_effects import EnemyEffects
from entities.players.player import Player

class Monster:
    #intent is an n x 1 array where each element is a list of enemy effects
    def __init__(self,health:int,intent:list[EnemyEffects]):
        self.health = health
        self.intent = intent
    def __str__(self):
        return(
            "---TestDummy Stats---\n"
            f"Health: {self.health}\n"
        )
    def lose_health(self, amount:int):
        self.health -= amount

    def attack(self,player:Player):
        self.effects.apply(player,self)

    
    
    