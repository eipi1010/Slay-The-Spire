from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities.creatures.monster import Monster

import random
import math

class Player:
    def __init__(self, deck:list,health:int):
        
        #Resources 
        self.health=health
        self.max_health=health
        self.mana=0
        self.block=0
        
        #CardsPiles
        self.deck = deck
        self.hand = []
        self.discard_pile = []
        self.exhaust_pile = []

        #Buffs
        self.powers = []
        self.relics = []

        #Debuffs
        self.weak = 0
        self.vulnerable = 0
        self.frail = 0

    
    def __str__(self):
        return(
            "---Ironclad Stats---\n"
            f"Health: {self.health}:\n"
            f"Block: {self.block}:\n"
            f"Draw Pile: {[card for card in self.deck]}\n"
            f"Hand: {[card for card in self.hand]}\n"
            f"Discard Pile: {[card for card in self.discard_pile]}\n"
            f"Exhaust Pile: {[card for card in self.exhaust_pile]}"
        )

    def start_turn(self):
        self.mana = 3
        self.draw(5)
        self.block = 0

    def play_one_turn_randomly(self,enemies):
        for i in range(len(self.hand)):
            if self.execute_card_play(card_index=random.randint(0,len(self.hand)-1),enemies=enemies,target_index=0):
                return True
        return False


    def play_randomly(self,enemies):
        for i in range(len(self.hand)):
            if self.execute_card_play(card_index=0,enemies=enemies,target_index=0):
                i = 0

    def execute_card_play(self, card_index, target_index, enemies):
        card = self.hand[card_index]

        if self.hand[card_index].mana > self.mana:
            return False
        
        self.mana -= card.mana

        self.hand.pop(card_index)

        card.play(self, enemies, target_index)

        if card.exhaust == True:
            self.exhaust_pile.append(card)
        elif card.type == "Power":
            self.powers.append(card) # Or just let it exist in the "active" zone
        else:
            self.discard_pile.append(card)
        return True

    def end_turn(self):
        self.discard_pile.extend(self.hand)
        self.weak = max(0,self.weak-1)
        self.vulnerable = max(0,self.vulnerable-1)
        self.frail = max(0,self.frail-1)
        self.hand.clear()


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

    def take_damage(self,amount:int):
        if self.block >= amount:
            self.block -= amount
        else:
            health_lost = amount - self.block
            self.health = max(self.health - health_lost,0)

    def gain_block(self,amount:int):
        if self.frail >= 1:
            amount = math.floor(amount * 0.75)
        self.block += amount
        


'''
    def play(self, card_index:int, enemies:list["Monster"],target_index:int = 0) -> bool:
        if self.hand[card_index].mana > self.mana:
            return False
        self.mana -= self.hand[card_index].mana
        self.hand[card_index].play(self, enemies, target_index)
        return True


'''







