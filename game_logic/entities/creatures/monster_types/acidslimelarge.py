import random
from game_logic.entities.creatures.monster import Monster
from game_logic.effects.enemy_effects import WeakenPlayer, DamagePlayer, GoopSpray, Split
from game_logic.entities.creatures.monster_types.acidslimemedium import AcidSlimeMedium

class AcidSlimeLarge(Monster):
    def __init__(self):
        # 1. Roll HP and set the split threshold
        hp = random.randint(65, 69)
        super().__init__(name="Acid Slime (L)", health=hp)
        self.split_threshold = hp // 2
        
        # 2. Define the regular attack pool (without Split logic)
        self.attack_pool = [
            # In Slay the Spire, Large Slimes usually have a pattern or random choice
            DamagePlayer(11),
            GoopSpray(2),
            WeakenPlayer(2),
            DamagePlayer(16)
        ]

    def get_current_intent(self):
        """Dynamic check: Split takes priority over everything else"""
        
        # 1. Check health for Split
        if self.health <= self.split_threshold:
            # We return a Split effect that spawns two Medium Slimes
            return Split(spawn=[AcidSlimeMedium(), AcidSlimeMedium()])

        # 2. Otherwise, pick an attack based on the turn count or randomness
        # For simplicity, we cycle through the pool
        return self.attack_pool[self.turn_count % len(self.attack_pool)]