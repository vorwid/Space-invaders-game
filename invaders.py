import random
import math
import pygame

pygame.init()


wid = 600
hi = 600

screen = pygame.display.set_mode((wid, hi))

def wri(text, x, y, size):
    f = pygame.font.SysFont("Arial", size)
    rend = f.render(text, 1, (255,100, 100))
    x = (wid - rend.get_rect().width) /2
    y = (hi - rend.get_rect().height) /2
    screen.blit(rend, (x, y))

wri("Press space to start", 80, 150, 40)


oponents = []




class invaders():
    def __init__(self):
        self.x = random.randint(250, 500)
        self.y = random.randint(250,500)
        self.vx = random.

    def coll(self, player):
    

for i in range(20):
    oponents.append(invaders())

dy = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dy= -1
            if event.key == pygame.K_DOWN:
                dy = 1
            if event.key == pygame.K_LEFT:
                dy = -1
            if event.key == pygame.K_RIGHT:
                dy = 1
            



pygame.display.update()
