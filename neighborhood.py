import turtle


def draw_house(size, roof_color, house_color):
    turtle.color(roof_color)
    turtle.begin_fill()
    for x in range(3):
        turtle.fd(size)
        turtle.left(120)

    turtle.end_fill()

    turtle.color(house_color)
    turtle.begin_fill()
    for y in range(4):
        turtle.fd(size)
        turtle.right(90)
    turtle.end_fill()


def draw_multiple_houses(x_coordinate, y_coordinate):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x_coordinate, y_coordinate)
    turtle.pendown()
    draw_house(size, roof_color, house_color)

x_coordinate = int(input("Enter x coordinate"))
y_coordinate = int(input("Enter y coordinate"))
size = int(input("Enter house size"))
roof_color = input("Enter Roof Color")
house_color = input("Enter House Color")


draw_multiple_houses(x_coordinate, y_coordinate)

turtle.exitonclick()
