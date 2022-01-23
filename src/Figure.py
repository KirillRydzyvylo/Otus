class Figure:
    area: float = 0

    def __init__(self):
        raise UnusableObjectError("Запрещено создавать объект данного класса")

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return self.area + figure.area
        raise ValueError("Передан неправильный класс")


class UnusableObjectError(Exception):
    pass
