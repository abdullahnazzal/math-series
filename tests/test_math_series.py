from math_series import __version__
from math_series.series import fibonacci,lucas


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

def test_if_lucas_return_correctly():
    # Arrange
    n=5
    expected=17
    # Act
    actual=lucas(n)
    # Assert
    assert expected == actual