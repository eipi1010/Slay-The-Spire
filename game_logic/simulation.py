
from battle import Battle   
from cards.ironclad_cards_module import ironclad_cards
from entities.players.player import Player
from entities.creatures.monster_types.slimeboss import SlimeBoss
from entities.creatures.monster_types.acidslimesmall import AcidSlimeSmall
import copy

def run_simulation(iterations=100):
    win_count = 0
    card_names = ["Strike"]*5 + ["Defend"]*4 + ["Bash"]

    for i in range(iterations):
    # Pass the class SlimeBoss, not an instance, to the Battle
        deck = [copy.deepcopy(ironclad_cards[name]) for name in card_names]
        player = Player(deck,87)
        enemies = [SlimeBoss()]
        battle = Battle(player, enemies, verbose=i == 9)
        if battle.run():
            win_count += 1
    
    print(f"Results after {iterations} simulations:")
    print(f"Wins: {win_count} | Losses: {iterations - win_count}")
    print(f"Win Rate: {(win_count/iterations)*100}%")

run_simulation(100)
#if __name__ == "__main__":
 #   run_simulation(100)