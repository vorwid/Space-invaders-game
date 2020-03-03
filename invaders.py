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



class invaders():
    def __init__(self):
        self.x = random.randint(250, 500)
        self.y = random.randint(250,500)
        self.vx = random.randint(-4, 4)
        self.vy = random.randint(-4, 4)
        self.grafika = pygame.image.load(os.path.join(""))
        self.wiel =  20
    def drawing(self):
        screen.blit(self.grafika(self.x, self.y))
    def  mov(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        if self.x <= 0 or self.x >= wid - self.wiel:
            self.vx = self.vx * -1
        if self.y <= 0 or self.y >= hi - self.wiel:
            self.vy = self.vy * -1
    def coll(self, player):
        x_center = self.x + self.wiel/2
        y_center = self.y + self.wiel/2
        if player.collidepoint(x_center, y_center):
            czcionka = pygame.font.SysFont("Georgia", 20)
            napis = czcionka. render("KONIEC GRY", 1, (123, 213, 231))
            screen.blit(napis, (100, 130))
            global gramy
            gramy = False
            
x_player = 300
y_player = 300
v = 20


    
oponents = []

for i in range(10):
    oponents.append(invaders())

dy = 0

gramy = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if gramy == True:
            screen.fill((50, 50, 100,))
            for o in oponents:
                o.drawing()
                o.mov()
            pygame.display.update()
            pygame.time.wait(10)
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
