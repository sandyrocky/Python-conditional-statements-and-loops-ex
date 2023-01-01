'''Write a Python program to guess a number between 1 to 9'''

import random as rd


a = int(input("enter your number for guessing :"))

if a == rd.randint(1, 10):
    print("yes you have got your guess number.")
    print("thank you sir, you gave us precise time.")
else:
    print("this is not your guessing number,please try agian.")
