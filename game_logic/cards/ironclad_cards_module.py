from game_logic.cards.cards import Card

# --- Specific Card Implementations ---
class Strike(Card):
    def __init__(self):
        super().__init__("Strike", 1, "Attack",exhaust=False)
        self.damage = 6

    def _on_upgrade(self):
        self.damage = 9

    def play(self,player, enemies, target_index):
        # The card knows exactly what to do with the target
        enemies[target_index].take_damage(self.damage)

class Bash(Card):
    def __init__(self):
        super().__init__("Bash", 2,"Attack",exhaust=False)
        self.damage = 8
        self.vulnerable = 2

    def _on_upgrade(self):
        self.damage = 10
        self.vulnerable = 3

    def play(self, player, enemies, target_index):
        enemies[target_index].take_damage(self.damage)
        enemies[target_index].vulnerable += self.vulnerable

