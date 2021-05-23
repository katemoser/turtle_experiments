import turtle
from turtle import Turtle, Screen, colormode
from random import randint, choice
import colorgram


#generate a list of colors from an image
#print(colors)

turtle.colormode(255)
kitty = Turtle()
kitty.shape("turtle")
kitty.color("CornflowerBlue")
kitty.speed(0)
kitty.pensize(3)

puppy = Turtle()

def generate_palette(image, num_colors):
    palette = colorgram.extract(image, num_colors)
    return palette


def generate_random_color():
    new_color = ((randint(0, 255), randint(0, 255), randint(0, 255)))
    print(new_color)
    return new_color


def draw_shape(pen, num_sides):
    for line in range(num_sides):
        pen.forward(100)
        pen.right(360 / num_sides)


def shapes_within_shapes(pen, num_shapes):
    for num_side in range(3, num_shapes + 1):
        # change to random color
        pen.pencolor(generate_random_color())
        draw_shape(num_side)


def random_grid_walk(pen, num_segments):
    directions = [0, 90, 180, 270]
    for segment in range(0, num_segments):
        pen.color(generate_random_color())
        angle = directions[randint(0, len(directions) - 1)]

        pen.right(angle)
        pen.forward(30)

def random_cool_walk(pen, num_segments):
    for segment in range(0,num_segments):
        pen.color(generate_random_color())
        pen.left(randint(-359,359))
        pen.forward(15)

def random_smooth_walk(pen, num_segments):
    for segment in range(0, num_segments):
        pen.color(generate_random_color())
        pen.left(randint(-100, 100))
        pen.forward(10)

def spirograph(pen, size, num_circles):
    for circle in range(0, num_circles):
        pen.color(generate_random_color())
        pen.circle(size)
        pen.left(360/num_circles)

def hirst_dot_painting(image, num_colors, pen, start_pos, width_of_painting, size_of_dot, gap):
    colors = generate_palette(image,num_colors)
    pen.penup()
    pen.setposition(start_pos)
    start_x = start_pos[0]
    for y in range(width_of_painting):
        for x in range(width_of_painting):
            random_color = colors[randint(0,len(colors)-1)].rgb
            pen.dot(size_of_dot, random_color)
            pen.forward(gap)
        pen.setpos(start_x, pen.ycor() + gap)
        pen.setheading(0)


hirst_dot_painting('girl.jpg', 100, kitty, (-150, -150), 20, 20, 20)

screen = Screen()
screen.exitonclick()
