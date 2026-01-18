import random
from entities.creatures.monster_class import Monster
from effects.enemy_effects import EnemyEffects, WeakenPlayer, DamagePlayer, GoopSpray

intent = [
    EnemyEffects([DamagePlayer(7),GoopSpray(1)]),
    EnemyEffects([WeakenPlayer(1)]),
    EnemyEffects([DamagePlayer(10)])
          ]

AcidSlimeMedium = Monster(health=random.randint(28,32), intent = intent)