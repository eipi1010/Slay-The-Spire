from cards import *
from classes import *

deck: list = [cards["Strike"],
              cards["Strike"],
              cards["Strike"],
              cards["Strike"],
              cards["Strike"],
              cards["Defend"],
              cards["Defend"],
              cards["Defend"],
              cards["Defend"],
              cards["Bash"]
              ]

deck = Deck(draw_pile = [
    cards["Strike"],
    cards["Strike"],
    cards["Strike"],
    cards["Strike"],
    cards["Strike"],
    cards["Defend"],
    cards["Defend"],
    cards["Defend"],
    cards["Defend"],
    cards["Bash"]
            ])

def start_turn() -> list:
    mana = 3
    deck.draw(5)
    return mana

for turn in range(1):
    start_turn()
    print(deck)
    
