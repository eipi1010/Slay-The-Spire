from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from effects.player_effects import CardEffects
    from entities.players.player import Player
    from entities.creatures.monster import Monster


class Card:
    def __init__(self, name:str, mana:int, effects: "CardEffects"):
        self.name = name
        self.mana = mana
        self.effects = effects

    def __repr__(self):
        return self.name
    
    def play(self, card_index:int, player: "Player", enemies: list["Monster"], target_enemy:int) -> None:
        self.effects.apply(card_index, player, enemies, target_enemy)

