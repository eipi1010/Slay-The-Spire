from enemy_effects import *

class TestDummy:
    def __init__(self,health:int = 87,effects:list = []):
        self.health = health
        self.effects = effects
    def __str__(self):
        return(
            "---TestDummy Stats---\n"
            f"Health: {self.health}\n"
        )
    def lose_health(self, amount:int):
        self.health -= amount
   # def apply(self):
   #     for effect in self.effects:
    #        effect.apply(self,player)
    
    
    