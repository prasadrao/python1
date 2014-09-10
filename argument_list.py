#!/usr/local/bin/python3
def multiplier(total = 0.0,*args):
    """ Multiply the arguments together, add a prior total and return the result.
        Return 0 if nothing is provided.
    """
    if not args:
        return total
    product = args[0]
    for a in args[1:]:
        product *= a
    return product + total

print(multiplier.__doc__)

print(multiplier())
print(multiplier(1,2,3,4))
print(multiplier(6,7,8,9,10,11,12,13))
print(multiplier(10,20,100))
