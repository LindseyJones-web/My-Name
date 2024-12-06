import turtle as t

from Shape import Shape


class Star(Shape):
    def __init__(self, starSize=50, xCor=0, yCor=0,
                 fillColor='white', borderColor='black',
                 borderThickness=1, nameOfShape='Stars'):
        super().__init__(xCor, yCor, fillColor, borderColor, borderThickness, nameOfShape)
        self.starSize = starSize

    def setStarSize(self, newSize):
        self.starSize = newSize

    def getStarSize(self):
        return self.starSize

    def drawSawTooth(self):
        t.forward(self.starSize)
        t.right(120)
        t.forward(self.starSize)

    def draw(self):
        t.pencolor(self.borderColor)
        t.pensize(self.borderThickness)
        numSawTooth = 5
        for eachSide in range(numSawTooth):
            self.drawSawTooth()
            t.left(48)

    def drawWithColor(self):
        t.fillcolor(self.fillColor)
        t.begin_fill()
        self.draw()
        t.end_fill()


if __name__ == '__main__':
    testStar = Star()
    testStar.draw()

    t.hideturtle()
    t.mainloop()
