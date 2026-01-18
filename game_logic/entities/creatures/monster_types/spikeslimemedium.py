import random
from entities.creatures.monster import Monster
from effects.enemy_effects import EnemyEffects, ApplyFrail, DamagePlayer, GoopSpray

class SpikeSlimeMedium(Monster):
    def __init__(self):
        hp = random.randint(28,32)

        intent = [
            EnemyEffects(effects=[DamagePlayer(8), GoopSpray(1)]),
            EnemyEffects(effects=[ApplyFrail(1)]),
        ]

        super().__init__(name="Spike Slime (M)", health=hp, intent=intent)
