#!/usr/local/bin/python3

import sys

def capitalize(text):
    return text.capitalize()

def title(text):
    return text.title()

def lower(text):
    return text.lower()

def upper(text):
    return text.upper()

def exit():
    """Terminates the program"""
    print("Good bye for now.")
    sys.exit()

str_func = { 
    'capitalize' : capitalize,
    'title' : title,
    'upper' : upper,
    'lower' : lower,
    'exit'  : exit
     }

while True:
      func = input("Enter a function name ( {0} ) : ".format(', '.join(str_func.keys())))
      if func == "exit":
         str_func[func]()
      inp_str = input("Enter a string: ")
      print(str_func[func](inp_str))
