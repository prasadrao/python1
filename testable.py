#!/usr/local/bin/python3
"""Demonstrates the doctest module in action."""

def square(x):
    '''Returns the sqare of a numeric argument.

    >>> square(3)
    9
    >>> square(1000)
    1000000
    >>> square(x)
    Traceback (most recent call last):
      File "/usr/local/python34/lib/python3.4/doctest.py", line 1324, in __run
        compileflags, 1), test.globs)
      File "<doctest testable.square[2]>", line 1, in <module>
        square(x)
    NameError: name 'x' is not defined
    '''
  
    return x**2


def _test():
    import doctest, testable
    return doctest.testmod(testable)

if __name__ == "__main__":
    _test()
