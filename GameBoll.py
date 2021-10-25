import pygame
from pygame.draw import *
from random import randint
pygame.init()
"""Big red ball- появляется с самого начала для ускорения набора очов. Дальше каждых пять попаданий он будет появляться. Если игрок уходит
в минус, ему нужно попасть так, чтоб счет стал равен пяти, тога появится бонусный шар, который даст возможность за один клик отиграть 11 очков"""
#Переменные
FPS = 30
X = 1000 #Ширина окна
Y = 800 #Высота окна
N = 3 #номер шарика
score = 0 #счет
flag = False #Флажок попадания
Big = False #Флажек большого шара

# Цвета используемые в игре
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, BLACK]

balls = []

#Програма

screen = pygame.display.set_mode((X, Y))


def new_ball():
    "Создание кординат шарика"
    global N
    if (score %5) == 0:
        for i in range(1):
            ball = {  'type': 'ball','x': randint(100,800),'y': randint(100,500),'vx': randint(-25,25),'vy': randint(-25,25),'radius': 100, 'color': COLORS[0]}
            balls.append(ball)
        for i in range(N):
            ball = {  'type': 'ball','x': randint(100,800),'y': randint(100,500),'vx': randint(-25,25),'vy': randint(-25,25),'radius': randint(30,50), 'color': COLORS[randint(1, 6)]}
            balls.append(ball)
        else:
            for i in range(N):
                    ball = {  'type': 'ball','x': randint(100,800),'y': randint(100,500),'vx': randint(-25,25),'vy': randint(-25,25),'radius': randint(30,50), 'color': COLORS[randint(1, 6)]}
                    balls.append(ball)

def draw_ball():
    "Рисование фигуры"
    global N
    for i in range(N):
        if not(0<balls[i]['x']-balls[i]['radius']<X-2*balls[i]['radius']):
            balls[i]['vx']=-balls[i]['vx']
        if not(0<balls[i]['y']-balls[i]['radius']<Y-2*balls[i]['radius']):
            balls[i]['vy']=-balls[i]['vy']
        balls[i]['x']+=balls[i]['vx']
        balls[i]['y']+=balls[i]['vy']
        circle(screen, balls[i]['color'], (balls[i]['x'], balls[i]['y']),balls[i]['radius'])


def click(points):
    "Обработка нажатия "
    global score, N, flag, Big

    for i in range(N):
        distance = (event.pos[0] - balls[i]['x'])**2 + (event.pos[1] - balls[i]['y'])**2

        if distance <= balls[i]['radius']**2:
            print('Попал!')
            flag = True
            if Big == True:
                score = points + 11
                change_ball(i)
                Big = False
            else:
                score = points + 1
                change_ball(i)



    if flag == False :
        print('Промах!')
        score = points - 1
    print('Счет:', score)
    flag = False


def change_ball(i):
    "Изменение крдинат шарика"
    global Big
    if (score %5) == 0:
       balls[1] = {  'type': 'ball','x': randint(100,800),'y': randint(100,500),'vx': randint(-25,25),'vy': randint(-25,25),'radius': 100, 'color': COLORS[0]}
       Big = True
    else:
        balls[i] = {  'type': 'ball','x': randint(100,800),'y': randint(100,500),'vx': randint(-25,25),'vy': randint(-25,25),'radius': randint(30,50), 'color': COLORS[randint(1, 5)]}










pygame.display.update()
clock = pygame.time.Clock()
finished = False
new_ball()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(score)
    screen.fill(WHITE)
    draw_ball()
    pygame.display.update()
    #print(balls)


pygame.quit()
