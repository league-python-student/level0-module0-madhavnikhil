import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    my_Harry = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    my_Harry.shape('turtle')
    # Set your turtle's speed using .speed(2)
    my_Harry.speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    my_Harry.color('green')
    my_Harry.pencolor('blue')
    # Move your turtle forward using .forward(100)
    my_Harry.forward(100)
    # TEST    Did your turtle move forward?

    # Move your turtle left or right using .left(90) or .right(90)
    my_Harry.left(90)
    # Now put the forward and left/right code into a for loop to repeat 4 times.

    for i in range(4):
        my_Harry.forward(100)
        my_Harry.left(90)


    # TEST    Did your turtle draw a square?

    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    my_Harry.goto(0, 0)


    # TEST    Did your turtle draw a circle?
    my_Harry.begin_fill()
    my_Harry.circle(20)
    # Add color to your shape by adding .begin_fill() before drawing the circle
    my_Harry.end_fill()
    # and .end_fill() below

    # Draw 3 more shapes with different fill colors!
    my_Harry.color("red")
    my_Harry.begin_fill()

    for i in range(3):
        my_Harry.forward(100)
        my_Harry.left(120)

    my_Harry.end_fill()

    my_Harry.color("blue")
    my_Harry.begin_fill()

    for i in range(5):
        my_Harry.forward(100)
        my_Harry.left(72)
        my_Harry.forward(100)
    my_Harry.end_fill()


    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
