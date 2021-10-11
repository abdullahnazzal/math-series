from math_series import __version__
from math_series.series import fibonacci,lucas,sum_series


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



def test_if_sum_series_return_correctly_1():
    # Arrange
    n=5
    x=0
    y=1
    expected=7
    # Act
    actual=sum_series(n,x,y)
    # Assert
    assert expected == actual

def test_if_sum_series_return_correctly_2():
    # Arrange
    n=5
    x=2
    y=1
    expected=17
    # Act
    actual=sum_series(n,x,y)
    # Assert
    assert expected == actual