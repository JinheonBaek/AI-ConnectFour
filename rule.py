class Rule:
    # Computer's Symbol: O
    def make_move(self, board, sym = "O"):
        col = self.evaluate(board, sym)
        board.insert(board.get(), col, sym)
    
    ## 3개 판단
    ## BFS 이용
    
    def evaluate(self, board, player = "O"):
        # Init
        curValue = 0
        maxValue = 0
        bestStep = -1
        
        # Get all possible steps
        steps = self.poss_steps(board.get())

        # Setps all possible moves
        for step in steps:
            board.insert(board.get(), step, player)

            curValue = self.dfs(board.get(), 0)

            if curValue > maxValue :
                maxValue = curValue
                bestStep = step

            board.uninsert(board.get(), step, player)
    

        return bestStep

    def dfs(self, board, depth = 0):

        return 3

    # Returns a list with free rows
    def poss_steps(self, board):
        ret = []
        for i in range(len(board[1])):
            if board[0][i]==" ":
                ret.append(i)
        return map(lambda x:x+1, ret)
