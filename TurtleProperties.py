"""

    @ Author: Dr. Romas James Hada

"""
import turtle as t


class TurtleProperties:
    def __init__(self, _xCor=0, _yCor=0, _fillColor='white',
                 _borderColor='black', _borderThickness=3, _nameOfShape='Shape'):
        self.xCor = _xCor
        self.yCor = _yCor
        self.fillColor = _fillColor
        self.borderColor = _borderColor
        self.borderThickness = _borderThickness
        self.name = _nameOfShape

    def setXCor(self, newXCor):
        self.xCor = newXCor

    def setYCor(self, newYCor):
        self.yCor = newYCor

    def setFillColor(self, newColor):
        self.fillColor = newColor

    def setBorderColor(self, newColor):
        self.borderColor = newColor

    def setBorderThickness(self, thickness):
        self.borderThickness = thickness

    def setName(self, name):
        self.name = name

    def getXCor(self):
        return self.xCor

    def getYCor(self):
        return self.yCor

    def getFillColor(self):
        return self.fillColor

    def getBorderColor(self):
        return self.borderColor

    def getBorderThickness(self):
        return self.borderThickness

    def getName(self):
        return self.name

    def updateXCor(self, updateX):
        self.xCor += updateX

    def updateYCor(self, updateY):
        self.yCor += updateY

    def moveTurtle(self):
        t.penup()
        t.goto(self.xCor, self.yCor)
        t.pendown()

    def __str__(self):
        return f"Drawing {self.name} ..."
