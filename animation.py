import turtle

turtle.bgcolor('black')
turtle = turtle.Turtle()
colors = ['yellow', 'white', 'cyan', 'pink', 'blue', 'red', 'green', 'magenta', 'orange']

length = 0
angle = 360//len(colors) - 1

while True:
    for color in colors:
        width = length/100 + 1
        turtle.pencolor(color)
        turtle.width(width)
        turtle.forward(length)
        turtle.right(angle)
        length += 1