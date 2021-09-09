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

draw_house(200, "blue", "red")

turtle.exitonclick()