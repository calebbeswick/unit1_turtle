import turtle

turtle.color("red")

turtle.fd(200)
turtle.right(144)
turtle.fd(200)
turtle.right(144)
turtle.fd(200)
turtle.right(144)
turtle.fd(200)
turtle.right(144)
turtle.fd(200)

turtle.penup()
turtle.goto(-150, 100)
turtle.pendown()

turtle.color("blue")

turtle.fd(50)
turtle.right(144)
turtle.fd(50)
turtle.right(144)
turtle.fd(50)
turtle.right(144)
turtle.fd(50)
turtle.right(144)
turtle.fd(50)

turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()

turtle.begin_fill()
turtle.fd(75)
turtle.right(144)
turtle.fd(75)
turtle.right(144)
turtle.fd(75)
turtle.right(144)
turtle.fd(75)
turtle.right(144)
turtle.fd(75)
turtle.end_fill()

turtle.exitonclick()