import turtle as t
from Assignments.Assignment_3.Shape import Shape


class Square(Shape):
    def __init__(self, _xCor=0, _yCor=0, _size=50, _color='black', _nameOfShape='Square'):
        self.xCor = _xCor
        self.yCor = _yCor
        self.size = _size
        self.color = _color
        self.outLineColor = _color
        self.name = _nameOfShape

    def setXCor(self, newXCor):
        self.xCor = newXCor

    def setYCor(self, newYCor):
        self.yCor = newYCor

    def setSize(self, newSize):
        self.size = newSize

    def setColor(self, newColor):
        self.color = newColor

    def setOutLineColor(self, newColor):
        self.outLineColor = newColor

    def getXCor(self):
        return self.xCor

    def getYCor(self):
        return self.yCor

    def getSize(self):
        return self.size

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
        for i in range(numSides):
            t.forward(self.size)
            t.right(90)
        t.penup()
        t.end_fill()

    def __str__(self):
        return f"Drawing {self.name} ..."
