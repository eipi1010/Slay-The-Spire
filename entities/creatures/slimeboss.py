from entities.creatures.monster_class import Monster
from effects.enemy_effects import EnemyEffects, Charging, DamagePlayer, GoopSpray, Split
from entities.creatures.acidslimelarge import AcidSlimeLarge

intent=[
        EnemyEffects(effects=[Split([GoopSpray(amount=3)],70,[AcidSlimeLarge,AcidSlimeLarge])]),
        EnemyEffects(effects=[Split([Charging()],70,[AcidSlimeLarge,AcidSlimeLarge])]),
        EnemyEffects(effects=[Split([DamagePlayer(amount=35)],70,[AcidSlimeLarge,AcidSlimeLarge])]),
        ]

SlimeBoss = Monster(health=140, intent=intent)

