import turtle

turtle.color("red")
turtle.begin_fill()
for x in range(3):
    turtle.fd(100)
    turtle.left(120)
for y in range(4):
    turtle.fd(100)
    turtle.right(90)
turtle.end_fill()
turtle.exitonclick()