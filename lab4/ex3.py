import pygame as pg
import numpy as np
from pygame.draw import *
pg.init()

screen = pg.display.set_mode((1200, 800))

def draw_ellipse_angle(surface, color, rect, angle, width=0):
    target_rect = pg.Rect(rect)
    shape_surf = pg.Surface(target_rect.size, pg.SRCALPHA)
    ellipse(shape_surf, color, (0, 0, *target_rect.size))
    rotated_surf = pg.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(center = target_rect.center))
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
rect(screen, blue, (0, 0, 1200, 400))

aaline(screen, black, (160, 500), (270, 390), 4)
aaline(screen, black, (220, 700), (280, 530), 2)
aaline(screen, black, (190, 705), (220, 700), 2)
aaline(screen, black, (350, 700), (310, 530), 2)
aaline(screen, black, (380, 702), (350, 700), 2)
aaline(screen, black, (320, 395), (410, 490), 2)
aaline(screen, black, (410, 490), (520, 380), 2)
aaline(screen, black, (520, 390), (580, 440), 2)
aaline(screen, black, (580, 440), (620, 410), 2)
#aaline(screen, black, (790, 370), (880, 320), 2)
#aaline(screen, black, (870, 370), (900, 200), 2)
aaline(screen, black, (495, 700), (495, 550), 2)
aaline(screen, black, (540, 700), (540, 550), 2)
aaline(screen, black, (475, 700), (495, 700), 2)
aaline(screen, black, (560, 700), (540, 700), 2)

aaline(screen, black, (620, 410), (630, 200), 2)
polygon(screen, yellow, [(630, 200), (570, 100), (680, 100)])
draw_ellipse_angle(screen, red, [620, 65, 60, 50], -20, 2)
draw_ellipse_angle(screen, brown, [570, 65, 60, 50], -20, 2)
draw_ellipse_angle(screen, white, [590, 35, 60, 50], -20, 2)

aaline(screen, black, (140, 350), (170, 495), 4)
polygon(screen, red, [(140, 350), (70, 280), (155, 250)])
circle(screen, red, (95, 270), 27)
circle(screen, red, (130, 260), 27)

aaline(screen, black, (620, 410), (650, 440), 2)
aaline(screen, black, (650, 440), (710, 390), 2)
aaline(screen, black, (720, 390), (840, 490), 2)
aaline(screen, black, (695, 700), (695, 550), 2)
aaline(screen, black, (740, 700), (740, 550), 2)
aaline(screen, black, (675, 700), (695, 700), 2)
aaline(screen, black, (760, 700), (740, 700), 2)

aaline(screen, black, (830, 490), (920, 390), 4)
aaline(screen, black, (870, 700), (930, 530), 2)
aaline(screen, black, (840, 705), (870, 700), 2)
aaline(screen, black, (1000, 700), (960, 530), 2)
aaline(screen, black, (1030, 702), (1000, 700), 2)
aaline(screen, black, (970, 395), (1060, 490), 2)

ellipse(screen, gray, [240, 370, 100, 200], 0)
ellipse(screen, gray, [890, 370, 100, 200], 0)
polygon(screen, pink, [(450, 580), (580, 580), (515, 350)])
polygon(screen, pink, [(650, 580), (780, 580), (715, 350)])
circle(screen, body_color, (515, 330), 40)
circle(screen, body_color, (290, 330), 40)
circle(screen, body_color, (715, 330), 40)
circle(screen, body_color, (940, 330), 40)

polygon(screen, yellow, [(1050, 400), (1130, 450), (1050, 500)])
draw_ellipse_angle(screen, red, [1085, 400, 60, 40], -65, 2)
draw_ellipse_angle(screen, brown, [1045, 380, 60, 40], -65, 2)
draw_ellipse_angle(screen, white, [1070, 355, 60, 40], -65, 2)






pg.display.update()
clock = pg.time.Clock()
finished = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
pg.quit()
