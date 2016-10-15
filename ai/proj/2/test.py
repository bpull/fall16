def alphaBeta(self, depth, turn):
    if depth == 0:
        return self.eval(turn)

    moves = []
    for i in range(7):
        if self.bcopy.b[0][i] == '\033[1;32;40m*':
            moves.append(i)

    alpha = float('-inf')

    for col in moves:
        self.bcopy.play_piece(col, turn)
        next_turn = 'B' if turn is 'R' else 'R'
        alpha = max(alpha, -self.alphaBeta(depth-1, next_turn))
        self.bcopy.undo(col)

    return alpha

def rootAlphaBeta(self):
    max_eval = float("-inf")
    alpha = float("-inf")
    best_move = -1

    self.copy()

    moves = []
    for i in range(7):
        if self.bcopy.b[0][i] == '\033[1;32;40m*':
            moves.append(i)

    for col in moves:
        self.bcopy.play_piece(col, 'B')
        alpha = -self.alphaBeta(self.depth-1,'R')
        self.bcopy.undo(col)

        if alpha > max_eval:
            max_eval = alpha
            best_move = col

    print ("best move is "+str(best_move)+" with value "+str(max_eval))
    return best_move
