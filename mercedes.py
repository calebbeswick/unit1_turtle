import turtle

turtle.pensize(3)
turtle.color("silver")
turtle.hideturtle()
turtle.circle(100)
turtle.left(90)
turtle.penup()
turtle.fd(100)
turtle.pendown()

for x in range(3):
    turtle.fd(100)
    turtle.penup()
    turtle.fd(-100)
    turtle.left(120)
    turtle.pendown()


turtle.exitonclick()