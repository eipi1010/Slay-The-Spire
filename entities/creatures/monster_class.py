from math import floor

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from effects.enemy_effects import EnemyEffects
    from entities.players.player import Player


class Monster:
    #intent is an n x 1 array where each element is a list of enemy effects
    def __init__(
            self,
            health:int,
            intent:list["EnemyEffects"],
            turn:int = 1,
            block:int = 0,
            vulnerable:int = 0,
            ):
        self.health = health
        self.intent = intent
        self.turn = turn
        self.block = block
        self.vulnerable = vulnerable
    def __str__(self):
        return(
            "---TestDummy Stats---\n"
            f"Health: {self.health}\n"
        )
    def take_damage(self, amount:int):
        if self.vulnerable >= 1:
            amount = floor(amount*1.5)

        if self.block >= amount:
            self.block - amount
        else:
            health_lost = amount - self.block
            self.health -= health_lost

    def attack(self,player:"Player",enemies:list["Monster"],target_enemy:int):
        self.intent[self.turn % len(self.intent)].apply(player,enemies,target_enemy)

    
    
    