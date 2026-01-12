from ironclad import *
from card import *
from enemies import Monstor
from enemy_effects import *

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

def start_turn() -> list:
    mana = 3
    player.draw(1)
    return mana

def turn():
    player.mana = 3
    player.draw(5)
    for i in range(len(player.hand)):
        if player.play(card_index=0,enemies=enemies,enemy_index=0):
            i = 0
    for i in range(len(enemies)):
        if enemies[i].health <= 0:
            enemies.pop(i)   
    for enemy in enemies:
        enemy.attack(player)
    player.discard_all

win_count = 0
loss_count = 0

for i in range(5):
    battle = True
    player = Ironclad(deck)
    test_dummy = Monstor(health=50, effects=EnemyEffects(effects=[DamagePlayer(amount=5)]))
    enemies = [test_dummy]
    while battle:
        turn()
        print(player)
        if len(enemies) == 0 or player.health <= 0:
            battle = False
    if len(enemies) == 0:
        win_count += 1
    else:
        loss_count += 1       

print(win_count)
    

    
