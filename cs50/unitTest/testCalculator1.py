# pytest is a third-party library that allows you to unit test your program.
# That is, you can test your functions within your program.
# To utilize pytest please type ' pip install pytest ' into your console window.

from calculator import square


def testPositive():
    assert square(2) == 4
    assert square(3) == 9

def testNegative():
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(-4) == 16

def testZero():
    assert square(0) == 0


import pytest

def testStr():
    with pytest.raises(TypeError):
        square("cat")

"""
Notice that instead of using assert, we are taking advantage of a function within the pytest library itself called raises which allows you to express that you expect an error to be raised.
We need to go to the top of our program and add import pytest and then call 'pytest.raises' with the type of error we are expecting. """
