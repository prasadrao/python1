#!/usr/local/bin/python3
"""This program tests whether user input has given an all upper case string ending with period or not."""
print(__doc__)
user_input=input("Please enter a string: ")
if user_input.isupper() and user_input.endswith("."):
    print("Input meets both requirements.")
elif not user_input.isupper() and user_input.endswith("."):
    print("Not all user input is in uppercase.")
elif not user_input.isupper() and not user_input.endswith("."):
    print ("Not all user input is in upper case.\nInput does not end with period.")
elif user_input.isupper() and not user_input.endswith("."):
    print("Input does not end with period.")
