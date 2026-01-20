from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities.players.player import Player
    from entities.creatures.monster import Monster

import copy
from game_logic.utils.battle import Battle

class FightAll:
    def __init__(self,monster_pool:list["Monster"]):
        self.monster_pool = monster_pool

    def execute(self,player:"Player",iterations_per_fight:int):
        for i in range(len(self.monster_pool)):
            win_count = 0
            health_remaining = 0
            for _ in range(iterations_per_fight):
                temp_player = copy.deepcopy(player)
                temp_enemies = copy.deepcopy(self.monster_pool[i])
                battle = Battle(temp_player, temp_enemies)
                if battle.run():
                    win_count += 1
                health_remaining += temp_player.health

            print(f"Win Rate against {self.monster_pool[i]}: {win_count/iterations_per_fight}",
                  f"{health_remaining/iterations_per_fight}")

    