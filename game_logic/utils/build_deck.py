from game_logic.cards.card_map import card_map


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
