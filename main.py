# imports
import turtle

# window setup
# win = window
win = turtle.Screen()
win.setup(width=600, height=400)
win.tracer()

# game loop
closed = False
while not closed:
    win.update()