class Heuristic:
    def __init__(self):
        # Alpha-Beta depth
        self.depth = 7
        # This heuristic assigns each field the number of possible connections with itself and size 4
        self.evaluationTable = [[3, 4, 5, 7, 5, 4, 3], 
                                [ 4, 6, 8, 10, 8, 6, 4],
                                [ 5, 8, 11, 13, 11, 8, 5], 
                                [ 5, 8, 11, 13, 11, 8, 5],
                                [ 4, 6, 8, 10, 8, 6, 4],
                                [ 3, 4, 5, 7, 5, 4, 3]]

    # Makes the Alpha-Beta & Minmax Algorithm move
    def make_ab_move(self, board, sym = "O"):
        # Alpha-Beta Algorithm
        valid_move = False
        while not valid_move:
            col = self.minmax(board, self.depth, sym)[1]
            valid_move = board.insert(board.get(), col, sym)

    # Started as MinMax using Alpha-Beta search
    def minmax(self, board, depth, player, maximizingPlayer = True, alpha = -9999, beta = 9999):
        # Get all possible steps
        steps = self.poss_steps(board.get())

        # Evaluate if endstate reached
        if depth == 0 or steps == []:
            wert = self.evaluate(board, player)
            return [wert, -1]

        # Maximizing Player
        if maximizingPlayer:
            # Init Maximizing Player
            maxValue = alpha
            bestStep = -1
            next_player = "O" if player=="X" else "X"

            # Setps all possible moves
            for step in steps:
                board.insert(board.get(), step, player)

                # Quick Evaluation if 4 CONNECTED then no need for further computation
                if board.check(board.get(), "O", 4) > 0:
                    board.uninsert(board.get(), step, player)
                    return [999,step]
                
                # MinMax Algorithm
                val = self.minmax(board, depth-1, next_player, False, maxValue, beta)[0]
                board.uninsert(board.get(), step, player)
                if val > maxValue:
                    bestStep = step
                    maxValue = val

                    # Alpha Beta Pruning
                    if maxValue >= beta:
                        break

            return [maxValue, bestStep]
        
        # Minimizing Player
        else:
            # Init Minimizing Player
            minValue = beta
            bestStep = -1
            next_player = "O" if player=="X" else "X"

            # Setps all possible moves
            for step in steps:
                board.insert(board.get(), step, player)

                # Quick Evaluation if 4 CONNECTED then no need for further computation
                if board.check(board.get(), "X", 4) > 0:
                    board.uninsert(board.get(), step, player)
                    return [-999,step]

                # MinMax Algorithm
                val = self.minmax(board, depth-1, next_player, True, alpha, minValue)[0]
                board.uninsert(board.get(), step, player)
                if val < minValue:
                    bestStep= step
                    minValue=val
                    
                    # Alpha Beta Pruning
                    if minValue <= alpha:
                        break

            return [minValue, bestStep]

    # Evaluation for Alpha-Beta algorithm
    def evaluate(self, board, player1 = "O"):
        # Init evaluate function
        player2 = "X" if player1=="O" else "O"
        # 138 * 2 = Entire block's sum in the evalutaion table
        utility = 138

        # Check first if connections with size 4 exist
        if board.check(board.get(), player1, 4) > 0:
            if board.check(board.get(), player2, 4) > 0:
                return 0
            return 2 * utility
        if board.check(board.get(), player2, 4) > 0:
            return -2 * utility

        board = board.get()
        # If not, use heuristic
        sum = 0
        for i in [0,1,2,3,4,5]:
            for j in [0,1,2,3,4,5,6]:
                if (board[i][j] == player1):
                    sum += self.evaluationTable[i][j]
                else:
                    if (board[i][j] == player2):
                        sum -= self.evaluationTable[i][j]
        return sum

    # Returns a list with free rows
    def poss_steps(self, board):
        ret = []
        for i in range(len(board[1])):
            if board[0][i]==" ":
                ret.append(i)
        return map(lambda x:x+1, ret)