from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities.players.player import Player
    from entities.creatures.monster import Monster

class ActOneSimulator:
    def __init__(self,path:list[str],easy_monster_pool:list["Monster"], monster_pool:list["Monster"],elite_pool:list["Monster"],boss_pool=list["Monster"]):
        self.path = path
        self.easy_monster_pool = easy_monster_pool
        self.monster_pool = monster_pool
        self.elite_pool = elite_pool
        self.boss_pool = boss_pool

    

