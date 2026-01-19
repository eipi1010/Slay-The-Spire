from game_logic.battle import Battle   
from game_logic.cards.ironclad_cards_module import ironclad_cards
from game_logic.entities.players.player import Player
from game_logic.entities.creatures.monster_pool_module import monster_pool
import copy


def run_simulation(iterations=100):
    win_count = 0
    card_names = ["Strike"]*5 + ["Defend"]*4 + ["Bash"] +["Anger"]

    for i in range(iterations):
    # Pass the class SlimeBoss, not an instance, to the Battle
        deck = [copy.deepcopy(ironclad_cards[name]) for name in card_names]
        player = Player(deck,87)
        enemies = copy.deepcopy(monster_pool[2])
        battle = Battle(player, enemies, verbose=i == 0)
        if battle.run():
            win_count += 1
    
    print(f"Results after {iterations} simulations:")
    print(f"Wins: {win_count} | Losses: {iterations - win_count}")
    print(f"Win Rate: {(win_count/iterations)*100}%")

run_simulation(1)