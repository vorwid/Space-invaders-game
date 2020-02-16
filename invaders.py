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
    y = (hi - rend.get_rect().high) /2
    screen.blit(rend, (x, y))

wri("Press space to start", 40)
