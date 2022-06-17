from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()


# turtle.color('red', 'green')
# turtle.begin_fill()
# for i in range(12):
#     turtle.forward(100)
#     turtle.right(150)
# turtle.end_fill()