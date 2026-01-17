from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities.creatures.monster_class import Monster
    from entities.players.player import Player

from cards.status_cards_module import status_cards

class EnemyEffects:
    def __init__(self,effects:list):
        self.effects = effects
    def apply(self, player:"Player",enemies:list["Monster"],target_enemy:int):
        for effect in self.effects:
            effect.apply(player,enemies,target_enemy)

class Charging:
    def __init__(self):
        pass
    def apply(self,player:"Player",enemies:list["Monster"],target_enemy:int):
        pass

class DamagePlayer:
    def __init__(self,amount:int):
        self.amount = amount
    def apply(self,player:"Player",enemies:list["Monster"],target_enemy:int):
        player.take_damage(self.amount)

class WeakenPlayer:
    def __init__(self,amount:int):
        self.amount = amount
    def apply(self,player:"Player",enemies:list["Monster"],target_enemy:int):
        player.weak += self.amount

class GoopSpray:
    def __init__(self,amount:int):
        self.amount = amount
    def apply(self,player:"Player",enemies:list["Monster"],target_enemy:int):
        for i in range(self.amount):
            player.discard_pile.append(status_cards["Slimed"])
    
class ApplyBlock:
    def __init__(self,amount:int):
        self.amount = amount
    def apply(self,player:"Player",enemies:list["Monster"],target_enemy:int):
        enemies[target_enemy].block += self.amount

