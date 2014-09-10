#!/usr/local/bin/python3
"""Prints a table showing the word count for each of the word lengths in a given file"""
import sys

def word_len(text):
    """Counts length of a word excluding any punctuation marks"""
    w_len = 0
    alph_lst = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in text:
        if i.lower() in alph_lst:
            w_len += 1
    return w_len

try:
    text_file = open(sys.argv[1], 'r')

except FileNotFoundError:
    print("File NOT FOUND: {0} ".format(sys.argv[1]))
    sys.exit()

except IndexError:
    print("Missing input file! Please provide file as an argument")
    sys.exit()

words_lst = []
wc_dict = {}

for i in text_file.readlines():
    words_lst = words_lst + i.split()

for w in words_lst:
    wc_dict[word_len(w)] = wc_dict.get(word_len(w), 0) + 1

del wc_dict[0]

print("{0:>10}  {1:>10}".format("Length","Count"))

for j,k in wc_dict.items():
    print("{0:10}  {1:10}".format(j,k))

text_file.close()
