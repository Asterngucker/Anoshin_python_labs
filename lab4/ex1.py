import pygame as pg
import numpy as np
from pygame.draw import *

pg.init()

screen = pg.display.set_mode((500, 500))

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

gray = (200, 200, 200)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
yellow = (255, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

screen.fill(gray)
circle_contour(yellow, 100, (255, 255))
circle_contour(red, 20, (210, 240))
circle(screen, black, (210, 240), 8)
circle_contour(red, 15, (300, 240))
circle(screen, black, (300, 240), 8)
rect(screen, black, (220, 300, 75, 15))
turned_rect(black, 8, 80, 30, 170, 190)
turned_rect(black, 8, 80, -20, 270, 230)
pg.display.update()
clock = pg.time.Clock()
finished = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
pg.quit()
