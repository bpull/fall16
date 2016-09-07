#B.S.Pullig 175148
#SI420 Proj 1 - Fall 2016-2017
import numpy as np

class Board:

    def __init__(self):
        self.b = np.ndarray(shape=(6,7), dtype=(str,1))
        self.b.fill('*')

    def __repr__(self):
        for i in range(6):
            for j in range(7):
                print(str(self.b[i][j]), end="")
            print('')
        print ("1234567")
        return ""

    def play_piece(self, column, token):
        for i in range(5,-1,-1):
            try:
                if self.b[i][column] == '*':
                    self.b[i][column] = str(token)
                    return i
            except Exception as e:
                return False
        return False



class Game:

    def __init__(self):
        self.b = Board()
        self.turn = 'B'
        self.input = ''
        self.over = False

    def next_move(self):
        print (self.b)

        if self.turn == 'R':
            print ("Red player, what's your move?")
        else:
            print ("Black player, what's your move?")
        self.input = input()
        if self.input.isdigit():
            self.input = int(self.input) - 1

    def play_turn(self):
        outcome = self.b.play_piece(self.input, self.turn)
        if outcome is not False:
            self.check_win(outcome)
        else:
            print ("Invalid move! Please try again!")
            self.next_move()
            self.play_turn()

    def check_win(self, row):
        return

    def change_player(self):
        if self.turn is 'B':
            self.turn = 'R'
        else:
            self.turn = 'B'




if __name__ == '__main__':
    curGame = Game()

    while curGame.over is not True:
        curGame.change_player()
        curGame.next_move()
        curGame.play_turn()
