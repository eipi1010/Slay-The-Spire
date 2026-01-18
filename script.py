
from cards.ironclad_cards_module import ironclad_cards
from entities.players.player import Player
from entities.creatures.slimeboss import SlimeBoss

'''
from effects.player_effects import CardEffects

from effects.enemy_effects import EnemyEffects, DamagePlayer
'''

deck = [
    ironclad_cards["Strike"],
    ironclad_cards["Strike"],
    ironclad_cards["Strike"],
    ironclad_cards["Strike"],
    ironclad_cards["Strike"],
    ironclad_cards["Defend"],
    ironclad_cards["Defend"],
    ironclad_cards["Defend"],
    ironclad_cards["Defend"],
    #cards["Bash"]
   ]

def start_turn() -> list:
    mana = 3
    player.draw(1)
    return mana

def turn():
    player.start_turn()
    for i in range(len(player.hand)):
        if player.play(card_index=0,enemies=enemies,enemy_index=0):
            i = 0
    for i in range(len(enemies)):
        if enemies[i].health <= 0:
            enemies.pop(i)   
    for i in range(len(enemies)):
        enemies[i].attack(player,enemies,target_enemy=i)

    for i in range(len(enemies)):
        for enemy in enemies:
            print(enemy)
        enemies[i].turn += 1

def print_stats(turn_count):
    print(f"--------------Turn Count: {turn_count}--------------\n")
    print(player)
    for enemy in enemies:
        print(enemy)


win_count = 0
loss_count = 0

for i in range(1):
    battle = True
    turn_count = 1
    player = Player(deck)
    enemies = [SlimeBoss]
    while battle:
        turn()
        print_stats(turn_count)
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
    

    
