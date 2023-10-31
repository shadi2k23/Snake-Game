import pygame
import time
import random

# Initialize the pygame
pygame.init()

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
yellow = (255, 255, 102)

# Set display width and height
dis_width = 800
dis_height = 600

# Define block size and speed
snake_block = 10
snake_speed = 15

# Create a display screen
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)

def draw_snake(snake_block, snake_list):
    for i, block in enumerate(snake_list):
        if i == 0:
            pygame.draw.rect(dis, black, [block[0], block[1], snake_block, snake_block])
        else:
            pygame.draw.rect(dis, green, [block[0], block[1], snake_block, snake_block])

def your_score(score):
    value = font_style.render("Your Score: " + str(score), True, black)
    dis.blit(value, [0, 0])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def game_loop():
    game_over = False
    game_close = False
    score = 0

    # Initial position of the snake
    x_snake = dis_width / 2
    y_snake = dis_height / 2

    x_change = 0
    y_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or Space-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_SPACE:
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
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        if x_snake >= dis_width or x_snake < 0 or y_snake >= dis_height or y_snake < 0:
            game_close = True

        x_snake += x_change
        y_snake += y_change
        dis.fill(white)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x_snake)
        snake_head.append(y_snake)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        your_score(score)
        pygame.display.update()

        if x_snake == foodx and y_snake == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
            score += 5

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
