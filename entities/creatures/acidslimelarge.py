from entities.creatures.monster_class import Monster
from effects.enemy_effects import EnemyEffects, WeakenPlayer, DamagePlayer, GoopSpray

intent = [
    EnemyEffects([DamagePlayer(11),GoopSpray(2)]),
    EnemyEffects([WeakenPlayer(2)]),
    EnemyEffects([DamagePlayer(16)])
          ]
