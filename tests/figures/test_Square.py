from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle
import pytest


@pytest.mark.parametrize(
    ("value_a", "expected"),
    (
            (None, TypeError),
            ("value_a", TypeError),
            ([1, 2, 3], TypeError),
            ((1, 2, 3), TypeError),
            (-1, TypeError),
            (-1, TypeError),
    )
)
def test_check_expected_error(value_a, expected):
    with pytest.raises(expected):
        Square(value_a, )


@pytest.mark.parametrize(
    ("value_a", "expected"),
    (
            (5, 20),
            (10, 40),
    )
)
def test_check_perimeter(value_a, expected):
    rectangle = Square(value_a, )
    assert rectangle.perimeter == expected


@pytest.mark.parametrize(
    ("value_a", "expected"),
    (
            (5, 25),
            (10, 100),
    )
)
def test_check_area(value_a, expected):
    circle = Square(value_a, )
    assert circle.area == expected


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (Circle(10), 414.2),
        (Rectangle(10, 15), 250),
        (Square(10), 200),
        (Triangle(11, 12, 13), 161.48),
    ]
)
def test_check_add_area(value, expected):
    circle = Square(10, )
    assert circle.add_area(value) == expected


def test_check_add_area_error():
    circle = Square(10, )
    with pytest.raises(ValueError):
        circle.add_area([1, 2, 3])
