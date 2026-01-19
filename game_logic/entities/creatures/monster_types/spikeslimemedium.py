import random
from game_logic.entities.creatures.monster import Monster
from game_logic.effects.enemy_effects import EnemyEffects, FrailPlayer, DamagePlayer, GoopSpray

class SpikeSlimeMedium(Monster):
    def __init__(self):
        # 1. Roll HP
        hp = random.randint(28, 32)
        
        # 2. Initialize parent without the fixed intent list
        super().__init__(name="Spike Slime (M)", health=hp)
        
        # 3. Define the attack pool
        # Turn 0: Slam (Damage + Goop)
        # Turn 1: Lick (Frail)
        self.attack_pool = [
            EnemyEffects([DamagePlayer(8), GoopSpray(1)]),
            FrailPlayer(1)
        ]

    def get_current_intent(self):
        """
        Alternates between its two primary moves.
        """
        return self.attack_pool[self.turn_count % len(self.attack_pool)]
