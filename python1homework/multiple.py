#!/usr/local/bin/python3
"""Display multiples tables"""
tup1 = ((1,1),(2,2),(12,13),(4,4),(99,98))
for a,b in tup1:
    print("{2:>5d} = {0:>2d} x {1:>2d}".format(a, b, a*b))
