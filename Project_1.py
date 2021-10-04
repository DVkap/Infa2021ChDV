import pygame
from pygame.draw import *

pygame.init()

FPS = 30
x = 60
pintBrov = ((485-x, 235-x), (485+x, 235+x))





screen = pygame.display.set_mode((1200, 700))

circle(screen, (255,255,0), (600,400), 300)

circle(screen, (255,0,0), (450,250), 50)
circle(screen, (0,0,0), (450,250), 30)
line(screen, (0,0,0), (500-x, 210-x), (500+x, 210+x),40)

circle(screen, (255,0,0), (750,250), 50)
circle(screen, (0,0,0), (750,250), 20)
line(screen, (0,0,0), (700+x, 210-x), (700-x, 210+x),40)

rect(screen, (0,0,0), (450, 550, 300,70))



'''rect(screen, (255, 0, 255), (600, 500, 200, 200))

rect(screen, (0, 0, 255), (100, 100, 200, 200), 5)

polygon(screen, (255, 255, 0), [(100,100), (200,50), (300,100), (100,100)])

polygon(screen, (0, 0, 255), [(100,100), (200,50), (300,100), (100,100)], 5)

circle(screen, (0, 255, 0), (200, 175), 50)

circle(screen, (255, 255, 255), (200, 175), 50, 5)'''

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

