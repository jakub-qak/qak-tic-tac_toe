import sys, pygame

pygame.init()

#dimensions
WIDTH = 300
HEIGHT = 300
SQUARES = WIDTH // 3
CIRCLE_RADIUS = SQUARES // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
LINE_WIDTH = 10
CROSS_CUTTING = SQUARES // 4.5
#colors
CYAN = (0, 255, 255)
LINE_COLOUR = (204, 93, 43)
BG_COLOUR = (255, 229, 180)
CIRCLE_COLOUR = (213, 173,	66)
CROSS_COLOUR = (205, 127, 50)

#Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BG_COLOUR)

#Board
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


#Lines
def draw_lines():
    pygame.draw.line(screen, LINE_COLOUR, (0,SQUARES), (WIDTH,SQUARES), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOUR, (0,2*SQUARES), (WIDTH,2*SQUARES), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOUR, (SQUARES,0),(SQUARES,HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOUR, (2*SQUARES,0),(2*SQUARES,HEIGHT), LINE_WIDTH)

draw_lines()

#Figures
def draw_figures(x=0, y=0, first_line_start = 0, first_line_end = 0, second_line_start = 0, second_line_end = 0):
    if player == 2:
        pygame.draw.circle(screen, CIRCLE_COLOUR, (x, y), CIRCLE_RADIUS, CIRCLE_WIDTH)
    elif player == 1:
        pygame.draw.line(screen, CROSS_COLOUR, first_line_start,first_line_end, CROSS_WIDTH)
        pygame.draw.line(screen, CROSS_COLOUR, second_line_start,second_line_end, CROSS_WIDTH)

#Checking if there are empty squares on the board 
def empty_space(x):
    return my_board[x] == " " 

#Checking if board is full 
def full_board():
    for x in my_board:
       if my_board[x] == " ":
           return False

    return True  

#Checking if someone win the game
def win(player):
    if my_board["1"] == my_board["2"] == my_board["3"] != ' ':
        if player == 1:
            colour = CROSS_COLOUR
        elif player == 2:
            colour = CIRCLE_COLOUR
        pygame.draw.line(screen, colour, (0,SQUARES*2.5),(SQUARES*3,SQUARES*2.5), 20)
        return True
    elif my_board["4"] == my_board["5"] == my_board["6"] != ' ':
        if player == 1:
            colour = CROSS_COLOUR
        elif player == 2:
            colour = CIRCLE_COLOUR
        pygame.draw.line(screen, colour, (0,SQUARES*1.5),(SQUARES*3,SQUARES*1.5), 20)
        return True
    elif my_board["7"] == my_board["8"] == my_board["9"] != ' ':
        if player == 1:
            colour = CROSS_COLOUR
        elif player == 2:
            colour = CIRCLE_COLOUR
        pygame.draw.line(screen, colour, (0,SQUARES*0.5),(SQUARES*3,SQUARES*0.5), 20)
        return True
    elif my_board["1"] == my_board["4"] == my_board["7"] != ' ':
        if player == 1:
            colour = CROSS_COLOUR
        elif player == 2:
            colour = CIRCLE_COLOUR
        pygame.draw.line(screen, colour, (SQUARES*0.5,0),(SQUARES*0.5,SQUARES*3), 20)
        return True
    elif my_board["2"] == my_board["5"] == my_board["8"] != ' ':
        if player == 1:
            colour = CROSS_COLOUR
        elif player == 2:
            colour = CIRCLE_COLOUR
        pygame.draw.line(screen, colour, (SQUARES*1.5,0),(SQUARES*1.5,SQUARES*3), 20)
        return True
    elif my_board["3"] == my_board["6"] == my_board["9"] != ' ':
        if player == 1:
            colour = CROSS_COLOUR
        elif player == 2:
            colour = CIRCLE_COLOUR
        pygame.draw.line(screen, colour, (SQUARES*2.5,0),(SQUARES*2.5,SQUARES*3), 20)
        return True
    elif my_board["7"] == my_board["5"] == my_board["3"] != ' ':
        if player == 1:
            colour = CROSS_COLOUR
        elif player == 2:
            colour = CIRCLE_COLOUR
        pygame.draw.line(screen, colour, (0,0),(SQUARES*3,SQUARES*3), 20)
        return True        
    elif my_board["9"] == my_board["5"] == my_board["1"] != ' ':
        if player == 1:
            colour = CROSS_COLOUR
        elif player == 2:
            colour = CIRCLE_COLOUR
        pygame.draw.line(screen, colour, (0,SQUARES*3),(SQUARES*3,0), 20)
        return True

    return False    

# Restarting game
def restart():
    screen.fill(BG_COLOUR)
    draw_lines()


pygame.display.set_caption("qak_tic_tac_toe") #window title

player = 1
game_over = False

# mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over: 
            
            #mouse clicking
            mouseX = event.pos[0] #x
            mouseY = event.pos[1] #y

            clicked_col = int(mouseX // SQUARES) #x
            clicked_row = int(mouseY // SQUARES) #y

            #coordinates of "O"
            circle_x = clicked_col * SQUARES + SQUARES // 2
            circle_y = clicked_row * SQUARES + SQUARES // 2

            #coordinates of "X"
            #first line
            cross_first_line_start = (clicked_col*SQUARES + CROSS_CUTTING ,clicked_row*SQUARES+SQUARES - CROSS_CUTTING)
            cross_first_line_end =  (clicked_col*SQUARES+SQUARES - CROSS_CUTTING, clicked_row*SQUARES + CROSS_CUTTING)
            #second Line
            cross_second_line_start = (clicked_col*SQUARES + CROSS_CUTTING,clicked_row*SQUARES + CROSS_CUTTING)
            cross_second_line_end =  (clicked_col*SQUARES+SQUARES - CROSS_CUTTING, clicked_row*SQUARES+SQUARES - CROSS_CUTTING)


            # moves on board = moves on console
            move = [clicked_col, clicked_row]
            
            if move == [0,0]:
                move = "7"
            elif move == [1,0]:
                move = "8"
            elif move == [2,0]:
                move = "9"
            elif move == [0,1]:
                move = "4"
            elif move == [1,1]:
                move = "5"
            elif move == [2,1]:
                move = "6"
            elif move == [0,2]:
                move = "1"
            elif move == [1,2]:
                move = "2"
            elif move == [2,2]:
                move = "3"    
            
            # Changing player
            if empty_space(move):
                if player == 1:
                    my_board[move] = "0"
                    player = 2
                    if win(player):
                        game_over = True
                elif player == 2:
                    my_board[move] = "X"
                    player = 1
                    if win(player):
                        game_over = True
                draw_figures(circle_x, circle_y, cross_first_line_start, cross_first_line_end, cross_second_line_start, cross_second_line_end)

                        

            print(move)
            print_board(my_board)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                player = 1
                my_board = {'7':' ','8':' ','9':' ',
         '4':' ','5':' ','6':' ',
         '1':' ','2':' ','3':' ',}
                #Restart game even if someone win
                game_over = False
            
            
    pygame.display.update()
