from src.Figure import Figure


class Rectangle(Figure):
    name = "Прямоугольник"

    def __init__(self, height: int, width: int):
        if height <= 0 or width <= 0:
            raise TypeError("Значения сторон прямоугольника должны быть больше  0")
        self.perimeter = (height + width) * 2
        self.area = height * width



