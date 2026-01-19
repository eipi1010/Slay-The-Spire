import random
from entities.creatures.monster import Monster
from effects.enemy_effects import WeakenPlayer, DamagePlayer

class AcidSlimeSmall(Monster):
    def __init__(self):
        # 1. Roll HP
        hp = random.randint(8, 12)
        
        # 2. Initialize parent without the fixed intent list
        super().__init__(name="Acid Slime (S)", health=hp)
        
        # 3. Define the attack pool
        self.attack_pool = [
            WeakenPlayer(1),
            DamagePlayer(3)
        ]

    def get_current_intent(self):
        """
        Small slimes usually cycle through their limited moves.
        """
        return self.attack_pool[self.turn_count % len(self.attack_pool)]