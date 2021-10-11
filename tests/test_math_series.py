from math_series import __version__
from math_series.series import fibonacci


def test_version():
    assert __version__ == '0.1.0'

def test_if_fibonacci_return_correctly():
    # Arrange
    n=5
    expected=7
    # Act
    actual=fibonacci(n)
    # Assert
    assert expected == actual

