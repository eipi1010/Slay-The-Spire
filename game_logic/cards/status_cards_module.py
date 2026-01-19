from game_logic.cards.cards import Card

class Slimed(Card):
    def __init__(self):
        super().__init__("Slimed",1,"Status",True)

    def _on_upgrade(self):
        pass

    def play(self,player, enemies, target_index):
        pass


