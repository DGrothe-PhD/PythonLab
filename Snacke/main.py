#Snake Game Python
# install pygame library 
# pip install pygame
import pygame
import random
import time 
#init pygame
pygame.init()

#Define Colors
white = (255,255,255)
yellow = (255,255,102)
black = (0,0,0)
red = (213,50,80)
green = (0,255,0)
blue = (50,153,213)

#game window
width = 600
height = 400

game_display = pygame.display.set_mode((width,height))
pygame.display.set_caption('Snake Game')

#Snake settings
snake_block = 10
snake_speed = 10

font_style = pygame.font.SysFont("bahnschrift",25)
score_font = pygame.font.SysFont("comicsansms",34)

#Clock
clock = pygame.time.Clock()

#define display_message
def display_message(msg,color):
    message = font_style.render(msg, True,color)
    game_display.blit(message,[width/6,height/6])

#define display_score
def display_score(score):
    value = font_style.render(f"Score: {score}",True,yellow)
    game_display.blit(value,[0,0])

#def draw_snake
def draw_snake(snake_block,snake_list):
    for block in snake_list:
        pygame.draw.rect(game_display,green,[block[0],block[1],snake_block,snake_block])

#main Game loop
def game_loop():
    game_over = False
    game_close = False
    #snake-position
    x = width/2
    y = height/2
    #snake body
    snake_list =[]
    snake_lenght = 1
    #Snake movement
    x_change = 0
    y_change = 0

    #Food position
    food_x = round(random.randrange(0,width-snake_block)/10.0)*10.0
    food_y = round(random.randrange(0,height - snake_block)/10.0)*10.0

    while not game_over:
        while game_close:
            game_display.fill(blue)
            display_message("You lost! press Q-Quit or C-play Again",red)
            display_score(snake_lenght-1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:#Quit
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:#Play Again
                        game_loop()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x_change = 0 
                    y_change = snake_block

        #check for boundaries
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True
        x += x_change
        y += y_change

        # fill the Background
        game_display.fill(black)

        # Draw food 
        pygame.draw.rect(game_display, yellow, [food_x,food_y, snake_block, snake_block])

        # Update snake's head
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_lenght:
            del snake_list[0]
        
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True
        
        draw_snake(snake_block,snake_list)
        
        display_score(snake_lenght - 1)
        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0,width - snake_block)/10.0)*10.
            food_y = round(random.randrange(0,height - snake_block)/10.0)*10.
            snake_lenght += 1
        
        #snake speed
        clock.tick(snake_speed)
    pygame.quit()
    quit()




game_loop()
