#!/usr/local/bin/python3
"""Inputter program. Enter text, it is saved and shown to you when you re-run program."""

while True:
    input_string = input('Enter Text:')
    if not input_string:
        print("Good Bye")
        break
    f = open('input_stream.txt', 'a')
    f.write(input_string)
    f.close()
    f = open('input_stream.txt', 'r')
    print(f.read()) 
f.close()
