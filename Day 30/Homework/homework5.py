from turtle import *

def draw_square_at(x, y, size=100):
    penup()
    goto(x, y)
    pendown()
    for _ in range(4):
        forward(size)
        right(90)
    penup()

draw_square_at(50, 50)
done()