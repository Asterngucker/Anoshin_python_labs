import pygame
import numpy as np
from pygame.draw import *
from random import randint
pygame.init()

FPS = 0.5
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
WHITE = (255, 255, 255)
class new_ball():
    def __init__(self):
        self.x = randint(50,1150)
        self.y = randint(50,750)
        self.r = randint(20,60)
        self.color = COLORS[randint(0, 5)]
    def new(self):
        circle(screen, self.color, (self.x, self.y), self.r)
        return (self.x, self.y, self.r)
    def coordinates(self):
        return ((self.x, self.y), self.r)

def distance(c1, c2):
    l = np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)
    return l
n = 0
pygame.display.update()
clock = pygame.time.Clock()
finished = False
##ball = new_ball()
mass = ((0, 0), 0)

font = pygame.font.Font('TlwgTypo.ttf', 40)
click_coor = (-100, -100)
text = []

while not finished:
    for event in pygame.event.get():
        pygame.draw.rect(screen, WHITE, (375, 350, 450, 80), 10, 5)
        text1 = ''
        for i in range(len(text)):
            text1 = text1 + text[i]
        name = font.render(text1, True, GREEN)
        screen.blit(name, (390, 370))
        screen.blit(font.render('Enter your name:', True, WHITE), (390, 300))
        pygame.display.update()
        if event.type == pygame.QUIT:
                    finished = True
                    pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                    print(text)
                    finished = True
            elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
            else:
                if len(text) < 14:
                    text += event.unicode
        screen.fill(BLACK)

finished = False
while not finished:
    print("\n")
    clock.tick(FPS)
    number = font.render('n = ' + str(n), True, GREEN)
    screen.blit(number, (30, 830))
    ball = new_ball()
    ball.new()
    pygame.display.update()
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
          click_coor = pygame.mouse.get_pos()

    print(distance(mass[0], click_coor))
    print(mass[1])
    print("cl_coor" + str(click_coor))
    if (distance(mass[0], click_coor) <= mass[1]):
        n += 1
    print("n = ", n)
    mass = ball.coordinates()
    click_coor = (-100, -100)
    
pygame.quit()
file = open('players.txt', 'a')
file.write(text1 + ' ' + str(n) + '\n')
file.close()    
print(text)
