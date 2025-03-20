from turtle import *

# we want to draw a house

# step 1: draw a square
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
# end of square

# drawing a door
begin_fill()
forward(70)
color("yellow")
left(90)
forward(120)          # height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
# drawing the roof

penup()
goto(200, 200)
pendown()
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
# drawing a window
color("saddle brown")
penup()
goto(180, 180)
pendown()

right(60)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(15)
left(90)
forward(30)
left(90)
forward(15)
left(90)
forward(15)
left(90)
forward(30)

penup()
goto(20, 180)
pendown()


left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(15)
left(90)
forward(30)
left(90)
forward(15)
left(90)
forward(15)
left(90)
forward(30)

# end of drawing a window
# end of drawing a house

exitonclick()

