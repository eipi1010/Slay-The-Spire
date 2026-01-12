from ironclad import *
from card import *
from enemies import TestDummy

deck = [
    cards["Strike"],
    cards["Strike"],
    cards["Strike"],
    cards["Strike"],
    cards["Strike"],
   # cards["Defend"],
   # cards["Defend"],
   # cards["Defend"],
   # cards["Defend"],
   # cards["Bash"]
   ]

player = Ironclad(deck)
enemies = [TestDummy()]

def start_turn() -> list:
    mana = 3
    player.draw(1)
    return mana

for round in range(3):
    start_turn()
    selected_card = 0
    target_enemy = 0
    player.play(0,enemies,target_enemy)
    print(player)
    print(enemies[0])
    
