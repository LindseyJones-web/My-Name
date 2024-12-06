import turtle as t

from Assignments.Assignment_3.Shape import Shape


def isEven(side):
    return side % 2 == 0


class Rectangle(Shape):
    def __init__(self, _xCor=0, _yCor=0, _width=100, _height=50, _color='black', _nameOfShape='Rectangle'):
        self.xCor = _xCor
        self.yCor = _yCor
        self.width = _width
        self.height = _height
        self.color = _color
        self.outLineColor = _color
        self.name = _nameOfShape


    def setXCor(self, newXCor):
        self.xCor = newXCor

    def setYCor(self, newYCor):
        self.yCor = newYCor

    def setWidth(self, newWidth):
        self.width = newWidth

    def setHeight(self, newHeight):
        self.height = newHeight

    def setColor(self, newColor):
        self.color - newColor

    def setOutLineColor(self, newColor):
        self.outLineColor = newColor

    def getXCor(self):
        return self.xCor

    def getYCor(self):
        return self.yCor

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getColor(self):
        return self.color

    def updateXCor(self, updateX):
        self.xCor += updateX

    def updateYCor(self, updateY):
        self.yCor += updateY

    def moveTurtle(self):
        t.penup()
        t.goto(self.xCor, self.yCor)
        t.pendown()

    def draw(self):
        numSides = 4
        self.moveTurtle()
        t.pencolor(self.outLineColor)
        t.fillcolor(self.color)
        t.begin_fill()
        t.pendown()
        for eachSide in range(numSides):
            if isEven(eachSide):
                t.forward(self.width)
            else:
                t.forward(self.height)
            t.right(90)
        t.penup()
        t.end_fill()

    def __str__(self):
        return f"Drawing {self.name} ..."
