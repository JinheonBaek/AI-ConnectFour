import pandas as pd

class Board:
    def __init__(self):
        self.board = [ [ " ", " ", " ", " ", " ", " "," "], [ " ", " ", " ", " "," ", " ", " "], [ " ", " ", " ", " ", " ", " ", " "], [ " ", " ", " ", " ", " ", " ", " "], [ " ", " ", " ", " ", " ", " ", " "], [ " ", " ", " ", " ", " ", " ", " "] ]

    # Gets board date in list type
    def get(self):
        return self.board

    # Gets board data in PD type (for ML)
    def getData(self):
        data = []
        
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                data.append(self.board[i][j])

        data = pd.DataFrame(data = data).T

        data[data == "X"] = 1
        data[data == " "] = 0
        data[data == "O"] = -1

        width = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        height = range(1, 7)
        cols = []

        for i in width:
            for j in height:
                cols.append(i + str(j))
        data.columns = cols

        return data

    # Displays the game
    def display(self):
        print ("   1   2   3   4    5   6   7")
        print ("6: " + self.board[0][0] + " | " + self.board[0][1] + " | " + self.board[0][2] + " | " + self.board[0][3] + " | " + self.board[0][4] + " | " + self.board[0][5] + " | " + self.board[0][6] + " | ")
        print ("  ---+---+---+---+---+---+---")
        print ("5: " + self.board[1][0] + " | " + self.board[1][1] + " | " + self.board[1][2] + " | " + self.board[1][3] + " | " + self.board[1][4] + " | " + self.board[1][5] + " | " + self.board[1][6] + " | ")
        print ("  ---+---+---+---+---+---+---+")
        print ("4: " + self.board[2][0] + " | " + self.board[2][1] + " | " + self.board[2][2] + " | " + self.board[2][3] + " | " + self.board[2][4] + " | " + self.board[2][5] + " | " + self.board[2][6] + " | ")
        print ("  ---+---+---+---+---+---+---+")
        print ("3: " + self.board[3][0] + " | " + self.board[3][1] + " | " + self.board[3][2] + " | " + self.board[3][3] + " | " + self.board[3][4] + " | " + self.board[3][5] + " | " + self.board[3][6] + " | ")
        print ("  ---+---+---+---+---+---+---+")
        print ("2: " + self.board[4][0] + " | " + self.board[4][1] + " | " + self.board[4][2] + " | " + self.board[4][3] + " | " + self.board[4][4] + " | " + self.board[4][5] + " | " + self.board[4][6] + " | ")
        print ("  ---+---+---+---+---+---+---+")
        print ("1: " + self.board[5][0] + " | " + self.board[5][1] + " | " + self.board[5][2] + " | " + self.board[5][3] + " | " + self.board[5][4] + " | " + self.board[5][5] + " | " + self.board[5][6] + " | ")
        print ("")

    # Checks for connected node
    ## board : Board Info
    ## symbol : O or X to check who is winner
    ## connectNum : check existence of connected node's number on particular symbol
    def check(self, board, symbol, connectNum):
        width = len(board[0])
        height = len(board)
        ret = 0
        
        for i in range(height):
            tmp = 0
            for j in range(width):
                if board[i][j] == symbol:
                    tmp = tmp + 1
                else:
                    tmp = 0
                if tmp >= connectNum:
                    ret = ret + 1

        for i in range(width):
            tmp = 0
            for j in range(height):
                if board[j][i] == symbol:
                    tmp = tmp + 1
                else:
                    tmp = 0
                if tmp >= connectNum:
                    ret = ret + 1

        sub = connectNum - 1

        for i in range(height-1, sub-1, -1):
            for j in range(0, width-sub, 1):
                tmp = 0
                for t in range(connectNum):
                    if(board[i-t][j+t] == symbol): tmp = tmp + 1
                if tmp == connectNum: ret = ret + 1

        for i in range(height-1, sub-1, -1):
            for j in range(width-1, sub-1, -1):
                tmp = 0
                for t in range(connectNum):
                    if(board[i-t][j-t] == symbol): tmp = tmp + 1
                if tmp == connectNum: ret = ret + 1

        return ret

    # Do a move
    def insert(self, board, col, symbol, _print = False):
        valid_move = False
        
        if(1 <= col <= 7):
            while not valid_move:
                for row in range (6, 0, -1):
                    if (1 <= row <= 6) and (board[row-1][col-1] == " "):
                        board[row-1][col-1] = symbol
                        if (_print == True): print("Put stone on (", 7 - row, ",", col, ")")
                        return True
                return False
        else:
            print ("Sorry, invalid input. Please try again!\n")
        return False

    # Undo a move
    def uninsert(self, board, col, symbol):
        for row in [1,2,3,4,5,6]:
            if (board[row-1][col-1] == symbol):
                board[row-1][col-1] = " "
                break

    # Returns a list with free rows
    def poss_steps(self, board):
        ret = []
        for i in range(len(board[1])):
            if board[0][i]==" ":
                ret.append(i)
        return map(lambda x:x+1, ret)
