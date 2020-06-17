import random
from snake import snake
from food import food
import pygame


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Snake")

snake = snake(screen)
food = food(screen)
food.spawn()

RUNNING = True
clock = pygame.time.Clock()
while RUNNING:
    clock.tick(15)


    screen.fill((255, 150, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            RUNNING = False
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_UP or event.key == pygame.K_w):
            snake.direction(0, -1)
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_DOWN or event.key == pygame.K_s):
            snake.direction(0, 1)
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
            snake.direction(1, 0)
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_LEFT or event.key == pygame.K_a):
            snake.direction(-1, 0)

    food.show()

    snake.update()
    snake.show()

    if snake.eat(food):
        food.spawn()

    if snake.crashed():
        print("You died")
        RUNNING = False

    pygame.display.update()
