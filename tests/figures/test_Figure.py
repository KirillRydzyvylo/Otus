import pytest
from src.Figure import Figure, UnusableObjectError


def test_figure():
    with pytest.raises(UnusableObjectError):
        Figure()
