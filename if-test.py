#!/usr/local/bin/python3
"""Detect any mention of Python in the user's input."""

uin = input("Please enter a sentence: ")
if "python" in uin.lower():
    print("You menitoned Python.")
else:
    print("Didn't see Python there.")
