from card import *
from player_effects import *

#IRONCLAD
cards = {
    "Strike": Card(name="Strike",mana=1,effects = CardEffects(effects=[DamageEffect(amount=5)]))
   # "Defend": Card(name="Defend",damage=0,block=5,mana=1),
   # "Bash": Card(name="Bash",damage=6,block=0,mana=2),
   # "Shrug It Off": Card(name="Shrug It Off",damage=0,block=8,mana=1,draw=1),
   # "Twin Strike": Card(name="Twin Strike",damage=10,block=0,mana=1),
   # "Sword Boomerang": Card(name="Sword Boomerang",damage=9,block=0,mana=1),
   # "strike": Card(damage=6,block=0,mana=1),
   # "strike": Card(damage=6,block=0,mana=1)
}

class Ironclad():
    def __init__(self, deck: list, health:int = 87, mana:int = 3, discard_pile: list = [], hand: list =[]):
        self.deck = deck
        self.health = health
        self.mana=mana
        self.discard_pile = discard_pile
        self.hand = hand
    
    def __str__(self):
        return(
            "---Ironclad Stats---"
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
        self.hand[card_index].play(enemies, enemy_index)
        self.discard_pile.append(self.hand[card_index])
        self.hand.pop(card_index)
        return True
    





