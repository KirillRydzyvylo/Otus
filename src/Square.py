from src.Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, height: int):
        Rectangle.__init__(self, height, height)
