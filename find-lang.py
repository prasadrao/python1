#!/usr/local/bin/python3
"""Detect any mention of several languages in the user."""

uin = input("Please enter a sentence: ")
if "pytho" in uin.lower():
    print("You mentioned Python.")
elif "perl" in uin.lower():
    print("Aha, a Perl user!")
elif "ruby" in uin.lower():
    print("SO you use Ruby, then?")
else:
    print("Didn't ese any languages there.")
