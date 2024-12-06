"""
Tasks To Perform:
    1. Create a folder Assignments. Inside this folder,
        create another folder Assignment_4. Download all the python files from D2L
        and placed them inside the folder Assignment_4. Complete the partial code and fix errors.

    2. After successful completion of this assignment,
        upload the screenshot of the outputs that displays the figure as shown in the sample output.
        The figure should exactly match with the figure shown in the sample output.
        Please check sample outputs for more information (50 Points).

    3. You should upload all the correct and complete Python files (Star.py, Shape.py, TurtleProperties.py,
        StarWithinStar.py) associated with this assignment.
        Your submission will not be accepted without all the Python files
        and the snapshots of sample outputs (40 Points).

    4. Title of your turtle screen should consist your full name (10 Points).
"""

import turtle as t
from Star import Star


def setTurtlePosition(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def maximizeWindow():
    screen = t.Screen()
    screen.setup(width=1.0, height=1.0)


def isEven(num):
    return num % 2 == 0


def drawStarsWithinStars(myStar, numStars):
    # Your code starts here
    for i in range(numStars):
        if isEven(i):
            myStar.setFillColor('white')
        else:
            myStar.setFillColor('yellow')

        myStar.setStarSize(myStar.getStarSize() * 0.9)
        myStar.updateXCor(-myStar.getStarSize() * 0.04)
        myStar.updateYCor(-myStar.getStarSize() * 0.1)
        myStar.moveTurtle()
        myStar.drawWithColor()

        if myStar.getStarSize() < 20:
            break




def start():
    t.shape("turtle")
    t.shapesize(stretch_wid=1.0, stretch_len=1.0)
    maximizeWindow()
    t.speed('fastest')
    t.title('Lindsey Jones - Stars Within Stars')

    myScreen = t.Screen()
    maxScreenWidth = myScreen.window_width()
    maxScreenHeight = myScreen.window_height()
    screenMargin = 25

    setTurtlePosition(-maxScreenWidth / 2 + screenMargin, maxScreenHeight / 3)

    textTobeDisplayed = "Figure: Stars Within Stars"
    t.color('white')
    t.write(textTobeDisplayed, font=('Helvetica', 16))

    t.Screen().bgcolor('black')
    myStar = Star(yCor=maxScreenHeight / 4, starSize=200, fillColor='white', borderColor='white', borderThickness=1)
    numStars = 15
    myStar.setBorderColor('black')
    drawStarsWithinStars(myStar, numStars)


if __name__ == '__main__':
    start()
    t.hideturtle()
    t.done()

