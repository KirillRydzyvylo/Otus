import math
from src.Figure import Figure


class Circle(Figure):
    name = "Круг"

    def __init__(self, radius: float):
        if radius <= 0:
            raise TypeError("Значение радиуса должно быть больше 0")
        self.perimeter = float("{0:.2f}".format(2 * math.pi * radius))
        self.area = float("{0:.1f}".format(math.pi * math.pow(radius, 2)))
