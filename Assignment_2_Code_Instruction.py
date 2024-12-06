"""
Tasks To Perform:
    1. Upload the screenshot of the output that displays the landscape of stairs as shown
        in the sample output (50 Points).

        Size of each step: 25 pixels
        Number of total stairs: 4

        Note: First stairs should consist 1 step, Second stairs should consist 2 steps,
        Third stairs should consist of 3 steps, and so on. Please check the image file for
        more information.

    2. You should upload a Python file with a correct code that draws two rectangles.
        Your should rename the Python file to Assignment_2_TypeYourName.py before uploading
        it to D2L. Your submission will not be accepted without the
        Python file and the snapshots of sample outputs (Assignment_2_TypeYourName.py) (30 Points).

    3. Title of your turtle screen should contain your full name (10 Points).

    4. Explain the use of built-in functions goto(),  forward(...), backward(...).
        You should explain in detail to get points. Lackadaisical answer will get zero points (10 Points).

    5. Challenge Problem (0 Bonus Points): Your output should display the landscape of stairs as shown
        in the sample output (image file) herewith.

"""

import turtle as t


def displayScreenInfinitely():
    t.mainloop()


def setTurtlePosition(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def maximizeWindow():
    screen = t.Screen()
    screen.setup(width=1.0, height=1.0)


def drawAStairCase(numSteps, stepSize):
    pass


def main():
    # Specify the shape of the turtle, i.e., turtle, circle, square, arrow, triangle, classic.
    t.shape("turtle")
    t.shapesize(stretch_wid=2.0, stretch_len=2.0)

    # “fastest”: 0, “fast”: 10, “normal”: 6, "slow”: 3, “slowest”: 1
    t.speed('fastest')
    t.title('Lindsey Jones: The Landscape of Stairs')
    maximizeWindow()
    myScreen = t.Screen()
    maxScreenWidth = myScreen.window_width()
    maxScreenHeight = myScreen.window_height()
    print(f"Width: {maxScreenWidth}\nHeight: {maxScreenHeight}")
    screenMargin = 25

    setTurtlePosition(-maxScreenWidth / 2 + screenMargin, maxScreenHeight / 2 - screenMargin)
    textTobeDisplayed = f"Your Screen Resolution: {maxScreenWidth} X {maxScreenHeight}"
    t.write(textTobeDisplayed, font=('Helvetica', 16))

    setTurtlePosition(-maxScreenWidth / 2 + screenMargin, 0)

    # Start your code here to instruct turtle pen to draw a landscape of stairs.
   # First Stair
    t.left(90)
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(25)

    t.left(90)
    t.forward(25)

# Second Stair
    t.left(90)
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.left(90)
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(50)

# Third Stair
    t.left(90)
    t.forward(25)
    
    t.left(90)
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.left(90)
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.left(90)
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(75)

    t.left(90)
    t.forward(25)

# Fourth Stair
    t.left(90)
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.left(90)
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.left(90)
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.left(90)
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(100)

    t.left(90)
    t.forward(25)


    setTurtlePosition(-maxScreenWidth / 2 + screenMargin, -3 * screenMargin)
    t.write("The Landscape of Stairs", font=('Helvetica', 16))

    t.hideturtle()
    displayScreenInfinitely()


if __name__ == '__main__':
    main()

