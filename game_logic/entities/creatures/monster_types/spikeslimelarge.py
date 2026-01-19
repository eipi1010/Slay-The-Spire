import random
from game_logic.entities.creatures.monster import Monster
from game_logic.effects.enemy_effects import DamagePlayer, FrailPlayer, Split
from game_logic.entities.creatures.monster_types.spikeslimemedium import SpikeSlimeMedium

class SpikeSlimeLarge(Monster):
    def __init__(self):
        # 1. Roll HP and set threshold
        hp = random.randint(65, 69)
        super().__init__(name="Spike Slime (L)", health=hp)
        self.split_threshold = hp // 2
        
        # 2. Define standard attack pool
        # Spike Slimes (L) alternate between licking (Frail) and slamming
        self.attack_pool = [
            FrailPlayer(2),
            DamagePlayer(16)
        ]

    def get_current_intent(self):
        """Priority: Split check, then cycle through attacks"""
        
        # 1. Check for Split
        if self.health <= self.split_threshold:
            # We only create these Medium Slimes when the split actually occurs
            return Split(spawn=[SpikeSlimeMedium(), SpikeSlimeMedium()])

        # 2. Otherwise, cycle through the attack pattern
        return self.attack_pool[self.turn_count % len(self.attack_pool)]