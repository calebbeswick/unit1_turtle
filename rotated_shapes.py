import turtle
turtle.hideturtle()
turtle.color("red")
turtle.speed(500)
for x in range(18):
    turtle.right(20)
    for x in range(4):
        turtle.forward(100)
        turtle.right(90)
turtle.exitonclick()