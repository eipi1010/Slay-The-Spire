from game_logic.battle import Battle   
# Import your new card classes here
from game_logic.cards.ironclad_cards_module import Strike,Bash
from game_logic.entities.players.player import Player
from game_logic.entities.creatures.monster_pool_module import monster_pool
import copy

def run_simulation(iterations=100):
    win_count = 0
    
    # Map names to their actual Classes
    card_map = {
        "Strike": Strike,
        "Bash": Bash,
    }
    
    # The list of strings we want in our deck
    card_names = ["Strike"]*5+ ["Bash"]

    for i in range(iterations):
        # Create a new instance of each card class for every simulation
        # This is cleaner than deepcopying dictionaries!
        deck = [card_map[name]() for name in card_names]
        
        player = Player(deck, 87)
        
        # Ensure monster_pool returns a list of monster instances
        enemies = copy.deepcopy(monster_pool[2])
        
        battle = Battle(player, enemies, verbose=(i == 0))
        
        if battle.run():
            win_count += 1
    
    print(f"Results after {iterations} simulations:")
    print(f"Wins: {win_count} | Losses: {iterations - win_count}")
    if iterations > 0:
        print(f"Win Rate: {(win_count/iterations)*100}%")

if __name__ == "__main__":
    run_simulation(1000)