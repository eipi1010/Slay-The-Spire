import random
from game_logic.entities.creatures.monster import Monster
from game_logic.effects.enemy_effects import EnemyEffects, GainStrength, DamagePlayer, GainBlock

class JawWorm(Monster):
    def __init__(self):
        hp = random.randint(40, 44)
        super().__init__("Jaw Worm", health=hp)
        
        # Define the three distinct actions
        self.chomp = DamagePlayer(11)
        self.bellow = EnemyEffects([GainStrength(3), GainBlock(6)])
        self.thrash = EnemyEffects([DamagePlayer(7), GainBlock(5)])
        
        # Track history to prevent move spamming (optional but accurate)
        self.last_move = None

    def get_current_intent(self):
        """
        Jaw Worm AI:
        Turn 0: Always Chomp.
        Other turns: 
        - 25% Chomp (Cannot use twice in a row)
        - 30% Bellow (Cannot use twice in a row)
        - 45% Thrash (Cannot use three times in a row)
        """
        if self.turn_count == 0:
            self.last_move = "chomp"
            return self.chomp

        # Simplified weighted choice for your simulation
        roll = random.randint(1, 100)
        
        if roll <= 25:
            move = self.chomp
        elif roll <= 55:
            move = self.bellow
        else:
            move = self.thrash
            
        return move
