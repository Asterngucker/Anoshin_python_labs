import pygame as pg
import numpy as np
from pygame.draw import *

pg.init()

screen = pg.display.set_mode((1100, 800))

def circle_contour(color, radius, coordinates):
    circle(screen, color, coordinates, radius)
    circle(screen, black, coordinates, radius, 1)
def turned_rect(color, width, length, angle, coordinate_x, coordinate_y):
    x1 = coordinate_x
    y1 = coordinate_y
    x2 = x1 + length*np.cos(np.pi*angle/180)
    y2 = y1 + length*np.sin(np.pi*angle/180)
    x3 = coordinate_x - width*np.sin(np.pi*angle/180)
    y3 = coordinate_y + width
    x4 = x3 + length*np.cos(np.pi*angle/180)
    y4 = y3 + length*np.sin(np.pi*angle/180)
    polygon(screen, color, [(x1, y1), (x3, y3), (x4, y4), (x2, y2)])

gray = (167, 147, 172)
cyan = (0, 255, 255)
blue = (170, 238, 255)
magenta = (255, 0, 255)
pink = (255, 85, 221)
yellow = (255, 200, 0)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (55, 200, 113)
brown = (85, 0, 0)
body_color = (244, 227, 215)
screen.fill(green)
rect(screen, blue, (0, 0, 1100, 400))

aaline(screen, black, (160, 450), (290, 300), 2)
aaline(screen, black, (220, 700), (300, 530), 2)
aaline(screen, black, (170, 705), (220, 700), 2)
aaline(screen, black, (380, 700), (360, 530), 2)
aaline(screen, black, (430, 702), (380, 700), 2)
aaline(screen, black, (380, 300), (500, 450), 2)
aaline(screen, black, (495, 450), (680, 300), 2)
aaline(screen, black, (715, 300), (790, 370), 2)
aaline(screen, black, (790, 370), (880, 320), 2)
aaline(screen, black, (870, 370), (900, 200), 2)
aaline(screen, black, (670, 700), (670, 550), 2)
aaline(screen, black, (740, 700), (740, 550), 2)
aaline(screen, black, (630, 700), (670, 700), 2)
aaline(screen, black, (780, 700), (740, 700), 2)
ellipse(screen, gray, [260, 260, 150, 300], 0)
polygon(screen, pink, [(600, 550), (800, 550), (700, 250)])
circle(screen, body_color, (700, 220), 50)
circle(screen, body_color, (340, 220), 50)
polygon(screen, red, [(900, 100), (980, 150), (900, 200)])
circle(screen, red, (925, 107), 27)
circle(screen, red, (970, 125), 27)
polygon(screen, yellow, [(160, 450), (90, 380), (170, 350)])
circle(screen, red, (925, 107), 27)
circle(screen, red, (970, 125), 27)
circle(screen, red, (145, 340), 24)
circle(screen, brown, (105, 360), 24)
circle(screen, white, (110, 325), 24)

pg.display.update()
clock = pg.time.Clock()
finished = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
pg.quit()
