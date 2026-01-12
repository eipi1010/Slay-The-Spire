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
    def __init__(self, draw_pile: list, health:int = 87, discard_pile: list = [], hand: list =[]):
        self.draw_pile = draw_pile
        self.health = health
        self.discard_pile = discard_pile
        self.hand = hand
    
    def __str__(self):
        return(
            "---Ironclad Stats---"
            f"Health: {self.health}:\n"
            f"Draw Pile: {[card for card in self.draw_pile]}\n"
            f"Hand: {[card for card in self.hand]}\n"
            f"Discard Pile: {[card for card in self.discard_pile]}\n"
        )
        
    def draw(self, card_draw:int) -> None:
        if len(self.draw_pile) != 0:
            random.shuffle(self.draw_pile)
        for i in range(card_draw):
            if len(self.draw_pile) == 0 and len(self.discard_pile) == 0:
                return
            elif len(self.draw_pile) == 0:
                self.draw_pile = self.discard_pile
                self.discard_pile.clear()
                random.shuffle(self.draw_pile)
            self.hand.append(self.draw_pile[0])
            self.draw_pile.pop(0)
        
    def play(self, card_index:int, enemy, target_enemy:int = 0) -> None:
        self.hand[card_index].play(enemy, target_enemy)
        self.discard_pile.append(self.hand[card_index])
        self.hand.pop(card_index)




