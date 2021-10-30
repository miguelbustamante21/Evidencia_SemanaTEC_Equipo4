"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.

Integrantes 
Miguel Bustamante A01781583
Luis Vasquez A01028111
Alonso Sanchez A01368013
"""

from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(10, 10) #Luis#
targets = []

def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -189 #miguel
        ball.y = -179 #miguel
        speed.x = (x + 500) / 25 #miguel
        speed.y = (y + 800) / 25 #miguel

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    "Move ball and targets."
    # Generate a new target at random times
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    # Move the existing targets
    for target in targets:
        target.x -= 0.5

    # Move the cannon shot
    if inside(ball):
        speed.y -= 0.50 #Luis#
        ball.move(speed)

    # Make a copy of the existing target list before redrawing
    dupe = targets.copy()
    targets.clear()

    # Detect if the bullet hits a target
    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    # Detect when a target reaches the left side
    for target in targets:
        if not inside(target):
            #targets.remove(target)
            return

    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
