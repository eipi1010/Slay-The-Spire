import random
from entities.creatures.monster import Monster
from effects.enemy_effects import EnemyEffects, WeakenPlayer, DamagePlayer

class AcidSlimeSmall(Monster):
    def __init__(self):
        hp = random.randint(8, 12)

        intent = [
            EnemyEffects(effects=[WeakenPlayer(1)]),
            EnemyEffects(effects=[DamagePlayer(3)]),
        ]

        # 3. Pass everything to the parent Monster class
        super().__init__(name="Acid Slime (S)", health=hp, intent=intent)
