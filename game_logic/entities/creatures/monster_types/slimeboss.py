from entities.creatures.monster import Monster
from effects.enemy_effects import EnemyEffects, Charging, DamagePlayer, GoopSpray, Split
from entities.creatures.monster_types.acidslimelarge import AcidSlimeLarge

class SlimeBoss(Monster):
    def __init__(self):
        intent = [
            EnemyEffects(effects=[Split([GoopSpray(amount=3)], 70, [AcidSlimeLarge(), AcidSlimeLarge()])]),
            EnemyEffects(effects=[Split([Charging()], 70, [AcidSlimeLarge(), AcidSlimeLarge()])]),
            EnemyEffects(effects=[Split([DamagePlayer(amount=35)], 70, [AcidSlimeLarge(), AcidSlimeLarge()])]),
        ]
        super().__init__("Slime Boss", health=140, intent=intent)

