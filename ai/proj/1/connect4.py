#B.S.Pullig 175148
#SI420 Proj 1 - Fall 2016-2017
import numpy as np

class Board:

    def __init__(self):
        self.b = np.ndarray(size=(7,6), dtype=str)
        self.b.fill('*')

    def __repr__(self):
        for i in range(7):
            for j in range(6):
                print(str(self.b[i][j]), end="")
            print('')
        print ("1234567\n")

    def play_piece(self, column, token):
        for i in range(6):
            if self.b[column][i] == '*':
                self.b[column][i] = str(token)
                return true
        return false

class Player:

    def __init__(self, color):
        self.color = color
        self.win = False



class Game:

    def __init__(self):
        self.b = Board()
        self.red = Player('R')
        self.black = Player('B')
        self.turn = 'R'

    def next_move(self):
        if self.turn == 'R':
            print ("Red player, what's your move?\n")
        else:
            print ("Black player, what's your move?\n")

    def play_turn(self, column):
        '''start working here you twat'''

if __name__ == '__main__':
