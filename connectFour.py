import sys
import copy
import math

#read in command line arguements and ensure they are entered appropriately
#if not, print error message and exit with error
if (len(sys.argv) != 2):
    print("\nUsage: python connectFour.py 'number 1-8'\n")
    sys.exit(-1)

depth = int(sys.argv[1])
board = [[0 for j in range(7)] for i in range(7)]
current = [5 for j in range(7)]
turn = 1
moves = 0

MIN = -1000000
MAX = 1000000
win = 1000
loss = -1000

################### PRINT BOARD #####################

def print_board(temp_board):
	sys.stdout.write("\n")
	sys.stdout.flush()

	for i in range(7):
		for j in range(7):
			if i == 6:
				sys.stdout.write("%d" % (j+1))
				sys.stdout.flush()
			elif temp_board[i][j] == 0:
				sys.stdout.write(u'\u25E6')
				sys.stdout.flush()
			elif temp_board[i][j] == 1:
				sys.stdout.write(u'\u25A1')
				sys.stdout.flush()
			elif temp_board[i][j] == 10:
				sys.stdout.write(u'\u25A0')
				sys.stdout.flush()	
			if j != 6:
				sys.stdout.write(" ")
				sys.stdout.flush()
				
			
		sys.stdout.write("\n")
		sys.stdout.flush()

###################  VALID MOVE  #####################

def valid_move(temp_current, move):
	        
        move -= 1
	if move > -1 and move < 7 and temp_current[move] > -1:
		return True
	else:
		return False

###################  MAKE MOVE  #####################

def make_move(temp_board, temp_current, x, turn):
	x -= 1
	#print "%d, %d, %d" % (x, current[x], turn)
	temp_board[temp_current[x]][x] = turn
	temp_current[x] -= 1

	if check_winner(temp_board, turn):
		return 1
	else:
		return 0
	
################  CHECK WINNER  ######################

def check_winner(temp_board, player):
	for y in range(7):
        	for x in range(3):
        		if temp_board[x][y] == player and temp_board[x+1][y] == player and temp_board[x+2][y] == player and temp_board[x+3][y] == player:
                		return True

    # check vertical spaces
	for x in range(6):
		for y in range(4):
			if temp_board[x][y] == player and temp_board[x][y+1] == player and temp_board[x][y+2] == player and temp_board[x][y+3] == player:
                		return True

    # check / diagonal spaces
	for x in range(3):
		for y in range(3, 7):
			if temp_board[x][y] == player and temp_board[x+1][y-1] == player and temp_board[x+2][y-2] == player and temp_board[x+3][y-3] == player:
				return True

    # check \ diagonal spaces
    	for x in range(3):
        	for y in range(4):
            		if temp_board[x][y] == player and temp_board[x+1][y+1] == player and temp_board[x+2][y+2] == player and temp_board[x+3][y+3] == player:
                		return True
	return False

##################  COMPUTER MOVE  ######################

def computer_move():
	move = 0
	best = 0
	alpha = MIN
	beta = MAX
	for i in range(1, 8):
		if valid_move(current, i):
			potential = eval_move(copy.deepcopy(board), copy.deepcopy(current), i, 1, alpha, beta)	
		#	print "POTENTIAL MOVE VALUE: %d" % (potential)
			if potential > alpha:
				alpha = potential
				move = i
				
	return make_move(board, current, move, 10)


####################  EVAL MOVE  ########################

def eval_move(temp_board, temp_current, move, level, alpha, beta):
	if level % 2 == 0:
		temp_turn = 1
	else:
		temp_turn = 10

	temp = make_move(temp_board, temp_current, move, temp_turn)		
#	print_board(temp_board)
#	print "potential win: %d" % (temp)
	
	#DETERMINE IF SOMEONE WON
	if temp == 1:
		if level %2 == 0:
			return loss
		else:
			return win
	elif level == depth:
		return eval_board(temp_board)
	else:

		#PRUNE DEPENDING ON ALPHA BETA AND MIN/MAX STATUS
		if level % 2 == 0:
			for i in range(1,8):
				if valid_move(temp_current, i):
					potential = eval_move(copy.deepcopy(temp_board), copy.deepcopy(temp_current), i, level + 1, alpha, beta)
					if potential > alpha:
						alpha = potential
					if beta <= alpha:
						return alpha
			return alpha
		else:
			for i in range(1,8):
				if valid_move(temp_current, i):
					potential = eval_move(copy.deepcopy(temp_board), copy.deepcopy(temp_current), i, level + 1, alpha, beta)
					if potential < beta:
						beta = potential
					if beta <= alpha:
						return beta
			return beta

####################  EVAL BOARD  #######################

def eval_board(temp_board):
	score = 0
 	score = check_three_pair(temp_board)
	return score

######################  MAIN  ###########################

def check_three_pair(temp_board):
	score = 0
	for y in range(7):
                for x in range(3):
                        if temp_board[x][y] + temp_board[x+1][y] + temp_board[x+2][y] + temp_board[x+3][y] == 3:
                                score += 10
                        elif temp_board[x][y] + temp_board[x+1][y] + temp_board[x+2][y] + temp_board[x+3][y] == 30:
				score -= 10
    # check vertical spaces
        for x in range(6):
                for y in range(4):
                        if temp_board[x][y] + temp_board[x][y+1] + temp_board[x][y+2] + temp_board[x][y+3] == 3:
                                score += 10
                        elif temp_board[x][y] + temp_board[x][y+1] + temp_board[x][y+2] + temp_board[x][y+3] == 30:
				score -= 10

    # check / diagonal spaces
        for x in range(3):
                for y in range(3, 7):
                        if temp_board[x][y] + temp_board[x+1][y-1] + temp_board[x+2][y-2] + temp_board[x+3][y-3] == 3:
                                score += 10
                        elif temp_board[x][y] + temp_board[x+1][y-1] + temp_board[x+2][y-2] + temp_board[x+3][y-3] == 30:
                                score -= 10

    # check \ diagonal spaces
        for x in range(3):
                for y in range(4):
                        if temp_board[x][y] + temp_board[x+1][y+1] + temp_board[x+2][y+2] + temp_board[x+3][y+3] == 3:
                                score += 10
                        elif temp_board[x][y] + temp_board[x+1][y+1] + temp_board[x+2][y+2] + temp_board[x+3][y+3] == 30:
                                score -= 10
        return score

######################  MAIN  ###########################

player_1 = raw_input("Human or Computer First -- h == human && c == computer: ")

if player_1 is 'h':
	turn = 10
else:
	turn = 1

print_board(board)

if turn == 10:
	move = raw_input("HUMAN's Move -- enter Q to quit: ")
	turn = 1
else:
	print "COMPUTER'S Move -- enter Q to quit: "	
	move = 0
        turn = 10

while(move != 'Q'):
	if turn == 1:
            #check valid input
            if (len(move) != 1):
                temp = -1
            elif (not move.isdigit()):
                temp = -1

            elif not valid_move(current, int(move)):
                temp = -1
            else:
                #print current
                temp = make_move(board, current, int(move), turn)

	else:
		temp = computer_move()

	if temp == 1:
		print_board(board)
		if turn == 1:
                	print "--------------HUMAN WINS----------------"
                else:
                       	print "-------------COMPUTER WINS----------------"
		break
	elif temp == 0:
		print_board(board)
		moves += 1
		if moves == 42:
			print "---------------BOARD IS FULL----------------"
			break
		if turn == 1:
			print "COMPUTER'S Move -- enter Q to quit: "	
			turn = 2
		else:
			move = raw_input("HUMAN's Move -- enter Q to quit: ")
			turn = 1
	else:
		if turn == 1:
			move = raw_input("ILLEGAL INPUT -- HUMAN's Move -- enter Q to quit: ")
		else:
			print "ILLEGAL INPUT -- COMPUTER's Messed Up -- "
			move = 'Q'
