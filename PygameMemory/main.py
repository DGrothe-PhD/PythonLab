#Memory game using pygame
#install pygame pip install pygame
import pygame
import random
import time 
from pygame.locals import *
#init pygame
pygame.init()
#Constants 
WIDTH, HEIGHT = 800,600
CARD_SIZE = 100
GRID_SIZE = 4
MARGIN = 20
RADUIS = 15
#Colors
BG_COLOR = (30,30,30)
CARD_BACK_COLOR = (50,50,200)
CARD_FRONT_COLOR = (100,100,100)
TEXT_COLOR = (255,255,255)
WIN_COLOR = (0,255,0)
#Display
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Memory Game")
#Font
font = pygame.font.Font(None,80)
win_font = pygame.font.Font(None,70)
#Function to draw rounded box 
def draw_rounded_rect(surface,color,rect,corner_raduis):
    pygame.draw.rect(surface,color,rect,border_radius=corner_raduis)
#initialize the game
def initialize_game():
    #Cards values and board setup 
    cards = list(range(1, (GRID_SIZE * GRID_SIZE // 2)+ 1))*2
    random.shuffle(cards)
    board = [cards[i:i + GRID_SIZE] for i in range(0 , len(cards),GRID_SIZE)]
    #cards state False means face down, True means face up
    revealed = [[False] * GRID_SIZE for _ in range(GRID_SIZE)]
    matched = [[False] * GRID_SIZE for _ in range(GRID_SIZE)]
    return board,revealed,matched
#Grid total winth and height
grid_width = GRID_SIZE * CARD_SIZE + (GRID_SIZE -1) *MARGIN
grid_height = GRID_SIZE * CARD_SIZE + (GRID_SIZE -1) *MARGIN
#calc the top- left corder of the grid to center it
grid_x = (WIDTH - grid_width) // 2
grid_y = (HEIGHT - grid_height) // 2

#Game Loop
running = True
board , revealed, matched = initialize_game()
first_card = None
second_card = None

def handle_end_game():
    #waiting for C to play again and Q to quit
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    return 'continue'
                elif event.key == pygame.K_q:
                    return 'quit'

while running:
    #print("Welcome")
    #Event handling 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
            #Get mouse position
            x, y = pygame.mouse.get_pos()
            print(f"x:{x},y{y}")
            x -= grid_x
            y -= grid_y
            if 0 <= x <=grid_width and 0 <= y<= grid_height:
                col = x // (CARD_SIZE + MARGIN)
                row = y // (CARD_SIZE + MARGIN)
                if row < GRID_SIZE and col < GRID_SIZE and not revealed[row][col]:
                    if first_card is None:
                        first_card = (row,col)
                        revealed[row][col] = True
                    elif second_card is None and (row,col) != first_card:
                        second_card = (row,col)
                        revealed[row][col] = True
    #check for matches
    if first_card and second_card:
        r1,c1 = first_card
        r2,c2 = second_card
        print(f"card1:{board[r1][c1]}, card2:{board[r2][c2]}")
        if board[r1][c1] == board[r2][c2]:
            matched[r1][c1] = matched[r2][c2] = True
        else:
            pygame.display.flip()
            time.sleep(0.5)
            revealed[r1][c1] = revealed[r2][c2] = False
        first_card = second_card = None
    #draw cards
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x = grid_x + col * (CARD_SIZE + MARGIN)
            y = grid_y + row * (CARD_SIZE + MARGIN)

            rect = pygame.Rect(x,y,CARD_SIZE,CARD_SIZE)
            if revealed[row][col] or matched[row][col]:
                #Show the card's value
                draw_rounded_rect(screen,CARD_FRONT_COLOR,rect,RADUIS)
                text = font.render(str(board[row][col]),True,TEXT_COLOR)
                screen.blit(text,(x + CARD_SIZE // 3, y + CARD_SIZE // 4))
            else:
                #show the card back 
                draw_rounded_rect(screen,CARD_BACK_COLOR,rect,RADUIS)
    #check if the game is won
    if all(all(row) for row in matched):
        text = win_font.render("You win!",True,WIN_COLOR)
        screen.blit(text,(WIDTH // 2 -150, HEIGHT // 2 - 50))
        pygame.display.flip()
        #waiting for C to play again or Q to Quit
        action = handle_end_game()
        if action == 'continue':
            #rest 
            board,revealed,matched = initialize_game()
            first_card = second_card = None
        elif action == 'quit':
            running = False
            
    pygame.display.flip()           

pygame.quit()