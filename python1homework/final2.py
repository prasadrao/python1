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

def hist_graph(wc_dict):
    """Prints out a graph with dictionary keys and values on x and y axes respectively."""
    max_count = max(wc_dict.values())
    y_scale = (round((max_count / 100)) + 1)*100 #Creating y-axis value based on max count of words for a given length
    lst_x = ["   "]*(len(wc_dict)+1)  # Create an empty list which will be used to store stars to be printed on each row, index of the list will be used as column number where star needs to be printed
    """ The below while loop will iterate over values of the input dictionary multiple times and update lst_x list with to be printed values"""
    while y_scale > 0:
        print("{0:3} -|{1}".format(y_scale,"".join(lst_x)))
        temp = y_scale
        while temp > y_scale - 100:
            for count_len in wc_dict.values():
                if count_len > temp - 20 and count_len <= temp:
                    for key_w,val_w in wc_dict.items():
                        if val_w == count_len:
                            lst_x[key_w-1] = "***"
                """Uncomment below parameter and comment above parameter to display output with count value instead of stars"""
                            #lst_x[key_w-1] = " "+str(val_w)
            print("{0:5}|{1}".format(" ","".join(lst_x)))
            temp -= 20
        y_scale -= 100
    print("{0:3} -+".format("0")+"-+-"*(len(lst_x)+1))
    print("{0:3}  | {1}".format(" ",'  '.join(str(x) for x in range(1,len(lst_x)))))

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
hist_graph(wc_dict)
