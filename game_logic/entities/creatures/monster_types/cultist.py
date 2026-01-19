import random
from game_logic.entities.creatures.monster import Monster
from game_logic.effects.enemy_effects import GainStrength, DamagePlayer

class Cultist(Monster):
    def __init__(self):
        hp = random.randint(48, 54)
        super().__init__("Cultist", health=hp)
        
        # Turn 0: Incantation
        # Turn 1+: Dark Strike
        self.incantation = GainStrength(3)
        self.dark_strike = DamagePlayer(6)

    def get_current_intent(self):
        """
        The Cultist logic: 
        Turn 0: Buff himself.
        All other turns: Attack.
        """
        if self.turn_count == 0:
            return self.incantation
        
        return self.dark_strike