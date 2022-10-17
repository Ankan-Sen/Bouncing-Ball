import pygame as p
import time as t
import random as r

p.init()

# ---------define constants------------------
WIDTH = 1000
HEIGHT = 600
RADIUS = 10
FPS = 60
G = 9
X_VEL = 2
Y_VEL = 0
X_POS = 50
Y_POS = 300
timeStep = 1 / FPS
screen = p.display.set_mode((WIDTH, HEIGHT))
bgcolor = (0, 0, 0)
screen.fill((0, 0, 0))
x_start = [20, 120, 300, 452, 750, 920, 550, 650]
y_start = [120, 45, 350, 425, 153, 540, 75, 220]
x_bonus = [160, 200, 390, 280, 478, 820, 560, 740]
y_bonus = [10, 45, 255, 510, 320, 123, 476, 215]
Adder = 3
run = True


for i in range(8):           # Drawing Obstacles
    p.draw.rect(screen, (150, 0, 0), (x_start[i], y_start[i], 50, 50), 25)
    p.display.update()


def drawBonus():
    k = r.randint(0, 7)
    p.draw.rect(screen, (0, 150, 0), (x_bonus[k], y_bonus[k], 10, 10), 5)
    p.display.update()
    return k


def detectCollision(x, y):
    for j in range(8):
        if x_start[j] - 10 <= x <= x_start[j] + 60 and y_start[j] - 10 <= y <= y_start[j] + 60:
            return True
    return False


def detectBonus(x, y, index):
    if x_bonus[index] - 10 <= x <= x_bonus[index] + 20 and y_bonus[index] - 10 <= y <= y_bonus[index] + 20:
        p.draw.rect(screen, bgcolor, (x_bonus[index], y_bonus[index], 10, 10), 5)
        return True
    return False


flag = 0
score = 0
idx = 0
print("Score = 0")

# -----------main loop---------------------
while run:
    p.draw.circle(screen, bgcolor, (X_POS, Y_POS), RADIUS)
    if flag == 0:
        idx = drawBonus()
        flag = 1
    for e in p.event.get():
        if e.type == p.QUIT:
            run = False
        elif e.type == p.KEYDOWN:
            if e.key == p.K_UP:
                Y_VEL -= Adder
            if e.key == p.K_DOWN:
                Y_VEL += Adder
    if Y_POS >= HEIGHT - RADIUS or Y_POS <= RADIUS:
        Y_VEL = -Y_VEL                                      # Rebound if hitting border
        G += 0.5
        Adder += 1
    if X_POS >= WIDTH - RADIUS or X_POS <= RADIUS:
        X_VEL = -(X_VEL + 0.2)
    Y_VEL += G * timeStep
    Y_POS += int(Y_VEL)
    X_POS += int(X_VEL)
    p.draw.circle(screen, (0, 0, 150), (X_POS, Y_POS), RADIUS)
    if detectBonus(X_POS, Y_POS, idx):
        score += 1
        print("Score = ", score)
        flag = 0
    if detectCollision(X_POS, Y_POS):
        print("Game Over")
        t.sleep(3)
        exit()
    t.sleep(0.91 * timeStep)
    p.display.update()
