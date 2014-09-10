#!/usr/local/bin/python3
"""Takes input string and prints out list of words in such a order that words with upper case letters are printed first and then other words."""

user_line = input("Enter a string: ")
all_words = user_line.split()
l_words = []   #empty list for lower case words
u_words = []   #empty list for other words

for i in all_words:
    if i.islower():
        l_words.append(i)
    else:
        u_words.append(i)

for i in u_words + l_words:
    print(i)
