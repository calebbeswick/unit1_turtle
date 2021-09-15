import turtle


turtle.color("black")
turtle.hideturtle()
turtle.speed(100)
turtle.pensize(10)

for x in range(4):
    turtle.circle(50)
    turtle.penup()
    turtle.fd(80)
    turtle.pendown()




turtle.exitonclick()