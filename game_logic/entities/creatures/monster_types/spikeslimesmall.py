import random
from game_logic.entities.creatures.monster import Monster
from game_logic.effects.enemy_effects import EnemyEffects, DamagePlayer

class AcidSlimeSmall(Monster):
    def __init__(self):
        hp = random.randint(10, 14)

        intent = [
            EnemyEffects(effects=[DamagePlayer(5)]),
        ]

        # 3. Pass everything to the parent Monster class
        super().__init__(name="Acid Slime (S)", health=hp, intent=intent)