import turtle

def makesquare(square_color):
    turtle.color(square_color)
    for x in range(10):
        turtle.right(36)
        for x in range(4):
            turtle.fd(50)
            turtle.right(90)


def makehexagon(hex_color):
    turtle.color(hex_color)
    for x in range(10):
        turtle.right(36)
        for x in range(6):
            turtle.fd(100)
            turtle.right(120)

def maketriangle(triangle_color):
    turtle.color(triangle_color)
    for x in range(40):
        turtle.right(9)
        for x in range(3):
            turtle.fd(150)
            turtle.right(120)

def maketriangle2(triangle_color2):
    turtle.color(triangle_color2)
    for x in range(60):
        turtle.right(6)
        for x in range(3):
            turtle.fd(25)
            turtle.right(120)

hex_color = input("Enter Hexagon Color")
turtle.hideturtle()
turtle.speed(100)
makehexagon(hex_color)
turtle.penup()

turtle.goto(-150, 200)

turtle.pendown()
square_color = input("Enter Square Color")
makesquare(square_color)


triangle_color2 = input("Enter First Triangle Color")
maketriangle2(triangle_color2)
turtle.penup()

turtle.goto(0,0)

turtle.pendown()
triangle_color = input("Enter Triangle Color")
maketriangle(triangle_color)

turtle.exitonclick()

