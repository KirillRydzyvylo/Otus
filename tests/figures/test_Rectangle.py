from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle
import pytest


@pytest.mark.parametrize(
    ("value_a", "value_b", "expected"),
    (
            (None, None, TypeError),
            ("value_a", "value_b", TypeError),
            ([1, 2, 3], 3, TypeError),
            ((1, 2, 3), "21", TypeError),
            (-1, -4, TypeError),
            (-1, 3, TypeError),
            (1, -3, TypeError)
    )
)
def test_check_expected_error(value_a, value_b, expected):
    with pytest.raises(expected):
        Rectangle(value_a, value_b)


@pytest.mark.parametrize(
    ("value_a", "value_b", "expected"),
    (
            (5, 6, 22),
            (10, 15, 50),
    )
)
def test_check_perimeter(value_a, value_b, expected):
    rectangle = Rectangle(value_a, value_b)
    assert rectangle.perimeter == expected


@pytest.mark.parametrize(
    ("value_a", "value_b", "expected"),
    (
            (5, 6, 30),
            (10, 15, 150),
    )
)
def test_check_area(value_a, value_b, expected):
    circle = Rectangle(value_a, value_b)
    assert circle.area == expected


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (Circle(10), 464.2),
        (Rectangle(10, 15), 300),
        (Square(10), 250),
        (Triangle(11, 12, 13), 211.48),
    ]
)
def test_check_add_area(value, expected):
    circle = Rectangle(10, 15)
    assert circle.add_area(value) == expected


def test_check_add_area_error():
    circle = Rectangle(10, 15)
    with pytest.raises(ValueError):
        circle.add_area([1, 2, 3])
