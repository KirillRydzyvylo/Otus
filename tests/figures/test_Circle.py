from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle
import pytest


@pytest.mark.parametrize(
    ("value", "expected"),
    (
            (None, TypeError),
            ("value", TypeError),
            ([1, 2, 3], TypeError),
            ((1, 2, 3), TypeError),
            (-1, TypeError),
            (0, TypeError),
    )
)
def test_check_expected_error(value, expected):
    with pytest.raises(expected):
        Circle(value)


@pytest.mark.parametrize(
    ("value", "expected"),
    (
            (1, 6.28),
            (10, 62.83),
            (100, 628.32),
    )
)
def test_check_perimeter(value, expected):
    circle = Circle(value)
    assert circle.perimeter == expected

@pytest.mark.parametrize(
    ("value", "expected"),
    (
            (1, 3.1),
            (10, 314.2),
            (100, 31415.9),
    )
)
def test_check_area(value, expected):
    circle = Circle(value)
    assert circle.area == expected

@pytest.mark.parametrize(
    ("value", "expected"),
    (
            (Circle(10), 628.4),
            (Rectangle(10, 15), 464.2),
            (Square(10), 414.2),
            (Triangle(11, 12, 13), 375.68),
    )
)
def test_check_add_area(value, expected):
    circle = Circle(10)
    assert circle.add_area(value) == expected


def test_check_add_area_error():
    circle = Circle(10)
    with pytest.raises(ValueError):
        circle.add_area([1, 2, 3])
