import random

class Card:
    def __init__(self, name:str, damage:int, block:int, mana:int, draw:int = 0):
        self.name = name
        self.damage = damage
        self.block = block
        self.mana = mana
        self.draw = draw

    def __repr__(self):
        return self.name

class Deck:
    def __init__(self, draw_pile: list=[], discard_pile: list = [], hand: list =[]):
        self.draw_pile = draw_pile
        self.discard_pile = discard_pile
        self.hand = hand
    
    def __str__(self):
        return(
            f"Draw Pile: {[card for card in self.draw_pile]}\n"
            f"Hand: {[card for card in self.hand]}\n"
            f"Discard Pile: {[card for card in self.discard_pile]}\n"
        )

    def add_cards(self, cards:list, place:str = "draw_pile") -> None:
        if (place == "draw_pile"):
            self.draw_pile.extend(cards)
        elif (place == "hand"):
            self.hand.extend(cards)
        elif(place == "discard_pile"):
            self.discard_pile.extend(cards)
        else:
            raise ValueError(f"Place {place} is not defined")
        
    def draw(self, card_draw:int) -> None:
        random.shuffle(self.draw_pile)
        for i in range(card_draw):
            if len(self.draw_pile) == 0 and len(self.discard_pile) == 0:
                return
            elif len(self.draw_pile) == 0:
                self.draw_pile = self.discard_pile
                self.discard_pile.clear()
                random.shuffle(self.draw_pile)
            self.hand.append(self.draw_pile[0])
            self.draw_pile.pop(0)
        
    def play(self, card: Card) -> list:
        if card.draw() > 0:
            self.add_cards(card.draw(), "draw_pile")
        return([card.damage(), card.block(), card.mana()])


