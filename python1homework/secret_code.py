#!/usr/local/bin/python3

msg = ""
out_put = ""
user_input = input("Enter Message:")
for i in str(user_input):
    c = ord(i)
    msg += chr(c  + 1)
for i in reversed(msg):
    out_put += i
print(out_put)
