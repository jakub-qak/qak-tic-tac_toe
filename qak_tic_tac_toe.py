my_board = {'7':' ','8':' ','9':' ',
         '4':' ','5':' ','6':' ',
         '1':' ','2':' ','3':' ',}

def print_board(board):
    print(f"{board['7']}|{board['8']}|{board['9']}")
    print("-+-+-")
    print(f"{board['4']}|{board['5']}|{board['6']}")
    print("-+-+-")
    print(f"{board['1']}|{board['2']}|{board['3']}")

# print_board(my_board)

print("Choose O or X and number from 1 to 9: \n7|8|9\n-+-+-\n4|5|6\n-+-+-\n1|2|3\nSTART!")

def game():

    for key in my_board:
        my_board[key] = ' ' 
    
    #move 1
    X_or_O_P1 = input("Player 1 (O/X)?")
    allowed = ["x", "X", "o", "o"]
    #Player has to choose X or Y
    while X_or_O_P1 not in allowed:
        print("Wrong! Choose O or X")
        X_or_O_P1 = input("Player 1 (O/X)?")
    #-----
    X_or_O_P1 = X_or_O_P1.upper()
    num_list = [str(x) for x in range(1,10)] 
    where = str(input("Where (1-9)?"))
    #Player has to choose number from 1-9
    while where not in num_list:
        print("Wrong! Choose number from 1 to 9")
        where =str(input("Where (1-9)?"))
    #-----
    my_board[where] = X_or_O_P1
    print_board(my_board)

    #move 2
    if X_or_O_P1 == "O":
        X_or_O_P2 = "X"
        print("Player 2 you have X")
    else:
        X_or_O_P2 = "O"
        print("Player 2 you have O")
    turn = X_or_O_P2
    where =str(input("Where (1-9)?"))
    while where not in num_list:
        print("Wrong! Choose number from 1 to 9")
        where =str(input("Where (1-9)?"))
    if my_board[where] != ' ' :
        where =str(input("You have to choose another number!"))
        #If someone is still choosing the same number as another player
        while my_board[where] != ' ':
            where =str(input("You have to choose another number (1-9)?"))
        my_board[where] = turn
        #-----
    else:
        my_board[where] = turn 
    print_board(my_board)



    #rest of moves
    i = 1
    while i < 8:
        # Changing players
        if turn == X_or_O_P2:
            turn = X_or_O_P1
        else:
            turn = X_or_O_P2
        #-----
        where =str(input("Where (1-9)?"))
        while where not in num_list:
            print("Wrong! Choose number from 1 to 9")
            where =str(input("Where (1-9)?"))
        if my_board[where] != ' ' :
            where =str(input("You have to choose another number!"))
            #If someone is still choosing the same number as another player
            while my_board[where] != ' ':
                where =str(input("You have to choose another number (1-9)?"))
            my_board[where] = turn 
            #------------
        else:
            my_board[where] = turn
            

        #WIN
        if my_board["1"] == my_board["2"] == my_board["3"] != ' ':
            print_board(my_board)
            print(f"\n{turn} WON!")
            break 
        elif my_board["4"] == my_board["5"] == my_board["6"] != ' ':
            print_board(my_board)
            print(f"\n{turn} WON!")
            break
        elif my_board["7"] == my_board["8"] == my_board["9"] != ' ':
            print_board(my_board)
            print(f"\n{turn} WON!")
            break
        elif my_board["1"] == my_board["4"] == my_board["7"] != ' ':
            print_board(my_board)
            print(f"\n{turn} WON!")
            break
        elif my_board["2"] == my_board["5"] == my_board["8"] != ' ':
            print_board(my_board)
            print(f"\n{turn} WON!")
            break
        elif my_board["3"] == my_board["6"] == my_board["9"] != ' ':
            print_board(my_board)
            print(f"\n{turn} WON!")
            break
        elif my_board["7"] == my_board["5"] == my_board["3"] != ' ':
            print_board(my_board)
            print(f"\n{turn} WON!")
            break        
        elif my_board["9"] == my_board["5"] == my_board["1"] != ' ':
            print_board(my_board)
            print(f"\n{turn} WON!")
            break
        else:
            print_board(my_board)
            i += 1    
            if i == 8:
                print("\nGAME OVER! IT'S TIE!")
    answer = input("Do you want to play again (y/n)?")
    while answer != "n":
        if answer == "n":
            break
        else:
            game()

    return print("Ok, goodbye!")

game()