import pygame
import math as m
from pygame.draw import *

pygame.init()

FPS = 30
X0 = 50
Y0 = 300

Xb = 700
Yb = 100
Rb = 40

X2 = 700
Y2 = Y0

n = 9
R = 50
Xt = X0 + 400
Yt = Y0
Xt2 = X2 + 200
Yt2 = Y0
R2 = R/2
L = 300
H = 200
Ht = 100

X2 = 700
Y2 = Y0

rec = (X0, Y0, L, H)
rec_2 =( X0+L/2, Y0+H/4, H/3, H/3)
rec_t = ( Xt, Yt, 40, 200)
triangle = ((X0, Y0), (X0+L, Y0), (X0+L/2, Y0-Ht))


rec11 = (X2,Y0, L/2, H/2)
rec_22 =(X2+L/4, Y0+H/6, H/6, H/6)
triangle2 = ((X2, Y0), (X2+L/2, Y0), (X2+L/4, Y0-Ht/2))
rec_t2 = ( Xt2, Yt2, 20, 100)



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


#Home2
rect(screen, (200, 70, 150), rec11,2)
rect(screen, (200, 70, 0), rec11)
rect(screen, (39, 70, 240), rec_22, 4)  #window
rect(screen, (205, 255, 100), rec_22)
polygon(screen, (123, 5, 111), triangle2)


#tree2
rect(screen, (0, 0, 0), rec_t2)
circle(screen, (0, 70, 0), (Xt2-R2/2+20, Yt2), R)
circle(screen, (0, 70, 0), (Xt2+R2/2+20, Yt2), R)
circle(screen, (0, 70, 0), (Xt2-R2+20, Yt2-R2), R)
circle(screen, (0, 70, 0), (Xt2+R2+20, Yt2-R2), R)
circle(screen, (0, 70, 0), (Xt2+20, Yt2-R2-30), R)

#cloud2
circle(screen, (190, 200, 255), (Xb-300, Yb), Rb)
circle(screen, (190, 200, 255), (Xb-300 + Rb/2, Yb), Rb)
circle(screen, (190, 200, 255), (Xb-300, Yb + Rb/2), Rb)
circle(screen, (190, 200, 255), (Xb-300 + Rb, Yb + Rb/2), Rb)
circle(screen, (190, 200, 255), (Xb-300+ Rb/2, Yb + Rb), Rb)


#cloud3
circle(screen, (190, 200, 255), (Xb-500, Yb), Rb)
circle(screen, (190, 200, 255), (Xb-500 + Rb/2, Yb), Rb)
circle(screen, (190, 200, 255), (Xb-500, Yb + Rb/2), Rb)
circle(screen, (190, 200, 255), (Xb-500 + Rb, Yb + Rb/2), Rb)
circle(screen, (190, 200, 255), (Xb-500+ Rb/2, Yb + Rb), Rb)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
