from classes import *

#IRONCLAD
cards = {
    "Strike": Card(name="Strike",damage=6,block=0,mana=1),
    "Defend": Card(name="Defend",damage=0,block=5,mana=1),
    "Bash": Card(name="Bash",damage=6,block=0,mana=2),
    "Shrug It Off": Card(name="Shrug It Off",damage=0,block=8,mana=1,draw=1),
    "Twin Strike": Card(name="Twin Strike",damage=10,block=0,mana=1),
    "Sword Boomerang": Card(name="Sword Boomerang",damage=9,block=0,mana=1),
   # "strike": Card(damage=6,block=0,mana=1),
   # "strike": Card(damage=6,block=0,mana=1)
}

class ironclad():
    def __init__(self, deck:Deck, health:int = 87):
        self.deck = deck
        self.health = health
    
    def play(self):
        self.dec
    