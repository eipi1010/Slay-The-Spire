import copy
import random
from game_logic.utils.battle import Battle
from game_logic.entities.players.player import Player
from game_logic.entities.creatures.monster_pool_module import monster_pool
from tqdm import tqdm
from game_logic.utils.build_deck import build_deck

# 1. Define the deck structure as strings
# This makes it easy to modify the starting deck for different tests
STARTING_CARD_NAMES = ["Strike"] * 4 + ["Strike+"] * 1 + ["Armaments+"] * 1 + ["Bash"]



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

