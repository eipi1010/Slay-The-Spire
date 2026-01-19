from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities.creatures.monster import Monster
    from entities.players.player import Player

from cards.status_cards_module import status_cards

class EnemyEffects:
    def __init__(self,effects:list):
        self.effects = effects
    def apply(self, player:"Player",enemies:list["Monster"],target_enemy:int):
        for effect in self.effects:
            effect.apply(player,enemies,target_enemy)
    def __str__(self):
        # Convert all effects to strings and join them
        return ", ".join([str(e) for e in self.effects])


class Charging:
    def __init__(self):
        pass
    def apply(self,player:"Player",enemies:list["Monster"],target_enemy:int):
        pass
    def __str__(self):
        return("Charging")


class DamagePlayer:
    def __init__(self,amount:int):
        self.amount = amount
    def apply(self,player:"Player",enemies:list["Monster"],target_enemy:int):
        strength_boost = enemies[target_enemy].strength
        player.take_damage(self.amount + strength_boost)
    def __str__(self):
        return(f"Dealing {self.amount} damage")
    
class GainStrength:
    def __init__(self,amount:int):
        self.amount = amount
    def apply(self,player:"Player",enemies:list["Monster"],target_enemy:int):
        enemies[target_enemy].strength += self.amount
    def __str__(self):
        return(f"Gaining {self.amount} strength")

class WeakenPlayer:
    def __init__(self,amount:int):
        self.amount = amount
    def apply(self,player:"Player",enemies:list["Monster"],target_enemy:int):
        player.weak += self.amount
    def __str__(self):
        return(f"Applying {self.amount} weak")
    
class FrailPlayer:
    def __init__(self,amount:int):
        self.amount=amount
    def apply(self,player:"Player",enemies:list["Monster"],target_enemy:int):
        player.frail += self.amount
    def __str__(self):
        return(f"Applying {self.amount} frail")

class GoopSpray:
    def __init__(self,amount:int):
        self.amount = amount
    def apply(self,player:"Player",enemies:list["Monster"],target_enemy:int):
        for i in range(self.amount):
            player.discard_pile.append(status_cards["Slimed"])
    def __str__(self):
        return(f"Adding {self.amount} slimed card(s) to discard pile")
    
class GainBlock:
    def __init__(self,amount:int):
        self.amount = amount
    def apply(self,player:"Player",enemies:list["Monster"],target_enemy:int):
        enemies[target_enemy].block += self.amount
    def __str__(self):
        return(f"Applying {self.amount} block to self")

class Split:
    def __init__(self, effects:list,amount:int,monsterspawn:list["Monster"]):
        self.effects = effects
        self.amount = amount
        self.monsterspawn = monsterspawn
    def apply(self,player:"Player",enemies:list["Monster"],target_enemy:int):
        if enemies[target_enemy].health <= self.amount:
            for enemy in enemies:
                enemy.health = enemies[target_enemy].health // 2
            enemies.pop(target_enemy)
            for enemy in self.monsterspawn:
                enemies.append(enemy)
        else:
            for effect in self.effects:
                effect.apply(player,enemies,target_enemy)
        
    def __str__(self):
        return ", ".join([str(e) for e in self.effects])


