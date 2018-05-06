import pickle

class Heuristic:
    def __init__(self):
        # Search depth, that should be even number
        self.depth = 6
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
            valid_move = board.insert(board.get(), col, sym, _print = True)

    # Started as MinMax using Alpha-Beta search
    def minmax(self, board, depth, player, maximizingPlayer = True, alpha = -9999, beta = 9999):
        # Get all possible steps
        steps = board.poss_steps(board.get())

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
        player2 = "X" if player1 == "O" else "O"
        # 138 * 2 = Entire block's sum in the evalutaion table
        utility = 300

        # Check first if connections with size 4 exist
        if board.check(board.get(), player1, 4) > 0:
            if board.check(board.get(), player2, 4) > 0:
                return 0
            return 2 * utility
        if board.check(board.get(), player2, 4) > 0:
            return -2 * utility

        tmp_board = board.get()
        # If not, use heuristic
        sum = 0
        for i in [0,1,2,3,4,5]:
            for j in [0,1,2,3,4,5,6]:
                if (tmp_board[i][j] == player1):
                    sum += self.evaluationTable[i][j]
                else:
                    if (tmp_board[i][j] == player2):
                        sum -= self.evaluationTable[i][j]

        # 내가 돌을 놓은 다음 상황에서,
        # 1) 내 돌이 3개 연속인 경우 * 3 의 Weight 를 준다
        # 2) 상대방의 돌이 2개 연속인 경우 * 3 의 - Weight 를 준다. (상대방이 돌을 놓아 3개가 만들어질 경우에 대해 미리 방지)
        # 3) 내 돌이 2개 연속인 경우 * 1 의 Weight 를 준다.
        sum += board.check(board.get(), player1, 3) * 3 + board.check(board.get(), player1, 2) * 1
        sum -= board.check(board.get(), player2, 2) * 2

        return sum

class NN_Heuristic:
    def __init__(self):
        # Search depth, that should be even number
        self.depth = 6

        # Load MLP Classifier
        self.MLP_classifier = pickle.load(open('model/MLP.data', 'rb'))

    # Makes the Alpha-Beta & Minmax Algorithm move
    def make_ab_move(self, board, sym = "O"):
        # Alpha-Beta Algorithm
        valid_move = False
        while not valid_move:
            col = self.minmax(board, self.depth, sym)[1]
            valid_move = board.insert(board.get(), col, sym, _print = True)

    # Started as MinMax using Alpha-Beta search
    def minmax(self, board, depth, player, maximizingPlayer = True, alpha = -9999, beta = 9999):
        # Get all possible steps
        steps = board.poss_steps(board.get())

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
        player2 = "X" if player1 == "O" else "O"
        # 0.5 * 2 = Max Value
        utility = 0.51

        # Check first if connections with size 4 exist
        if board.check(board.get(), player1, 4) > 0:
            if board.check(board.get(), player2, 4) > 0:
                return 0
            return 2 * utility
        if board.check(board.get(), player2, 4) > 0:
            return -2 * utility

        # If not, use heuristic
        predict = self.MLP_classifier.predict_proba(board.getData())
        
        return (predict[0][2] - predict[0][0])
