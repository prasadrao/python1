#!/usr/local/bin/python3
"""Program to locate the first space in the input string."""

s = input("Please enter a string: ")
pos = 0
for c in s:
    if c == " ":
        print("First space occurred at position", pos)
        break
    pos += 1
else:
    print("No spaces found")
