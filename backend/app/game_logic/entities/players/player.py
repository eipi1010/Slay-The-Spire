import random

#ADDDDD WEAK



class Player:
    def __init__(
            self, deck:list,
            health:int = 87,
            mana:int = 0,
            block:int = 0,
            hand: list =None,
            discard_pile: list =None,
            exhaust_pile =None,
            weak:int = 0,
            vulnerable:int = 0
                 ):
        
        #Resources 
        self.health = health
        self.mana=mana
        self.block=block
        
        #CardsPiles
        self.deck = deck
        self.hand = hand if hand is not None else []
        self.discard_pile = discard_pile if discard_pile is not None else []
        self.exhaust_pile = exhaust_pile if exhaust_pile is not None else []

        #Debuffs
        self.weak = weak
        self.vulnerable = vulnerable

    
    def __str__(self):
        return(
            "---Ironclad Stats---\n"
            f"Health: {self.health}:\n"
            f"Draw Pile: {[card for card in self.deck]}\n"
            f"Hand: {[card for card in self.hand]}\n"
            f"Discard Pile: {[card for card in self.discard_pile]}\n"
            f"Exhaust Pile: {[card for card in self.exhaust_pile]}"
        )

    def start_turn(self):
        self.mana = 3
        self.discard_pile.extend(self.hand)
        self.block = 0
        self.weak = max(0,self.weak-1)
        self.vulnerable = max(0,self.vulnerable-1)
        self.hand.clear()
        self.draw(5)
    
    def take_damage(self,amount:int):
        if self.block >= amount:
            self.block - amount
        else:
            health_lost = amount - self.block
            self.health -= health_lost

    def draw(self, card_draw:int) -> None:
        if len(self.deck) != 0:
            random.shuffle(self.deck)
        for i in range(card_draw):
            if len(self.deck) == 0 and len(self.discard_pile) == 0:
                return
            elif len(self.deck) == 0:
                self.deck = self.discard_pile.copy()
                self.discard_pile.clear()
                random.shuffle(self.deck)
            self.hand.append(self.deck[0])
            self.deck.pop(0)
        
    def play(self, card_index:int, enemies, enemy_index:int = 0) -> bool:
        if self.hand[card_index].mana > self.mana:
            return False
        self.mana -= self.hand[card_index].mana
        self.hand[card_index].play(card_index, self, enemies, enemy_index)
        return True






