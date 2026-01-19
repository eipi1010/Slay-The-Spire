from game_logic.entities.creatures.monster import Monster
from game_logic.effects.enemy_effects import EnemyEffects, Charging, DamagePlayer, GoopSpray, Split
from game_logic.entities.creatures.monster_types.acidslimelarge import AcidSlimeLarge
from game_logic.entities.creatures.monster_types.spikeslimelarge import SpikeSlimeLarge

class SlimeBoss(Monster):
    def __init__(self):
        # We don't pass 'intent' to super anymore
        super().__init__("Slime Boss", health=140)
        self.split_threshold = 70
        self.is_charging = False

    def get_current_intent(self):
        """Logic-driven intent selection"""
        
        # 1. Check for Split
        if self.health <= self.split_threshold:
            # We return the Split effect only when HP is low
            return Split(spawn=[AcidSlimeLarge(), SpikeSlimeLarge()])

        # 2. Boss Cycle Logic
        # Turn 0: Goop Spray
        # Turn 1: Charging
        # Turn 2: Big Slam (35 damage)
        cycle_turn = self.turn_count % 3
        
        if cycle_turn == 0:
            return GoopSpray(amount=3)
        elif cycle_turn == 1:
            self.is_charging = True
            return Charging()
        elif cycle_turn == 2:
            self.is_charging = False
            return DamagePlayer(amount=35)


