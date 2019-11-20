
import pygame
import random

WIDTH = 600
HEIGHT = 600
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))


xpos = 300
ypos = 300

dx = 20
dy = 15


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Move ball
    xpos += dx
    ypos += dy

    # Change direction of ball
    if xpos <= 10 or xpos >= 590:
        dx *= -1
    if ypos <= 10 or ypos >= 590:
        dy *= -1
        
    pygame.draw.circle(screen, RED, (xpos,ypos), 10)
    pygame.display.update()

   
pygame.quit()
