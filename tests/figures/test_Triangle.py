from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle
import pytest


@pytest.mark.parametrize(
    ("value_a", "value_b", "value_c", "expected"),
    (
            (None, 1, 4, TypeError),
            ("value_a", 3, 4, TypeError),
            ([1, 2, 3], 3, 1, TypeError),
            ((1, 2, 3), 21, 13, TypeError),
            (-1, 11, 23, TypeError),
            (-1, 32, 33, TypeError),
    )
)
def test_check_expected_error(value_a, value_b, value_c, expected):
    with pytest.raises(expected):
        Triangle(value_a, value_b, value_c)


@pytest.mark.parametrize(
    ("value_a", "value_b", "value_c", "expected"),
    (
            (10, 11, 12, 33),
            (3, 4, 5, 12),
    )
)
def test_check_perimeter(value_a, value_b, value_c, expected):
    triangle = Triangle(value_a, value_b, value_c)
    assert triangle.perimeter == expected


@pytest.mark.parametrize(
    ("value_a", "value_b", "value_c", "expected"),
    (
            (10, 11, 12, 51.52),
            (3, 4, 5, 6),
    )
)
def test_check_area(value_a, value_b, value_c, expected):
    triangle = Triangle(value_a, value_b, value_c)
    assert triangle.area == expected


@pytest.mark.parametrize(
    ("value", "expected"),
    (
            (Circle(10), 320.2),
            (Rectangle(10, 15), 156),
            (Square(10), 106),
            (Triangle(11, 12, 15), 71.24),
    )
)
def test_check_add_area(value, expected):
    triangle = Triangle(3, 4, 5)
    assert triangle.add_area(value) == expected


def test_check_add_area_error():
    triangle = Triangle(3, 4, 5)
    with pytest.raises(ValueError):
        triangle.add_area([1, 2, 3])


def test_check_none_result():
    triangle = Triangle(3, 4, 15)
    assert triangle is None
