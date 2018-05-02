class Rule:
    # Computer's Symbol: O
    def make_move(self, board, sym = "O"):
        col = self.rule(board, sym)
        board.insert(board.get(), col, sym)
    
    ## 3개 판단
    ## BFS 이용
    
    def rule(self, board, player = "O"):
        # Init
        curValue = 0
        maxValue = 0
        bestStep = 3

        next_player = "X" if player == "O" else "O"
        
        # Get all possible steps
        steps = self.poss_steps(board.get())

        # Rule 1 (내 승리 조건 확인하기)
        for step in steps:
            board.insert(board.get(), step, player)

            if board.check(board.get(), player, 4) > 0:
                board.uninsert(board.get(), step, player)
                return step
            
            board.uninsert(board.get(), step, player)

        # Get all possible steps
        steps = self.poss_steps(board.get())

        # Rule 2 (상대방 승리 조건 막기)
        for step in steps:
            board.insert(board.get(), step, next_player)

            if board.check(board.get(), next_player, 4) > 0:
                board.uninsert(board.get(), step, next_player)
                return step

            board.uninsert(board.get(), step, next_player)

        # Get all possible steps
        steps = self.poss_steps(board.get())

        # Rule 3 (상대방이 Row 상에 연속된 3개의 돌을 구현하는 것을 막기)
        # Rule 3 (Row 상에 연속된 3개의 돌이 있고, 양 옆 공간이 비어있는 상황을 미연에 방지하기 위함임)
        for step in steps:
            board.insert(board.get(), step, next_player)

            if self.row_check(board.get(), step, next_player, 3) > 0:
                board.uninsert(board.get(), step, next_player)
                return step

            board.uninsert(board.get(), step, next_player)

        # Get all possible steps
        steps = self.poss_steps(board.get())

        # Rule 4 (내가 Row 상에 연속된 3개의 돌을 두기)
        # Rule 4 (Rule 3 과 비슷한 아이디어에서 도출, 내가 유리한 조건 끌어내기)
        for step in steps:
            board.insert(board.get(), step, player)

            if self.row_check(board.get(), step, player, 3) > 0:
                board.uninsert(board.get(), step, player)
                return step

            board.uninsert(board.get(), step, player)

        # Rule 5 (Some eval function)
        steps = self.poss_steps(board.get())
        
        for step in steps:
            board.insert(board.get(), step, player)
            
            curValue = self.evaluate(board, player)

            if curValue >= maxValue :
                maxValue = curValue
                bestStep = step

            board.uninsert(board.get(), step, player)

        return bestStep
    
    def row_check(self, board, step, symbol, connectNum):
        # Init
        height = -1

        # Finds step columns's height (0 is top / 5 is bottom in board index)
        # Height is 5, 0 ~ 4 indexes on that column is free
        for i in range(len(board)):
            if board[5 - i][step - 1] == " ":
                height = 6 - i
                break

        # That column is already full, search next column to retrun this function
        if height == -1:
            return 0

        # Calculate connected node on particular row
        tmp = [0, 0]

        for i in range(connectNum):
            if (step - i - 1) >= 0 and board[height][step - i - 1] == symbol:
                tmp[0] += 1
            else:
                tmp[0] = 0
            if (step + i - 1) <= 6 and board[height][step + i - 1] == symbol:
                tmp[1] += 1
            else:
                tmp[1] = 0

        if tmp[0] >= connectNum or tmp[1] >= connectNum:
            return 1
        
        return 0

    # Rule evaluate function
    # 내가 돌을 놓은 다음 상황에서,
    # 1) 내 돌이 3개 연속인 경우 * 3 의 Weight 를 준다
    # 2) 상대방의 돌이 2개 연속인 경우 * 3 의 Weight 를 준다. (상대방이 돌을 놓아 3개가 만들어질 경우에 대해 미리 방지)
    # 3) 내 돌이 2개 연속인 경우 * 1 의 Weight 를 준다.
    def evaluate(self, board, player):
        next_player = "X" if player == "O" else "O"

        value = board.check(board.get(), player, 3) * 3 + board.check(board.get(), player, 2) * 1
        value -= board.check(board.get(), next_player, 2) * 3
        
        return value

    # Returns a list with free rows
    def poss_steps(self, board):
        ret = []
        for i in range(len(board[1])):
            if board[0][i]==" ":
                ret.append(i)
        return map(lambda x:x+1, ret)
