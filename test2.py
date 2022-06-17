import turtle
# import random

wn = turtle.Screen()
turtle.fillcolor('red')
turtle.begin_fill()
turtle.width(5)
turtle.shape("turtle")

for i in range(3):
    turtle.forward(200)
    turtle.left(120)
turtle.end_fill()
wn.exitonclick()
