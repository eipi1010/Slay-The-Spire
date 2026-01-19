import pygame
import os

def load_all_assets():
    # Create a master dictionary to return
    all_assets = {}
    
    # Load Cards
    card_path = "assets/images/cards"
    if os.path.exists(card_path):
        for f in os.listdir(card_path):
            if f.endswith(".png"):
                name = os.path.splitext(f)[0]
                all_assets[name] = pygame.image.load(os.path.join(card_path, f)).convert_alpha()

    # Load Creatures
    creature_path = "assets/images/creatures"
    if os.path.exists(creature_path):
        for f in os.listdir(creature_path):
            if f.endswith(".png"):
                name = os.path.splitext(f)[0]
                all_assets[name] = pygame.image.load(os.path.join(creature_path, f)).convert_alpha()
    
    return all_assets # This sends the data back to main.py