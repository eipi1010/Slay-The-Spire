from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities.creatures.monster import Monster
    from entities.players.player import Player


class Battle:
    def __init__(self, player:"Player", enemies:list["Monster"], verbose:bool=False):
        self.player = player
        self.enemies = enemies
        self.turn_count = 1
        self.is_active = True
        self.verbose = verbose

    def run(self):
        while self.is_active:
            if self.verbose:
                print(self)

            self.play_turn()
            self.check_game_over()
            self.turn_count += 1


        return len(self.enemies) == 0

    
    def play_turn(self):
        self.player.start_turn()

        self.player.play_randomly(self.enemies)
        self.enemies = [e for e in self.enemies if e.health > 0]
        self.player.end_turn()

        for i in range(len(self.enemies)):
            self.enemies[i].play_turn(self.player,self.enemies,i)
        
        for enemy in self.enemies:
            enemy.end_turn()

    def check_game_over(self):
        if self.player.health <= 0 or len(self.enemies) == 0:
            self.is_active = False

    def __str__(self):
        enemy_stats = "\n".join([str(e) for e in self.enemies])
        return (f"--- Turn {self.turn_count} ---\n"
                f"{self.player}\n"
                f"{enemy_stats}\n")
    
