import pygame
import math as m
from pygame.draw import *

pygame.init()

FPS = 30
X0 = 250
Y0 = 300

Xb = 700
Yb = 100
Rb = 40


n = 9
R = 50
Xt = 1200-X0
Yt = Y0

L = 300
H = 200
Ht = 100

triangle = ((X0, Y0), (X0+L, Y0), (X0+L/2, Y0-Ht))
    
rec = (X0, Y0, L, H)
rec_2 =( X0+L/2, Y0+H/4, H/3, H/3)
rec_t = ( 1200-X0, Y0, 40, 200)





screen = pygame.display.set_mode((1200, 700))
line(screen, (0, 100, 255),(0,0), (1200, 0), 700)
line(screen, (0, 255, 0),(0,700), (1200, 700), 700)


#Home
rect(screen, (200, 70, 150), rec,2)
rect(screen, (200, 70, 0), rec)
rect(screen, (39, 70, 240), rec_2, 4)
rect(screen, (205, 255, 100), rec_2)
polygon(screen, (123, 5, 111), triangle)

#tree
rect(screen, (0, 0, 0), rec_t)
circle(screen, (0, 70, 0), (Xt-R/2+20, Yt), R)
circle(screen, (0, 70, 0), (Xt+R/2+20, Yt), R)
circle(screen, (0, 70, 0), (Xt-R+20, Yt-R), R)
circle(screen, (0, 70, 0), (Xt+R+20, Yt-R), R)
circle(screen, (0, 70, 0), (Xt+20, Yt-R-30), R)

#cloud
circle(screen, (190, 200, 255), (Xb, Yb), Rb)
circle(screen, (190, 200, 255), (Xb + Rb/2, Yb), Rb)
circle(screen, (190, 200, 255), (Xb, Yb + Rb/2), Rb)
circle(screen, (190, 200, 255), (Xb + Rb, Yb + Rb/2), Rb)
circle(screen, (190, 200, 255), (Xb+ Rb/2, Yb + Rb), Rb)

#sun
circle(screen, (254, 243,5), (1000, 100), 70)









pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

