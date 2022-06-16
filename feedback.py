import random

play = ['1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c']
keep_playing = 'y'


#Global variables
a = ['      ' for i in range(9)]
b = [i for i in range(9)]
played_moves = []


def img(a):
    image = f'''
                     a      b       c
                       |        |  
           1     {a[0]}| {a[1]} | {a[2]}  
                  _____|________|_____
                       |        |     
           2     {a[3]}| {a[4]} | {a[5]}  
                  _____|________|_____
                       |        |     
           3     {a[6]}| {a[7]} | {a[8]}  
                       |        |
                 '''
    return image


def win (a):
    if a[0] == a[1] == a[2] != "      " or a[3] == a[4] == a[5] != "      " or a[6] == a[7] == a[8] != "      ":
        winner = True
    elif a[0] == a[3] == a[6] != "      " or a[1] == a[4] == a[7] != "      " or a[8] == a[5] == a[2] != "      ":
        winner = True
    elif a[0] == a[4] == a[8] != "      " or a[6] == a[4] == a[2] != "      ":
        winner = True
    else:
        winner = False
    return winner


def continue_game():
    keep_game = input("Would you like to play again?: Y/N ").lower()
    if keep_game == 'y':
        global a
        global b
        global played_moves
        a = ['      ' for i in range(9)]
        b = [i for i in range(9)]
        played_moves = []
        print(img(a))
    return keep_game


print("Welcome to our great and delightful Tic Tac Game!")
print(img(a))

while keep_playing == 'y':
    user_move = input("Please type your move: (1a, 2c, etc). To exit type 'exit': \n").lower()
    if user_move == 'exit':
        keep_playing = 'n'
    else:
        if user_move in played_moves:
            print(f"Position {user_move} has already been used.  Please try a different move.")
        else:
            if user_move in play:
                played_moves.append(user_move)
                index = play.index(user_move)
                a[index] = "  X   "
                b.remove(index)
                board = img(a)
                print(f"Your move: \n{board}")
                is_winner = win(a)
                if is_winner:
                    print("Congratulations! You have won!")
                    keep_playing = continue_game()
                else:
                    if b == []:
                        print("There are no further moves available. It is a tight.")
                        keep_playing = continue_game()
                    else:
                        computer_move = random.choice(b)
                        played_moves.append(play[computer_move])
                        a[computer_move] = "  O   "
                        b.remove(computer_move)
                        board = img(a)
                        print(f"Computer move: \n{board}")
                        is_winner = win(a)
                        if is_winner:
                            print("We are sorry! The computer has won!")
                            keep_playing = continue_game()
                        else:
                            if b == []:
                                print("There are no further moves available. It is a tight.")
                                keep_playing = continue_game()
            else:
                print(f"Move {user_move} is not allowed, please try again")
print("Thank you for trying our great Tic Tac game! We hope you enjoyed it!")