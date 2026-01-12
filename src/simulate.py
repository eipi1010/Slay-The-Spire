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

def print_stats(turn_count):
    print(f"--------------Turn Count: {turn_count}--------------\n")
    print(player)
    for enemy in enemies:
        print(enemy)


win_count = 0
loss_count = 0

for i in range(10):
    battle = True
    turn_count = 1
    player = Ironclad(deck)
    test_dummy = Monstor(health=50, effects=EnemyEffects(effects=[DamagePlayer(amount=5)]))
    enemies = [test_dummy]
    while battle:
        print_stats(turn_count)
        turn()
        turn_count += 1
        if len(enemies) == 0 or player.health <= 0:
            battle = False
    if len(enemies) == 0:
        win_count += 1
    else:
        loss_count += 1 

    print_stats(turn_count)  

print(f"win_count: {win_count}\n"
      f"loss count: {loss_count}")
    

    
