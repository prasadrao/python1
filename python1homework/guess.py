#!/usr/local/bin/python3
"""Program to find if user can guess our secret number. If so in how many chances. Maximum number of chances per turn is 5."""
print(__doc__)
secret = 18
count = 0

while True:
    if count > 4:
       print("Sorry! You have reached maximum attempts") 
       break
    guess = input("Please enter your guess number: ")
    guess = int(guess)
    if guess > secret:
       print("Guess a lower number")
       count += 1
       continue
    elif guess < secret:
       print("Guess a higher number")
       count += 1
       continue
    elif guess == secret:
       print("Correct! Well done, the number was", secret)
       break
