from visualisation.assets import load_all_assets
from visualisation.renderer import GameRenderer
from game_logic.cards.ironclad_cards_module import ironclad_cards
from game_logic.entities.players.player import Player
import copy
from game_logic.entities.creatures.monster_pool_module import monster_pool
import pygame
import sys

card_names = ["Strike"]*5 + ["Defend"]*4 + ["Bash"]
deck = [copy.deepcopy(ironclad_cards[name]) for name in card_names]
player = Player(deck,87)
enemies = copy.deepcopy(monster_pool[1])

def main():
    print("Step 1: Initializing Pygame...")
    pygame.init()
    
    print("Step 2: Setting up Screen...")
    screen = pygame.display.set_mode((1280, 720))
    
    print("Step 3: Loading Assets...")
    assets = load_all_assets()
    print(f"Loaded {len(assets)} assets.")

    print("Step 4: Initializing Renderer...")
    renderer = GameRenderer(screen, assets)

    print("Step 5: Entering Game Loop...")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        renderer.draw_state(player, enemies)

if __name__ == "__main__":
    main()
