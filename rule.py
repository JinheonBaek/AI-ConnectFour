class Rule:
    def make_move(self, board, sym = "O"):
        col = self.evaluate(board, sym)
        board.insert(board.get(), col, sym)

    def evaluate(self, board, player1 = "O"):
        player2 = "X" if player1 == "O" else "O"
        return 3