# Tick-Tac-Toe game in command line
import numpy


board = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]


print("Welcome to Tic Tac Toe terminal game. \n"
      "Enjoy with your friends! \n\n")
choice = input("Wanna play against the computer? y or n: ").lower()


def board_to_array(board):
    for list in board:
        print('  |  '.join(list))
        print("------------")


player_one = input("Player 1: X or O: ").upper()
player_two = None

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
            print("Player 2 wins")
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

    board_array = numpy.array(board)
    # Diagonal
    diagonal_list = board_array.diagonal().tolist()
    diagonal_list_reversed = numpy.flipud(board_array).diagonal().tolist()

    #corners
    random_corner = [board[0][0], board[0][2], board[2][0], board[2][2], board[1][1]]


    # Checking if player one is gonna win next move
    for row in board:
        if row.count("O") == 2:
            for pos in row:
                if pos == "":
                    row[row.index(pos)] = player_two
                    return

    for index in range(3):
        list = board_array[0:3, index].tolist()
        if list.count("O") == 2:
            for pos in list:
                if pos == "":
                    board[list.index(pos)][index] = player_two
                    return

    # Diagonal L-R
    if diagonal_list_reversed.count("O") == 2:
        for pos in diagonal_list:
            if pos == "":
                board[diagonal_list_reversed.index(pos)][diagonal_list_reversed.index(pos)] = "O"
                return

    # Diagonal R-L
    if diagonal_list.count("O") == 2 or diagonal_list.count("X") == 2:
        for pos in diagonal_list:
            if pos == "":
                board[diagonal_list.index(pos)][diagonal_list.index(pos)] = player_two
                return

    # Row
    for row in board:
        if row.count("X") == 2:
            for pos in row:
                if pos == "":
                    row[row.index(pos)] = player_two
                    return


    # Column
    for index in range(3):
        list = board_array[0:3, index].tolist()
        if list.count("X") == 2:
            for pos in list:
                if pos == "":
                    board[list.index(pos)][index] = player_two
                    return

    # Diagonal L-R
    if diagonal_list_reversed.count("X") == 2:
        for pos in diagonal_list:
            if pos == "":
                board[diagonal_list_reversed.index(pos)][diagonal_list_reversed.index(pos)] = player_two
                return


    # Diagonal R-L
    if diagonal_list.count("X") == 2:
        for pos in diagonal_list:
            if pos == "":
                board[diagonal_list.index(pos)][diagonal_list.index(pos)] = player_two
                return

    # check for available corners
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "":
                board[i][j] = player_two
                return



game_end = 1


while True:

    game_end += 1
    row = input("Player 1 what row: ")
    column = input("Select what column: ")
    board[int(column) - 1][int(row) - 1] = player_one
    if choice == 'y':
        computer_ai(board)
    elif choice == 'n':
        board_to_array(board)
        validator(board)
        row = input("Player 2 what row: ")
        column = input("Select what column: ")
        board[int(column) - 1][int(row) - 1] = player_two



    board_to_array(board)
    validator(board)
    # The draw validator
    if game_end == 6:
        print("It's a draw")
        break






