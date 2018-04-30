import board as connect_four
import rule 
import heuristic as connect_four_heuristic
import nn

def main():
    # Init Board
    board = connect_four.Board()

    # Init Heuristic
    heuristic = connect_four_heuristic.Heuristic()

    # Init Values
    free_cells = 42
    users_turn = True

    # Set first Movement
    choice = input("Would you like to go first? (y or n): ")

    if (choice == 'y' or choice=='Y'):
        users_turn = True
    elif (choice == 'n' or choice =='N') :
        users_turn = False        
    else:
        print ('invalid input')

    # Play game
    while not winner(board) and (free_cells > 0):
        
        # Display board
        board.display()
        
        # User turn or Computer turn
        if users_turn:
            # User turn
            make_user_move(board)

            # Change turn
            users_turn = not users_turn
        else:
            # Computer turn
            mode = getMode()
            
            # Computer Run Mode (Rule / Heuristic / Neural Network)
            if mode == 1:
                # Rule base
                break
            elif mode == 2:
                # Heuristic base
                heuristic.make_ab_move(board)
            else:
                # Neural Network base
                break

            # Change turn
            users_turn = not users_turn

        free_cells -= 1

    # Game end
    board.display()

    if (winner(board) == 'X'):
        print ("You Won!")
    elif (winner(board) == 'O'):
        print ("The Computer Won!")
        print ("\nGAME OVER")
    else:
        print ("Draw!")
        print ("\nGAME OVER \n")

# Gets user input and makes a move.
def make_user_move(board):
    while True:
        try:
            col = input("What col would you like to move to (1-7):")
            col = int(col)
            break
        except ValueError:
            print("Only Numbers from (1-7)")

    valid_move = False
    while not valid_move:
        valid_move = board.insert(board.get(), col, "X")

# Returns a winner (if there is one) for a given game.
def winner(board):
    if board.check(board.get(), "X", 4)>0:
        return "X"
    if board.check(board.get(), "O", 4)>0:
        return "O"
    return ""

# Gets Compurse's play mode
def getMode():
    print("Mode 1 : Rule base")
    print("Mode 2 : Heuristic Method")
    print("Mode 3 : Neural Network Method")

    while True:
        try:
            mode = input("What mode would you like to select (1-3):")
            mode = int(mode)
            break
        except ValueError:
            print("Only Numbers from (1-3)")

    return mode

main()