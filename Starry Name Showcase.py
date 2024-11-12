import turtle as t
from Star import Star
from Letter_Class import DrawLetters
import random

def displayScreenInfinitely():
    t.mainloop()

def setTurtlePosition(x, y):
    t.penup()
    t.setposition(x, y)
    t.pendown()

def maximizeWindow():
    screen = t.Screen()
    screen.setup(width=1.0, height=1.0)

def main():
    t.shape("turtle")
    t.speed('fastest')
    myScreen = t.Screen()
    myScreen.setup(width=1.0, height=1.0)
    myScreen.bgcolor('black')
    t.shapesize(stretch_wid=2.0, stretch_len=2.0)
    t.title('Starry Name Showcase')
    maximizeWindow()
    setTurtlePosition(-400, 200)

    drawer = DrawLetters()


    drawer.draw_letter_L()
    drawer.draw_letter_I()
    drawer.draw_letter_N()
    drawer.draw_letter_D()
    drawer.draw_letter_S()
    drawer.draw_letter_E()
    drawer.draw_letter_Y()
    drawer.draw_letter_J()
    drawer.draw_letter_O()
    drawer.draw_letter_N2()
    drawer.draw_letter_E2()
    drawer.draw_letter_S2()

    numStars = 50
    myStar = Star(starSize=100, borderColor='yellow', fillColor='white', borderThickness=1)
    for star in range(numStars):
        myStar.setXCor(random.randint(-400, 500))
        myStar.setYCor(random.randint(-300, 300))
        size = random.randint(5, 15)
        myStar.setStarSize(size)
        myStar.moveTurtle()
        myStar.drawWithColor()

    t.hideturtle()
    drawer.display_screen_infinitely()

if __name__ == '__main__':
    main()



