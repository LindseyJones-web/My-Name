"""

   @ Author: Dr. Romas James Hada

"""

from abc import abstractmethod, ABC
from TurtleProperties import TurtleProperties


class Shape(ABC, TurtleProperties):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def drawWithColor(self):
        pass
