from cards.cards_class import *
from effects.player_effects import *

class Player():
    def __init__(self, deck: list, health:int = 87, mana:int = 3, block:int = 0, hand: list =[],discard_pile: list = [],exhaust_pile = []):
        self.deck = deck
        self.health = health
        self.mana=mana
        self.block=block
        self.hand = hand
        self.discard_pile = discard_pile
        self.exhaust_pile = exhaust_pile
    
    def __str__(self):
        return(
            "---Ironclad Stats---\n"
            f"Health: {self.health}:\n"
            f"Draw Pile: {[card for card in self.deck]}\n"
            f"Hand: {[card for card in self.hand]}\n"
            f"Discard Pile: {[card for card in self.discard_pile]}\n"
        )
    
    def lose_health(self,amount:int):
        self.health -= amount

    def draw(self, card_draw:int) -> None:
        if len(self.deck) != 0:
            random.shuffle(self.deck)
        for i in range(card_draw):
            if len(self.deck) == 0 and len(self.discard_pile) == 0:
                return
            elif len(self.deck) == 0:
                self.deck = self.discard_pile.copy()
                self.discard_pile.clear()
                random.shuffle(self.deck)
            self.hand.append(self.deck[0])
            self.deck.pop(0)

    def discard_all(self):
        self.discard_pile.extend(self.hand)
        self.hand.clear
        
    def play(self, card_index:int, enemies, enemy_index:int = 0) -> bool:
        if self.hand[card_index].mana > self.mana:
            return False
        self.mana -= self.hand[card_index].mana
        return True
    





