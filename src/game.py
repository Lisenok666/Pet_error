import numpy as np

from random import shuffle, randint


class Game:
    def __init__(self, n = 4, k = 9, take_cards = 6):
        self.cards = []
        self.n = n
        self.k = k
        self.take_cards = take_cards
        self.trump = 0
        
        for i in range(n):
            for j in range(k):
                self.cards.append([i, j])
        shuffle(self.cards)
        #print(f'{len(self.cards)}')

    def get_opotunity(self, card, hand):
        opotunity = []
        for el in hand:
            if card[0] == self.trump:
                if el[1] > card[1]:
                     opotunity.append(el)
            else:
                if el[0] == self.trump:
                    opotunity.append(el)
                elif el[1] > card[1] and el[0] == card[0]:
                     opotunity.append(el)
        if len(opotunity):
            return opotunity
        else:
            return -1
    
    def get_opotunity_atack(self, table, hand):
        if len(hand) == 0:
            return -1
        elif len(table) == 0:
            return hand
        else:
            opotunity = []
            oposite = list(set([el[1] for el in table]))
            for el in hand:
                if el[1] in oposite:
                      opotunity.append(el)
        if len(opotunity):
            return opotunity
        return -1
    
    def playing(self, player1, player2):
        for i in range(self.take_cards):
            player1.get_card(self.cards.pop())
            player2.get_card(self.cards.pop())
        
        player1.card_in_game = len(self.cards)
        player2.card_in_game = len(self.cards)
        player1.trumb = self.cards[0]
        player2.trumb = self.cards[0]
        play = randint(0,1)
        #print(f'Козырь =  {self.trump}')
        while(len(player1.cards_in_hand) > 0 and len(player2.cards_in_hand) > 0):
            if play % 2 == 0:
                play += self.play_move(player1, player2)
            else:
                play += self.play_move(player2, player1)
                
        # результат игры       
        if len(player1.cards_in_hand) == 0 and len(player2.cards_in_hand) == 0:
            return 0
        elif len(player1.cards_in_hand) == 0:
            return 1
        else:
            return -1
        
                
    def play_move(self, player1, player2):
        table = []
        can_move = 1
        defence_win = 0
        while can_move:
            op = self.get_opotunity_atack(table, player1.cards_in_hand)
            if op != -1:
                attack_card = player1.move(op, table)
                player2.card_on_table(attack_card)
                table.append(attack_card)
                player1.drop_card(attack_card)
                
                op = self.get_opotunity(table[-1], player2.cards_in_hand)
                if op != -1:
                    defence_card = player2.move(op, table)
                    player1.card_on_table(defence_card)
                    table.append(defence_card)  
                    player2.drop_card(defence_card)
                else:
                    can_move = 0
            else:
                can_move = 0
                defence_win = 1
        
        if defence_win:
            if len(player1.cards_in_hand) < self.take_cards:
                for i in range(self.take_cards - len(player1.cards_in_hand)):
                    try:
                        player1.get_card(self.cards.pop())
                    except:
                        pass
            if len(player2.cards_in_hand) < self.take_cards:
                for i in range(self.take_cards - len(player2.cards_in_hand)):
                    try:
                        player2.get_card(self.cards.pop())
                    except:
                        pass
            for el in table:
                player2.card_out_game(el)
                player1.card_out_game(el)
                
        else:
            if len(player1.cards_in_hand) < self.take_cards:
                for i in range(self.take_cards - len(player1.cards_in_hand)):
                    try:
                        player1.get_card(self.cards.pop())
                    except:
                        pass
            for el in table:
                player2.get_card(el)
                player1.card_in_enemy(el)
        #print(player1.info_table, player2.info_table, table)
        player1.card_in_game = len(self.cards)
        player2.card_in_game = len(self.cards)
        return defence_win