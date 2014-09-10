#!/usr/local/bin/python3

def my_func(a, b = "b was not entered", c = "c was not entered"):
    """ Prints current a,b and c values."""
    print(a+"\n"+b+"\n"+c)

my_func("test")
my_func("test","test")
my_func("test","test","test")
print(my_func)
