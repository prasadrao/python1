#!/usr/local/bin/python3
""" Program takes integer and returns value which is result of 10 divided by integer. """

def div_ten(a):
    try:
       return print(10/int(a))
    except ValueError:
           print("Your input must be an integer!")
    except ZeroDivisionError:
           print("Your input can not be zero!")
    except Exception as msg:
           print("Problem: {0}".format(msg))

while True:
    input_num = input("Provide an integer or Press ENTER to exit: ")
    if not input_num:
        print("Good bye for now!")
        break
    div_ten(input_num)
