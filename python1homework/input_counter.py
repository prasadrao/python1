#!/usr/local/bin/python3
words_dict = {}
words_set = set()
len_set = 0
while True:
   input_string = input("Enter text: \n")
   if not input_string:
       print("Finished")
       break
   for punc in ",?;.":
       input_string = input_string.replace(punc, "")
   for word in input_string.lower().split():
       words_set.add(word)
       if len(words_set) > len_set :
          words_dict[word] = len(words_set)
          len_set = len(words_set)
   for i,k in words_dict.items():
       print(i, k)
