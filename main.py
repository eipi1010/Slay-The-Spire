from visualisation.assets import load_all_assets
from visualisation.renderer import GameRenderer
from game_logic.utils.simulation import build_deck,run_simulation
from game_logic.entities.players.player import Player
import copy
from game_logic.entities.creatures.monster_pool_module import monster_pool
import time
import pygame
import sys

STARTING_CARD_NAMES = ["Strike"] * 5 + ["Bash"] + ["Defend"] *4


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
    current_deck = build_deck(STARTING_CARD_NAMES) 
    player = Player(current_deck,health=80)
    enemies = copy.deepcopy(monster_pool[1])

    print("Step 5: Entering Game Loop...")
    is_active = True

    while is_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Deepcopy enemies so their HP/Intent resets every time
        player.start_turn()
        renderer.draw_state(player, enemies)
        time.sleep(2)
        can_play =True
        while can_play:
            can_play = player.play_one_turn_randomly(enemies)
            enemies = [e for e in enemies if e.health > 0]
            renderer.draw_state(player,enemies)
            time.sleep(1)

        player.end_turn()
        renderer.draw_state(player, enemies)
        time.sleep(2)

        for i in range(len(enemies)):
            enemies[i].play_turn(player,enemies,i)
            renderer.draw_state(player, enemies)
            time.sleep(2)
        
        for enemy in enemies:
            enemy.end_turn()
            renderer.draw_state(player,enemies)
            time.sleep(2)

        if player.health <= 0 or len(enemies) == 0:
            renderer.draw_state(player,enemies)
            is_active = False
            time.sleep(5)
        

        # Player Starts turn


if __name__ == "__main__":
    run_simulation(1000)    
    main()