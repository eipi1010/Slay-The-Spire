from math import floor
import copy

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities.players.player import Player
    from entities.creatures.monster import Monster

class CardEffects:
    def __init__(self,effects:list):
        self.effects = effects
    def apply(self, card_index:int, player:"Player",enemies:list["Monster"], enemy_index:int):
        for effect in self.effects:
            effect.apply(card_index, player, enemies, enemy_index)

class DamageEffect:
    def __init__(self,amount:int):
        self.amount = amount
    def apply(self,card_index:int, player:"Player", enemies:list["Monster"], enemy_index:int):
        if player.weak > 0:
            self.amount = floor(self.amount * 0.75)
        enemies[enemy_index].take_damage(amount=self.amount)

class BlockEffect:
    def __init__(self,amount:int):
        self.amount = amount
    def apply(self,card_index:int, player:"Player", enemies:list["Monster"] , enemy_index:int):
        player.block += self.amount

class VulnerableEffect:
    def __init__(self,amount:int):
        self.amount = amount
    def apply(self,card_index:int,player:"Player",enemies:list["Monster"],enemy_index:int):
        if player.frail >= 1:
            self.amount = floor(self.amount*0.75)
        enemies[enemy_index].vulnerable += self.amount

class DuplicateToDiscardPileEffect:
    def __init__(self,amount:int):
        self.amount = amount
    def apply(self,card_index:int,player:"Player",enemies:list["Monster"],enemy_index:int):
        for _ in range(self.amount):
            duplicate_card = copy.deepcopy(player.hand[card_index])
            player.discard_pile.append(duplicate_card)

class UpgradeRandomCardInHandEffect:
    def __init__(self,amount:int):
        self.amount = amount
    def apply(self,card_index:int,player:"Player",enemies:list["Monster"],enemy_index:int):
        for _ in range(self.amount):
            
        
class SelfDiscardEffect:
    def __init__(self):
        pass
    def apply(self, card_index:int, player:"Player", enemies:list["Monster"], enemy_index:int):
        player.discard_pile.append(player.hand[card_index])
        player.hand.pop(card_index)

class SelfExhaustEffect:
    def __init__(self):
        pass
    def apply(self, card_index:int, player:"Player",enemies:list["Monster"], enemy_index:int):
        player.exhaust_pile.append(player.hand[card_index])
        player.hand.pop(card_index)



    
