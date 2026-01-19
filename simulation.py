import copy
import random
from game_logic.battle import Battle
from game_logic.entities.players.player import Player
from game_logic.entities.creatures.monster_pool_module import monster_pool
from game_logic.cards.ironclad_cards_module import card_map
from tqdm import tqdm

# 1. Define the deck structure as strings
# This makes it easy to modify the starting deck for different tests
STARTING_CARD_NAMES = ["Strike"] * 4 + ["Strike+"] * 1 + ["Armaments+"] * 1 + ["Bash"]

def build_deck(names):
    """Converts string names into a fresh list of Card objects."""
    new_deck = []
    for name in names:
        is_upgraded = name.endswith("+")
        base_name = name.rstrip("+")
        
        if base_name in card_map:
            # Create a fresh instance of the card
            card_class = card_map[base_name]
            new_deck.append(card_class(upgraded=is_upgraded))
        else:
            raise KeyError(f"Card name '{base_name}' not found in card_map.")
    return new_deck

def run_simulation(iterations=1000):
    win_count = 0

    print(f"Starting simulation: {iterations} iterations...")

    for i in tqdm(range(iterations), desc="Simulating Battles", unit="battle"):
        # 2. IMPORTANT: Generate a fresh deck and fresh enemies for every run
        # This prevents state leakage between battles
        current_deck = build_deck(STARTING_CARD_NAMES)
        player = Player(current_deck,health=80)
        
        # Deepcopy enemies so their HP/Intent resets every time
        enemies = copy.deepcopy(monster_pool[2])
        
        # Verbose only for the first run to see the logic
        battle = Battle(player, enemies, verbose=(i == 0))
        
        if battle.run():
            win_count += 1
    
    # 3. Final Reporting
    win_rate = (win_count / iterations) * 100
    print("-" * 30)
    print(f"Results after {iterations} simulations:")
    print(f"Wins: {win_count} | Losses: {iterations - win_count}")
    print(f"Win Rate: {win_rate:.2f}%")
    print("-" * 30)

if __name__ == "__main__":
    run_simulation(10000)