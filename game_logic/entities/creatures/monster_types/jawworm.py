from game_logic.entities.creatures.monster import Monster
from game_logic.effects.enemy_effects import EnemyEffects, GainStrength, DamagePlayer, GainBlock
import random

class JawWorm(Monster):
    def __init__(self):
        hp = random.randint(40,44)

        intent = [
            EnemyEffects(effects=[DamagePlayer(11)]),
            EnemyEffects(effects=[GainStrength(3),GainBlock(6)]),
            EnemyEffects(effects=[DamagePlayer(7),GainBlock(5)]),
        ]
        super().__init__("Jaw Worm", health=hp, intent=intent)
