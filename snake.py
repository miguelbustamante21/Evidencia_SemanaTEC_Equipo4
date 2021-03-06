"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

Team members

Miguel Angel Bustamante Pérez A01781583
Espacio 1
Espacio 2

"""
#Libraries 

from turtle import * #brings objects from the module. turtle is a python feature like a drawing board 
from random import randrange #randrange is a function that returns a random integer number within the given range 
from freegames import square, vector 


food = vector(15, 4) #miguel, cambiar la pos inicial
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction." #Alonso
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        print("Level Up") #Alonso
    else:
        print("Endgame") #Alonso
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'cyan') #miguel cambio el color de la serpiente

    square(food.x, food.y, 9, 'green yellow') #miguel cambio el color de la comida 
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
