import random
from entities.creatures.monster_class import Monster
from effects.enemy_effects import EnemyEffects, WeakenPlayer, DamagePlayer, GoopSpray, Split
from entities.creatures.acidslimemedium import AcidSlimeMedium

health=random.randint(65,69)
split_threshold = health//2

intent=[
        EnemyEffects(effects=[Split([DamagePlayer(11),GoopSpray(amount=2)],split_threshold,[AcidSlimeMedium,AcidSlimeMedium])]),
        EnemyEffects(effects=[Split([WeakenPlayer(2)],split_threshold,[AcidSlimeMedium,AcidSlimeMedium])]),
        EnemyEffects(effects=[Split([DamagePlayer(amount=16)],split_threshold,[AcidSlimeMedium,AcidSlimeMedium])]),
        ]

AcidSlimeLarge = Monster(health=random.randint(65,69), intent = intent)
