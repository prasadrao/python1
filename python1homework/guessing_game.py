#!/usr/local/bin/python3
import random
number = random.randint(0,99)

print(number)
def check_num(guess):
     if guess == number:
        return "break"
     if guess < number:
        return "Too low"
     if guess > number:
        return "Too high"

while True:
      input_number = input("Guess a number: ")
      if not input_number :
          break
      val = check_num(int(input_number))
      if val == "break":
          print("You guessed it!")
          break
      else:
          print(val)

