import pytest
from main import *


# Test the calc function
# noinspection PyTypeChecker
def test_calc():
    assert calc(2, 3, '+') == 5
    assert calc(2, 3, '-') == -1
    assert calc(2, 3, '*') == 6
    assert calc(2, 3, '/') == 0.6666666666666666
    assert calc(2, 3, '+') == 5
    assert calc(2, 3, '-') == -1
    
    with pytest.raises(ValueError):
        calc(2, 3, '2')
    with pytest.raises(TypeError):
        calc('2', 3, '+')
    with pytest.raises(TypeError):
        calc(2, '3', '+')
    with pytest.raises(ValueError):
        calc(2, 3, 'invalid_operator')
    with pytest.raises(ZeroDivisionError):
        calc(2, 0, '/')


# Test the newton_method function
def test_newton_method():
    def f(x):
        return x ** 2 - 4
    
    def df(x):
        return 2 * x
    
    assert newton_method(f, df, 2) == pytest.approx(2, rel=1e-6)
    
