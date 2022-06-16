# Tick-Tac-Toe game in command line

board = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]


def board_to_array(board):
    for list in board:
        print('  |  '.join(list))
        print("------------")

print("Welcome to Tic Tac Toe terminal game. \n"
      "Enjoy with your friends! \n\n")

player_one = input("Player 1: X or O: ").upper()

if player_one == "X":
        player_two = "O"
        print("Player 1: X")
        print("Player 2: O")

elif player_one == "O":
        print("player 1: O")
        player_two = "X"
        print("Player 2: X")

else:
        print("You entered the wrong letter, please restart the program!")



def validator(board):

    for i in range(len(board)):

    # Row validator
        if board[i].count("X") == 3:
            print("Player 1 wins")
            exit()
        elif board[i].count("O") == 3:
            print("Player 2 wins on row")
            exit()


    # Column validator
        if board[0][i] == "X" and board[1][i] == "X" and board[2][i] == "X":
            print("Player 1 wins")
            exit()
        elif board[0][i] == "O" and board[1][i] == "O" and board[2][i] == "O":
            print("Player 2 wins")
            exit()


    # Diagonal R-L validator
    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        print("Player 1 wins!")
        exit()
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        print("Player 2 wins!")
        exit()



    # Diagonal L-R validator
    if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        print("Player 1 wins!")
        exit()
    elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        print("Player 2 wins!")
        exit()


def computer_ai(board):

    #corners
    top_left_corner = board[0][0]
    top_right_corner = board[0][2]
    bottom_left_corner = board[2][0]
    bottom_right_corner = board[2][2]

    # check for available corners
    if first_move == 0:
        if top_left_corner == "":
            board[0][0] = "O"
        elif top_right_corner == "":
            board[0][2] = "O"
        elif bottom_left_corner == "":
            board[2][0] = "O"
        elif bottom_right_corner == "":
            board[2][2] = "O"
    first_move = 1

    # Checking if player one is gonna win next move

    # Row
    for i in board:
        for j in i:
            if i.count("X") == 2:
                if board[i][j] == "":
                    board[i][j] = "O"

    # Column
    for i in range(len(board)):
        if board[0][i] and board[1][i] == "X" or board[1][i] and board[2][i] == "X":
            if board[0][i] == "":
                board[0][i] = "O"
            elif board[2][i] == "":
                board[2][i] = "O"





game_end = 1


while True:
    game_end += 1
    row = input("Player 1 what row: ")
    column = input("Select what column: ")
    board[int(column) - 1][int(row) - 1] = player_one

    computer_ai(board)
    board_to_array(board)
    # validator(board)
    # The draw validator
    # if game_end == 6:
    #     print("It's a draw")
    #     break
    # row = input("Player 2 what row: ")
    # column = input("Select what column: ")
    # board[int(column) - 1][int(row) - 1] = player_two
    # board_to_array(board)
    # validator(board)





