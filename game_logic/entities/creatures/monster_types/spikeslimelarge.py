import random
from entities.creatures.monster import Monster
from effects.enemy_effects import EnemyEffects, DamagePlayer, GoopSpray, Split, ApplyFrail
from entities.creatures.monster_types.spikeslimemedium import SpikeSlimeMedium

class SpikeSlimeLarge(Monster):
    def __init__(self):
        # 1. Roll HP first so we can use it for the threshold
        hp = random.randint(65, 69)
        split_threshold = hp // 2

        # 2. Define intents using that specific threshold
        intent = [
            EnemyEffects(effects=[Split([DamagePlayer(16), GoopSpray(2)], split_threshold, [SpikeSlimeMedium(), SpikeSlimeMedium()])]),
            EnemyEffects(effects=[Split([ApplyFrail(2)], split_threshold, [SpikeSlimeMedium(), SpikeSlimeMedium()])]),
        ]

        # 3. Pass everything to the parent Monster class
        super().__init__(name="Spike Slime (L)", health=hp, intent=intent)
