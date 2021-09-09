import turtle


turtle.penup()
turtle.color("red")
turtle.goto(-100, 0)
turtle.pendown()
def draw_house():
    turtle.begin_fill()
    for x in range(3):
        turtle.fd(50)
        turtle.left(120)
    for y in range(4):
        turtle.fd(50)
        turtle.right(90)
    turtle.end_fill()

def pen_up_house():
    turtle.pendown()
    draw_house()
    turtle.penup()


pen_up_house()
turtle.goto(0, 0)
pen_up_house()
turtle.goto(100, 0)
pen_up_house()



turtle.exitonclick()