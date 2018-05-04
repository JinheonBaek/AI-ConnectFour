import board as connect_four
import rule as connect_four_rule
import heuristic as connect_four_heuristic
# import nn

def main():
    print("--------------------------------------")
    print("-----     Connect Four           -----")
    # Init Board
    print("-----     Init Board             -----")
    board = connect_four.Board()

    # Init Rule, Heuristic, NN_heuristic
    print("-----     Load Rule              -----")
    rule = connect_four_rule.Rule()
    print("-----     Load Heuristic         -----")
    heuristic = connect_four_heuristic.Heuristic()
    print("-----     Load NN_Heuristic      -----")
    NN_heuristic = connect_four_heuristic.NN_Heuristic()
    
    print("-----     Load All, Play game!   -----")
    print("--------------------------------------")
    print("")

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
            # First move condition (do not put in middle col)
            if free_cells == 42:
                firstMove(board)
                users_turn = not users_turn
                continue

            # Computer turn
            mode = getMode()
            
            # Computer Run Mode (Rule / Heuristic / Neural Network)
            if mode == 1:
                # Rule base
                rule.make_move(board)
            elif mode == 2:
                # Heuristic base
                heuristic.make_ab_move(board)
            else:
                # Neural Network Heuristic base
                NN_heuristic.make_ab_move(board)

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
    print("--------------------------------------")
    print("---      Your turn                 ---")
    print("--------------------------------------")
    
    while True:
        try:
            col = input("What col would you like to move to (1-7):")
            col = int(col)
            break
        except ValueError:
            print("Only Numbers from (1-7)")

    valid_move = False
    while not valid_move:
        valid_move = board.insert(board.get(), col, "X", _print = True)

# Returns a winner (if there is one) for a given game.
def winner(board):
    if board.check(board.get(), "X", 4)>0:
        return "X"
    if board.check(board.get(), "O", 4)>0:
        return "O"
    return ""

# Make First Move (Assignment Condition: At first move, do not put in middle col)
def firstMove(board):
    print("First move")
    board.insert(board.get(), 3, "O", _print = True)

# Gets Compurse's play mode
def getMode():
    print("--------------------------------------")
    print("--- AI's turn                      ---")
    print("--- Mode 1 : Rule base             ---")
    print("--- Mode 2 : Heuristic Method      ---")
    print("--- Mode 3 : Neural Network Method ---")
    print("--------------------------------------")

    while True:
        try:
            mode = input("What mode would you like to select (1-3):")
            mode = int(mode)
            break
        except ValueError:
            print("Only Numbers from (1-3)")

    return mode

main()