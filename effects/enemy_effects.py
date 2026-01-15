from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities.creatures.monster_class import Monster
    from entities.players.player import Player

class EnemyEffects:
    def __init__(self,effects:list):
        self.effects = effects
    def apply(self, player,enemy):
        for effect in self.effects:
            effect.apply(player,enemy)

class Charging:
    def __init__(self):
        pass
    def apply(self, player:"Player", enemies:list["Monster"], target_enemy:int):
        pass

class DamagePlayer:
    def __init__(self,amount:int):
        self.amount = amount
    def apply(self,player:"Player",enemies:list["Monster"], target_enemy:int):
        player.lose_health(self.amount)

