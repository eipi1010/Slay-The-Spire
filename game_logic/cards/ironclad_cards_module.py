from game_logic.cards.cards import Card
import random

# --- Specific Card Implementations ---
class Strike(Card):
    def __init__(self, upgraded=False):
        super().__init__("Strike", 1, "Attack")
        self.damage = 6
        if upgraded:
            self.upgrade()

    def _on_upgrade(self):
        self.damage = 9

    def play(self, player, enemies, target_index):
        enemies[target_index].take_damage(self.damage)

class Defend(Card):
    def __init__(self, upgraded=False):
        super().__init__("Defend", 1, "Skill")
        self.block = 5
        if upgraded:
            self.upgrade()

    def _on_upgrade(self):
        self.block = 8

    def play(self, player, enemies, target_index):
        player.gain_block(self.block)

class Bash(Card):
    def __init__(self, upgraded=False):
        super().__init__("Bash", 2, "Attack")
        self.damage = 8
        self.vulnerable = 2
        if upgraded:
            self.upgrade()

    def _on_upgrade(self):
        self.damage = 10
        self.vulnerable = 3

    def play(self, player, enemies, target_index):
        enemies[target_index].take_damage(self.damage)
        enemies[target_index].vulnerable += self.vulnerable

class Anger(Card):
    def __init__(self, upgraded=False):
        super().__init__("Anger", 0, "Attack")
        self.damage = 6
        if upgraded:
            self.upgrade()

    def _on_upgrade(self):
        self.damage = 8

    def play(self, player, enemies, target_index):
        enemies[target_index].take_damage(self.damage)
        # Anger adds a copy of itself to the discard pile. 
        # If the original was upgraded, the copy should be too!
        player.discard_pile.append(Anger(upgraded=self.upgraded))

class Armaments(Card):
    def __init__(self, upgraded=False):
        super().__init__("Armaments", 1, "Skill")
        self.block = 5
        if upgraded:
            self.upgrade()

    def _on_upgrade(self):
        self.block = 8

    def play(self, player, enemies, target_index):
        player.gain_block(self.block)
        
        # Filter: 1. Not already upgraded, 2. Not a Status/Curse, 3. Is not this specific card
        valid_targets = [
            c for c in player.hand 
            if not c.upgraded 
            and c is not self 
            and c.type not in ["Status", "Curse"]
        ]

        if not valid_targets:
            return

        if self.upgraded:
            for card in valid_targets:
                card.upgrade()
        else:
            random.choice(valid_targets).upgrade()


    


# Map names to their actual Classes
card_map = {
    "Strike": Strike,
    "Bash": Bash,
    "Defend":Defend,
    "Anger":Anger,
    "Armaments":Armaments,

}