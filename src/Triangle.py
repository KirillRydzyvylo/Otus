import math
from src.Figure import Figure


def is_exists(side_a, side_b, side_c):
    exists = side_a + side_b > side_c
    exists = exists and side_a + side_c > side_b
    return exists and side_b + side_c > side_a


class Triangle(Figure):
    def __init__(self, side_a: int, side_b: int, side_c: int):
        self.perimeter = float("{0:.2f}".format(side_a + side_b + side_c))
        self.area = float("{0:.2f}".format(math.sqrt(self.perimeter / 2 * (self.perimeter / 2 - side_a) *
                                                     (self.perimeter / 2 - side_b) * (self.perimeter / 2 - side_c))))

    def __new__(cls, side_a, side_b, side_c):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise TypeError("Значения сторон стреугоьника должны быть больше  0")

        if not is_exists(side_a, side_b, side_c):
            return None
        else:
            return object.__new__(cls)
