import random
import turtle
from PIL import ImageGrab
def draw_spiral():
    turtle.speed(0)
    turtle.bgcolor('black')
    colors = ["red", "yellow", "blue", "green"]
    length = 10
    for i in range(100):
        turtle.forward(length)
        turtle.right(120)
        if i % 5 == 0:
            turtle.pencolor(random.choice(colors))
        length = length + 1

    canvas = turtle.getscreen().getcanvas()
    canvas.postscript(file="temp.eps")
    img = ImageGrab.grab(bbox=canvas.winfo_screen())
    img.save("spiral.png", "PNG")
    turtle.done()


draw_spiral()
