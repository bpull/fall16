#B.S.Pullig 175148
#SI420 Proj 2- Fall 2016-2017
import numpy as np
import sys

class Board:

    #create board full of empty spots
    def __init__(self):
        self.b = np.ndarray(shape=(6,7), dtype=(str,11))
        self.b.fill("\033[1;32;40m*")

    #print board
    def __repr__(self):
        for i in range(6):
            for j in range(7):
                print(str(self.b[i][j]), end="\033[1;32;40m")
            print('')
        print ("\033[1;32;40m1234567")
        return ""

    #attempts to place a piece into the board. if successful, it will return the row in which it landed
    #if not successful, it will return false
    def play_piece(self, column, token):
        for i in range(5,-1,-1):
            try:
                if self.b[i][column] == "\033[1;32;40m*":
                    if token == 'B':
                        self.b[i][column] = str("\033[1;30;40m") + str(token)
                    else:
                        self.b[i][column] = str("\033[1;31;41m") + str(token)
                    return i
            except Exception as e:
                return False
        return False

    def undo(self, column):
        for i in range(6):
            if self.b[i][column] != "\033[1;32;40m*":
                self.b[i][column] = "\033[1;32;40m*"
                return

class Game:

    #class definition to hold the board and keep track of the turn, input, and if the game is still running
    def __init__(self, depth, first, debug=False):
        self.b = Board()
        self.bcopy = Board()
        if first is 'h':
            self.turn = 'B'
        elif first is 'c':
            self.turn = 'R'
        self.input = ''
        self.over = False
        self.depth = int(depth)
        self.debug = debug

    def copy(self):
        self.bcopy.b = np.copy(self.b.b)

    #prints the current board and saves the next input from the human
    def next_move(self, col=False):
        if col is False:
            print (self.b)

            if self.turn == 'R':
                print ("Red player, what's your move?")
            else:
                print ("Black player, what's your move?")
            self.input = input()
            if self.input.isdigit():
                if int(self.input) == 0:
                    self.input = 10
                self.input = int(self.input) - 1
        else:
            self.input = int(col)

    #
    def play_turn(self):
        outcome = self.b.play_piece(self.input, self.turn)
        if outcome is not False:
            self.over,junkB,junkR,jB,jR = self.check_win()
        else:
            print ("Invalid move! Please try again!")
            self.next_move()
            self.play_turn()

    #check all verticals, horizontals, and diagonals for 4 in a row
    def check_win(self,eval=False):
        '''check board state for a winning combination. there are only 25 possible straights that can contain 4 in a row'''

        max_niar_B = 0
        max_niar_R = 0
        two_niar_B = 0
        two_niar_R = 0
        num_in_a_row = 0
        token_counted = '\033[1;32;40m*'
        cur_token = ''
        last_play_token = ''
        board = None

        if eval:
            board = self.bcopy.b
        else:
            board = self.b.b

        #check all verticals
        for col in range (7):
            for row in range(5,-1,-1):

                cur_token = board[row][col]

                if cur_token != '\033[1;32;40m*':
                    if cur_token == token_counted:
                        num_in_a_row = num_in_a_row + 1
                        if token_counted == '\033[1;30;40mB':
                            if num_in_a_row == 1 and last_play_token == '\033[1;30;40mB':
                                two_niar_B += 1
                            elif num_in_a_row == 2 and last_play_token == '\033[1;30;40mB':
                                max_niar_B += 1
                            elif num_in_a_row == 2:
                                two_niar_B += 1
                            elif num_in_a_row == 3:
                                max_niar_B += 1
                        else:
                            if num_in_a_row == 1 and last_play_token == '\033[1;31;41mR':
                                two_niar_R += 1
                            elif num_in_a_row == 2 and last_play_token == '\033[1;31;41mR':
                                max_niar_R += 1
                            if num_in_a_row == 2:
                                two_niar_R += 1
                            elif num_in_a_row == 3:
                                max_niar_R += 1
                    else:
                        if token_counted == '\033[1;30;40mB':
                            if num_in_a_row == 2:
                                two_niar_B -= 1
                            elif num_in_a_row == 3:
                                max_niar_B -= 1
                        else:
                            if num_in_a_row == 2:
                                two_niar_R -= 1
                            elif num_in_a_row == 3:
                                max_niar_R -= 1
                        num_in_a_row = 1
                        token_counted = cur_token
                else:
                    num_in_a_row = 0
                    last_play_token = token_counted
                    token_counted = '\033[1;32;40m*'

                if num_in_a_row == 4:
                    return True,max_niar_B,max_niar_R,two_niar_B,two_niar_R

            num_in_a_row = 0
            token_counted = '\033[1;32;40m*'
            cur_token = ''

        #check all horizontals
        for row in range (6):
            for col in range(7):

                cur_token = board[row][col]

                if cur_token != '\033[1;32;40m*':
                    if cur_token == token_counted:
                        num_in_a_row = num_in_a_row + 1
                        if token_counted == '\033[1;30;40mB':
                            if num_in_a_row == 1 and last_play_token == '\033[1;30;40mB':
                                two_niar_B += 1
                            elif num_in_a_row == 2 and last_play_token == '\033[1;30;40mB':
                                max_niar_B += 1
                            elif num_in_a_row == 2:
                                two_niar_B += 1
                            elif num_in_a_row == 3:
                                max_niar_B += 1
                        else:
                            if num_in_a_row == 1 and last_play_token == '\033[1;31;41mR':
                                two_niar_R += 1
                            elif num_in_a_row == 2 and last_play_token == '\033[1;31;41mR':
                                max_niar_R += 1
                            if num_in_a_row == 2:
                                two_niar_R += 1
                            elif num_in_a_row == 3:
                                max_niar_R += 1
                    else:
                        if token_counted == '\033[1;30;40mB':
                            if num_in_a_row == 2:
                                two_niar_B -= 1
                            elif num_in_a_row == 3:
                                max_niar_B -= 1
                        else:
                            if num_in_a_row == 2:
                                two_niar_R -= 1
                            elif num_in_a_row == 3:
                                max_niar_R -= 1
                        num_in_a_row = 1
                        token_counted = cur_token
                else:
                    num_in_a_row = 0
                    last_play_token = token_counted
                    token_counted = '\033[1;32;40m*'

                if num_in_a_row == 4:
                    return True,max_niar_B,max_niar_R,two_niar_B,two_niar_R

            num_in_a_row = 0
            token_counted = '\033[1;32;40m*'
            cur_token = ''

        #check all left slanted diagonals
        ranges = [range(5,1,-1), range(5,0,-1), range(5,-1,-1), range(5,-1,-1), range(4,-1,-1), range(3,-1,-1)]
        for cur_range,j in zip(ranges,range(2,-4,-1)):
            for i in cur_range:

                cur_token = board[i][i-j]

                if cur_token != '\033[1;32;40m*':
                    if cur_token == token_counted:
                        num_in_a_row = num_in_a_row + 1
                        if token_counted == '\033[1;30;40mB':
                            if num_in_a_row == 1 and last_play_token == '\033[1;30;40mB':
                                two_niar_B += 1
                            elif num_in_a_row == 2 and last_play_token == '\033[1;30;40mB':
                                max_niar_B += 1
                            elif num_in_a_row == 2:
                                two_niar_B += 1
                            elif num_in_a_row == 3:
                                max_niar_B += 1
                        else:
                            if num_in_a_row == 1 and last_play_token == '\033[1;31;41mR':
                                two_niar_R += 1
                            elif num_in_a_row == 2 and last_play_token == '\033[1;31;41mR':
                                max_niar_R += 1
                            if num_in_a_row == 2:
                                two_niar_R += 1
                            elif num_in_a_row == 3:
                                max_niar_R += 1
                    else:
                        if token_counted == '\033[1;30;40mB':
                            if num_in_a_row == 2:
                                two_niar_B -= 1
                            elif num_in_a_row == 3:
                                max_niar_B -= 1
                        else:
                            if num_in_a_row == 2:
                                two_niar_R -= 1
                            elif num_in_a_row == 3:
                                max_niar_R -= 1
                        num_in_a_row = 1
                        token_counted = cur_token
                else:
                    num_in_a_row = 0
                    last_play_token = token_counted
                    token_counted = '\033[1;32;40m*'

                if num_in_a_row == 4:
                    return True,max_niar_B,max_niar_R,two_niar_B,two_niar_R

            num_in_a_row = 0
            token_counted = '\033[1;32;40m*'
            cur_token = ''

        #check all right slanted straights
        xranges = [range(3,-1,-1),range(4,-1,-1),range(5,-1,-1),range(5,-1,-1),range(5,0,-1),range(5,1,-1)]
        yranges = [range(4), range(5), range(6), range(1,7), range(2,7), range(3,7)]
        for rows,cols in zip(xranges,yranges):
            for i,j in zip(rows,cols):

                cur_token = board[i][j]


                if cur_token != '\033[1;32;40m*':
                    if cur_token == token_counted:
                        num_in_a_row = num_in_a_row + 1
                        if token_counted == '\033[1;30;40mB':
                            if num_in_a_row == 1 and last_play_token == '\033[1;30;40mB':
                                two_niar_B += 1
                            elif num_in_a_row == 2 and last_play_token == '\033[1;30;40mB':
                                max_niar_B += 1
                            elif num_in_a_row == 2:
                                two_niar_B += 1
                            elif num_in_a_row == 3:
                                max_niar_B += 1
                        else:
                            if num_in_a_row == 1 and last_play_token == '\033[1;31;41mR':
                                two_niar_R += 1
                            elif num_in_a_row == 2 and last_play_token == '\033[1;31;41mR':
                                max_niar_R += 1
                            if num_in_a_row == 2:
                                two_niar_R += 1
                            elif num_in_a_row == 3:
                                max_niar_R += 1
                    else:
                        if token_counted == '\033[1;30;40mB':
                            if num_in_a_row == 2:
                                two_niar_B -= 1
                            elif num_in_a_row == 3:
                                max_niar_B -= 1
                        else:
                            if num_in_a_row == 2:
                                two_niar_R -= 1
                            elif num_in_a_row == 3:
                                max_niar_R -= 1
                        num_in_a_row = 1
                        token_counted = cur_token
                else:
                    num_in_a_row = 0
                    last_play_token = token_counted
                    token_counted = '\033[1;32;40m*'

                if num_in_a_row == 4:
                    return True,max_niar_B,max_niar_R,two_niar_B,two_niar_R

            num_in_a_row = 0
            token_counted = '\033[1;32;40m*'
            cur_token = ''

        return False,max_niar_B,max_niar_R,two_niar_B,two_niar_R

    #change who is playing; if B, then R. if R, then B
    def change_player(self):
        if self.turn is 'B':
            self.turn = 'R'
        else:
            self.turn = 'B'

    #print who the winner is
    def print_winner(self):
        if self.turn is 'B':
            print("Black Wins!")
        else:
            print("Red Wins!")

    def eval(self, turn):
        #will check if the opposite person won because it was changes since last play
        over, max_niar_B, max_niar_R, two_niar_B, two_niar_R = self.check_win(eval=True)

        if self.debug:
            print (self.bcopy)

        if over:
            if turn is 'B':
                if self.debug:
                    print("Eval = -100000000")
                    a = input()
                return -100000000
            else:
                if self.debug:
                    print("Eval = 100000000")
                    a = input()
                return 100000000
        else:
            score =  (20*max_niar_B+1)**4 - (20*max_niar_R)**4
            score += (20*two_niar_B+1)**3 - (20*two_niar_R)**3
            if self.debug:
                print ("Eval = "+str(score))
                a = input()
            return score

    #inspiration taken from stackoverflow regarding alphaBeta pruning.
    #http://stackoverflow.com/questions/12569392/alpha-beta-algorithm-extracting-move
    def alphaBeta(self, depth, alpha, beta, turn):
        if depth == 0:
            return self.eval(turn)

        moves = []
        for i in range(7):
            if self.bcopy.b[0][i] == '\033[1;32;40m*':
                moves.append(i)

        for col in moves:
            self.bcopy.play_piece(col, turn)
            next_turn = 'B' if turn is 'R' else 'R'
            cur_eval = -self.alphaBeta(depth-1, -beta, -alpha, next_turn)
            self.bcopy.undo(col)

            if cur_eval >= beta:
                return beta
            if cur_eval > alpha:
                alpha = cur_eval

        return alpha

    def rootAlphaBeta(self):
        max_eval = -float("inf")
        alpha = float("inf")
        best_move = 0

        self.copy()

        moves = []
        for i in range(7):
            if self.bcopy.b[0][i] == '\033[1;32;40m*':
                moves.append(i)

        for col in moves:
            self.bcopy.play_piece(col, 'B')
            alpha = -self.alphaBeta(self.depth-1, -float("inf"), alpha, 'R')
            self.bcopy.undo(col)

            if alpha > max_eval:
                max_eval = alpha
                best_move = col

        return best_move

#if running from the terminal, start the game
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print ("usage: python3 connect4.py <depth>")
        sys.exit(1)
    elif sys.argv[1].isdigit():
        print ("Will the Human or Computer play first? (h/c)")
        play = input()
        if play is 'h' or play is 'c':
            if len(sys.argv) > 2:
                curGame = Game(sys.argv[1], play, debug=True)
            else:
                curGame = Game(sys.argv[1], play)
            #the game is just a cycle of changing players, reading input, and playing the piece
            while curGame.over is not True:
                curGame.change_player()
                if curGame.turn is 'R':
                    curGame.next_move()
                    curGame.play_turn()
                else:
                    col = curGame.rootAlphaBeta()
                    curGame.next_move(col)
                    curGame.play_turn()

            print(curGame.b)
            print("Game Over!")
            curGame.print_winner()
        else:
            print ("Invalid input")
            sys.exit(1)
    else:
        print ("Invalid input")
        sys.exit(1)
