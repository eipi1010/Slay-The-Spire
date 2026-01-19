import random
from game_logic.entities.creatures.monster import Monster
from game_logic.effects.enemy_effects import DamagePlayer

class AcidSlimeSmall(Monster):
    def __init__(self):
        # 1. Roll HP
        hp = random.randint(10, 14)
        
        # 2. Initialize parent without the fixed intent list
        super().__init__(name="Acid Slime (S)", health=hp)
        
        # 3. Define the single attack
        # Small slimes in the game often only have one move
        self.tackle = DamagePlayer(5)

    def get_current_intent(self):
        """
        Since this slime only has one move, it returns it every turn.
        """
        return self.tackle