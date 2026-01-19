from game_logic.entities.creatures.monster import Monster
from game_logic.effects.enemy_effects import EnemyEffects, GainStrength, DamagePlayer
import random

class Cultist(Monster):
    def __init__(self):
        hp = random.randint(48,54)

        intent = [
            EnemyEffects(effects=[GainStrength(3)]),
            EnemyEffects(effects=[DamagePlayer(6)]),
        ]
        super().__init__("Cultist", health=hp, intent=intent)
