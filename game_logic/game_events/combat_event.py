from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities.players.player import Player
    from entities.creatures.monster import Monster

import copy
from battle import Battle

class CombatEvent():
    def __init__(self,enemies:list["Monster"]):
        self.enemies = enemies

    def execute(self,player_template:"Player",iterations:int):
        win_count = 0
        for i in range(iterations):
            temp_player = copy.deepcopy(player_template)
            temp_enemies = copy.deepcopy(self.enemies)

            battle = Battle(temp_player, temp_enemies, verbose=i==0)
            if battle.run():
                win_count += 1

        return win_count/iterations
    


