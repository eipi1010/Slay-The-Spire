from game_logic.cards.ironclad_cards_module import ironclad_cards
from game_logic.entities.players.player import Player
from game_logic.entities.creatures.monster_types.slimeboss import SlimeBoss
from game_logic.battle import Battle
import pygame
import copy

# Initialize Pygame stuff...

def main():
    # Setup the game state once
    card_names = ["Strike"]*5 + ["Defend"]*4 + ["Bash"]
    deck = [copy.deepcopy(ironclad_cards[name]) for name in card_names]
    player = Player(deck, 87)
    enemies = [SlimeBoss()]
    battle = Battle(player, enemies)

    while True: # The Main Pygame Loop
        # 1. Check for clicks
        # 2. Update logic
        if battle.state == "MONSTER_TURN":
            battle.handle_monster_turn()
        
        # 3. Draw everything
        draw_ui(player, enemies)