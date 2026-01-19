import random
from game_logic.entities.creatures.monster import Monster
from game_logic.effects.enemy_effects import EnemyEffects, DamagePlayer, GoopSpray, WeakenPlayer

class AcidSlimeMedium(Monster):
    def __init__(self):
        # We define the intent inside __init__ so each slime gets its own copy
        intent = [
            EnemyEffects([DamagePlayer(7), GoopSpray(1)]),
            EnemyEffects([WeakenPlayer(1)]),
            EnemyEffects([DamagePlayer(10)])
        ]
        
        # Calculate health here so each instance gets a different random roll
        hp = random.randint(28, 32)
        
        # super() sends the name, health, and intent up to the Monster class
        super().__init__(name="Acid Slime (M)", health=hp, intent=intent)