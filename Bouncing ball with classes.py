# Simply pong game using python 3 and pygame
# Minimal without start and game over screen


import pygame
import random
vec = pygame.math.Vector2

TITLE = 'Simple Pong with Python 3 and Pygame'
WIDTH = 600
HEIGHT = 600
FPS = 120
FONT_NAME = 'arial'

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        
        ball_image = pygame.Surface((20, 20)) # radius x2
        pygame.draw.circle(ball_image, WHITE, (10,10), 10) # surface, color, (x,y), radius
        
        self.image = ball_image
        self.rect = self.image.get_rect() 
        
        # Position and velocity vector (x,y)
        self.pos = vec(400,300)
        self.vel = vec(24,19)
        
    def update(self):
        self.pos += self.vel
        
        if self.pos.x <= 10 or self.pos.x >=590:
            self.vel.x *= -1
            
        if self.pos.y <= 10 or self.pos.y >= 590:
            self.vel.y *= -1
            
        self.rect.center = self.pos
    


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bouncing Ball')
        
clock = pygame.time.Clock()
running = True


    
all_sprites = pygame.sprite.Group()
ball = Ball()
all_sprites.add(ball)
      


while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()
    screen.fill(BLACK)
    all_sprites.draw(screen)
        
    pygame.display.flip()
   


pygame.quit()



