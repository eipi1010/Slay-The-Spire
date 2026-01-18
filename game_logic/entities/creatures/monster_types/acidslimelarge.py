import random
from entities.creatures.monster import Monster
from effects.enemy_effects import EnemyEffects, WeakenPlayer, DamagePlayer, GoopSpray, Split
from entities.creatures.monster_types.acidslimemedium import AcidSlimeMedium

class AcidSlimeLarge(Monster):
    def __init__(self):
        # 1. Roll HP first so we can use it for the threshold
        hp = random.randint(65, 69)
        split_threshold = hp // 2

        # 2. Define intents using that specific threshold
        intent = [
            EnemyEffects(effects=[Split([DamagePlayer(11), GoopSpray(2)], split_threshold, [AcidSlimeMedium(), AcidSlimeMedium()])]),
            EnemyEffects(effects=[Split([WeakenPlayer(2)], split_threshold, [AcidSlimeMedium(), AcidSlimeMedium()])]),
            EnemyEffects(effects=[Split([DamagePlayer(16)], split_threshold, [AcidSlimeMedium(), AcidSlimeMedium()])]),
        ]

        # 3. Pass everything to the parent Monster class
        super().__init__(name="Acid Slime (L)", health=hp, intent=intent)
