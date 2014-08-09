#!/usr/local/bin/python3
"""Count the words, lines and character in a chunk of test."""

gettysburg = """\
Four score and seven years ago our
fathers brought forth on this continent,
a new nation, conceived in Liberty, and 
dedicated to the proposition that 
all men are created equal.

Now we are engaged in a great civil war,
testing whether that nation, or 
any nation so conceived and so dedicated,
can long endure. We are met on
a great battle-field of that war. We have 
come to deicate a portion of that
field, as a final resting place for those 
who her gave their lives that that
nation might live. It is altogether
fitting and proper that we should do this deinstitutionalizing
deinstitutionalizingafdaf. """

lengthct = [0]*20 # al list of 20 zeroes
charct = len(gettysburg)

lines = gettysburg.split("\n")
linect = len(lines)

wordct = 0
whole_words = [] #initiate empty list
for line in lines:
    words = line.split()
    whole_words = whole_words + words
    wordct += len(words)
    for word in words:
        if not lengthct[len(word)]:
            lengthct[len(lengthct):len(word)+1] = [0]*len(word)
        lengthct[len(word)] += 1

print("The text contains", linect, "lines,", wordct, "words, and", charct, "characters.")
for i, ct in enumerate(lengthct):
    if ct:
        print("Length", i, ":", ct)
for i in set(whole_words):
    print(i,":",whole_words.count(i))
