"""
Tasks To Perform:
    1. Create a folder Assignments. Inside this folder,
        create another folder Assignment_3. Download all the python files from D2L
        and placed them inside the folder Assignment_3. Complete the partial code and fix errors.

    2. Rename the iRobot_Lindsey_Jones.py to iRobot_Your_Full_Name.py. This is your main file (20 Points).

    3. After successful completion of this assignment,
        upload the screenshot of the outputs that displays the iRobot of different
        sizes, i.e., 50 pixels, 75 pixels, 100 pixels, and 125 pixels. Please check sample outputs
        for more information (80 Points).

    4. You should upload all the correct and complete Python files (Shape.py, Circle.py, Rectangle.py,
        Square.py, and iRobot_Your_Full_Name.py) associated with this assignment.
        Your submission will not be accepted without all the Python files
        and the snapshots of sample outputs (80 Points).

    5. Title of your turtle screen should consist your full name (20 Points).

    6. Challenge Problem (500 Bonus Points): Can you modify the code such that it will display
        three iRobots of different sizes in one screen? Please take a look at sample outputs.

"""
import turtle as t

from Assignments.Assignment_3.Circle import Circle
from Assignments.Assignment_3.Rectangle import Rectangle
from Assignments.Assignment_3.Square import Square

def setTurtlePosition(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def maximizeWindow():
    screen = t.Screen()
    screen.setup(width=1.0, height=1.0)


def drawRobot(xCor, yCor, faceSize):
    penSize = 0.1 * faceSize
    t.pensize(penSize)
    faceOfRobot = Square(xCor, yCor, faceSize, 'white', 'Face of a Robot')
    faceOfRobot.setOutLineColor('black')
    faceOfRobot.draw()

    xCor += faceOfRobot.getSize() / 4
    yCor -= faceOfRobot.getSize() / 2

    eyeSize = faceSize / 8
    eyeGap = faceSize / 2

    eyeOfRobot = Circle(xCor, yCor, eyeSize, 'black', 'Eye')
    eyeOfRobot.setOutLineColor('red')

    # left eye
    eyeOfRobot.draw()

    # right eye
    eyeOfRobot.setXCor(xCor + eyeGap)
    eyeOfRobot.draw()

    mouthWidth = faceOfRobot.getSize() / 2
    mouthHeight = faceOfRobot.getSize() / 4

    mouthOfRobot = Rectangle(xCor, yCor - eyeOfRobot.getRadius(),
                             mouthWidth, mouthHeight, 'black', 'Mouth of Robot')
    mouthOfRobot.setOutLineColor('red')
    mouthOfRobot.draw()

    neckPositionX = mouthOfRobot.getXCor()
    neckPositionY = mouthOfRobot.getYCor() - faceOfRobot.getSize() / 2.7

    neckWidth = mouthWidth
    neckHeight = mouthHeight
    neck = Rectangle(neckPositionX, neckPositionY, neckWidth,
                     neckHeight, 'white', 'Neck of Robot')
    neck.setOutLineColor('black')
    neck.draw()

    bodyWidth = 1.5 * faceOfRobot.getSize()
    bodyHeight = 2 * faceOfRobot.getSize()

    body = Rectangle(neck.getXCor() - neck.getWidth(),
                     neck.getYCor() - neck.getHeight(),
                     bodyWidth, bodyHeight, 'yellow', 'Body of Robot')
    body.setOutLineColor('black')
    body.draw()

    # left hand of the robot
    t.seth(300)
    handOfRobot = Rectangle(body.getXCor(), body.getYCor(),
                            body.getWidth() / 4, body.getHeight() / 1.5, body.getColor(), 'Hand')
    handOfRobot.setOutLineColor('black')
    handOfRobot.draw()

    # right hand of the robot
    t.seth(60)
    handOfRobot = Rectangle(body.getXCor() + 7 * body.getWidth() / 8, body.getYCor() - body.getHeight() + 165,
                            body.getWidth() / 4, body.getHeight() / 1.5,
                            body.getColor())
    handOfRobot.setOutLineColor('black')
    handOfRobot.draw()

    # redrawing the robot's body
    t.seth(0)
    body.draw()

    legPosX = body.getXCor() + body.getWidth() / 8
    legPosY = body.getYCor() - body.getHeight()

    legWidth = body.getWidth() / 4
    legHeight = body.getHeight() / 3

    legOfRobot = Rectangle(legPosX, legPosY, legWidth, legHeight, 'blue')
    legOfRobot.setOutLineColor('black')
    legOfRobot.draw()

    gapBetweenLegs = body.getWidth() / 2
    legOfRobot.updateXCor(gapBetweenLegs)
    legOfRobot.draw()

    setTurtlePosition(legOfRobot.getXCor() - legOfRobot.getWidth(),
                      legOfRobot.getYCor() - 2 * legOfRobot.getHeight())
    textTobeDisplayed = f"iRobot (Face Size: {faceSize} Pixels)"
    fontSize = round(faceSize / 4)
    t.write(textTobeDisplayed, font=('Helvetica', fontSize), align='center')


def drawSeriesOfiRobots(xCor, yCor, initialSize, reductionScaleRate, numRobots):
    pass


def startDrawing():
    t.shape('turtle')
    t.speed('fastest')
    t.title('Lindsey Jones: iRobot')
    maximizeWindow()
    myScreen = t.Screen()
    maxScreenWidth = myScreen.window_width()
    maxScreenHeight = myScreen.window_height()

    xCor = - 0.1 * maxScreenWidth
    yCor = 0.45 * maxScreenHeight
    faceSize = 100

    drawRobot(xCor, yCor, faceSize)

    t.hideturtle()
    t.mainloop()


if __name__ == '__main__':
    startDrawing()
