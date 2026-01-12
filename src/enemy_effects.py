class Effects:
    def __init__(self,effects:list):
        self.effects = effects
    def apply(self, player,enemy):
        for effect in self.effects:
            effect.apply(player,enemy)

class DamageEffect:
    def __init__(self,amount:int):
        self.amount = amount
    def apply(player,enemy):
        player.health 
        pass

