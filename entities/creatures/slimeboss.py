from entities.creatures.monster_class import Monster
from effects.enemy_effects import EnemyEffects, Charging, DamagePlayer, GoopSpray

intent=[
        EnemyEffects(effects=[GoopSpray(amount=3)]),
        EnemyEffects(effects=[Charging()]),
        EnemyEffects(effects=[DamagePlayer(amount=35)]),
        ]

SlimeBoss = Monster(health=140, intent=intent)