import numpy as np
from random import choice

class Player:
    def __init__(self,decetioner):
        self.cards_in_hand = []
        self.info_table = np.zeros((4, 9))
        
    def move(self, opotunity, table):
        pass
    
    def card_on_table(self, card):
        pass
    
    def card_out_game(self, card):
        pass
        
    def card_in_enemy(self, card):
        pass
        
    def trumb(self, card):
        pass
        
    def get_card(self, card):
        pass
    
    def drop_card(self, card):
        pass
        
class Random_Player(Player):
    def __init__(self,decetioner = None):
        super().__init__(Player)
        self.card_in_game = None
        self.decetioner = decetioner
        
    def clear(self):
        self.cards_in_hand = []
        self.info_table = np.zeros((4, 9))
        
    def move(self, opotunity, table):
        t =list(set(tuple(i) for i in opotunity))
        if len(t) == 0:
            return -1
        try:
            card = list(choice(t))
            if self.decetioner is not None:
                self.decetioner.collect_info(self.info_table, t, table)
            self.info_table[card[0], card[1]] = 2
            return card
        except:
            return -1
    
    def card_on_table(self, card):
        self.info_table[card[0], card[1]] = 2
    
    def card_out_game(self, card):
        self.info_table[card[0], card[1]] = -2
        
    def card_in_enemy(self, card):
        self.info_table[card[0], card[1]] = -1
        
    def trumb(self, card):
        self.info_table[card[0], card[1]] = -3
        
    def get_card(self, card):
        self.cards_in_hand.append(card)
        self.info_table[card[0], card[1]] = 1
    
    def drop_card(self, card):
        self.cards_in_hand.remove(card)