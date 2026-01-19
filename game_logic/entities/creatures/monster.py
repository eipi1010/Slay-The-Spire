from math import floor
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from effects.enemy_effects import EnemyEffects
    from entities.players.player import Player

class Monster:
    def __init__(self, name: str, health: int, intent: list["EnemyEffects"] = None):
        self.name = name
        self.health = health
        self.max_health = health
        self.intent = intent if intent else []
        self.turn_count = 0

        self.block = 0
        self.strength = 0
        self.weak = 0
        self.vulnerable = 0

    def __repr__(self):
        return self.name

    def get_current_intent(self):
        """
        Decides the move for the turn. 
        Subclasses like SlimeBoss will override this to check for 'Split'.
        """
        if not self.intent:
            return None
        return self.intent[self.turn_count % len(self.intent)]

    def __str__(self):
        current = self.get_current_intent()
        return (
            f"--- {self.name} ---\n"
            f"Health: {self.health}/{self.max_health}\n"
            f"Intent: {current}\n"
            f"Block: {self.block}\n"
            f"Strength: {self.strength}\n"
            f"Weak: {self.weak}\n"
            f"Vulnerable: {self.vulnerable}\n"
        )
    
    def take_damage(self, amount: int):
        if self.vulnerable >= 1:
            amount = floor(amount * 1.5)

        if self.block >= amount:
            self.block -= amount
        else:
            health_lost = amount - self.block
            self.block = 0 # Block is fully consumed
            self.health = max(self.health - health_lost, 0) 
            
    def play_turn(self, player: "Player", enemies: list["Monster"], my_index: int):
        action = self.get_current_intent()
        if action:
            # We pass my_index so the effect knows which monster is acting
            action.apply(player, enemies, my_index)
        
        # We don't call end_turn here, usually Battle calls it after everyone acts
        # but you can keep it here if your loop logic prefers it.

    def end_turn(self):
        self.block = 0
        self.weak = max(0, self.weak - 1)
        self.vulnerable = max(0, self.vulnerable - 1)
        self.turn_count += 1

    
    
    