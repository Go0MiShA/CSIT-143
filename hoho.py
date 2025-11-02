import turtle

screen = turtle.Screen()
screen.setup(480, 540)
screen.bgpic("mypic.gif")

cx, cy = 60, -90
top_width = 60
bottom_width = 80
height = 30

top_w2 = top_width / 2
bottom_w2 = bottom_width / 2
h2 = height / 2

points = [
    (cx - top_w2, cy + h2),
    (cx + top_w2, cy + h2),
    (cx + bottom_w2, cy - h2),
    (cx - bottom_w2, cy - h2)
]

pen = turtle.Turtle()
pen.speed(500)
pen.color("black")
pen.width(1)
pen.hideturtle()

pen.penup()
pen.goto(points[0])
pen.pendown()
pen.begin_fill()
for x, y in points[1:]:
    pen.goto(x, y)
pen.goto(points[0])
pen.end_fill()

turtle.done()
