import random
from game_logic.entities.creatures.monster import Monster
from game_logic.effects.enemy_effects import EnemyEffects, DamagePlayer, GoopSpray, WeakenPlayer

class AcidSlimeMedium(Monster):
    def __init__(self):
        hp = random.randint(28, 32)
        super().__init__(name="Acid Slime (M)", health=hp)
        
        # We group the first turn's effects into one EnemyEffects object
        self.attack_pool = [
            EnemyEffects([DamagePlayer(7), GoopSpray(1)]), # Turn 0: Both happen
            WeakenPlayer(1),                               # Turn 1
            DamagePlayer(10)                               # Turn 2
        ]

    def get_current_intent(self):
        return self.attack_pool[self.turn_count % len(self.attack_pool)]