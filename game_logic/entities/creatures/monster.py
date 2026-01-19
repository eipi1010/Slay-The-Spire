from math import floor

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from effects.enemy_effects import EnemyEffects
    from entities.players.player import Player


class Monster:
    #intent is an n x 1 array where each element is a list of enemy effects
    def __init__(self,name:str,health:int,intent:list["EnemyEffects"]):
        self.health = health
        self.name = name
        self.intent = intent
        self.turn_count = 0

        self.block = 0
        self.strength = 0


        self.weak = 0
        self.vulnerable = 0
        
    def __repr__(self):
        return self.name

    def __str__(self):
        return (
            f"--- {self.name} ---\n"
            f"Health: {self.health}\n"
            f"Intent: {self.intent[self.turn_count % len(self.intent)]}\n"
            f"Block: {self.block}\n"
            f"Strength: {self.strength}\n"
            f"Weak: {self.weak}\n"
            f"Vulnerable: {self.vulnerable}\n"
        )
    
    def take_damage(self, amount:int):
        if self.vulnerable >= 1:
            amount = floor(amount*1.5)

        if self.block >= amount:
            self.block - amount
        else:
            health_lost = amount - self.block
            self.health = max(self.health - health_lost,0) 
            
    def play_turn(self,player:"Player",enemies:list["Monster"],target_enemy:int):
        self.intent[self.turn_count % len(self.intent)].apply(player,enemies,target_enemy)

    def end_turn(self):
        self.block = 0
        self.weak = max(0,self.weak-1)
        self.vulnerable = max(0,self.vulnerable-1)
        self.turn_count += 1

    
    
    