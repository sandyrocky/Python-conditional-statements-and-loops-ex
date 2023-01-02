'''  Write a Python program to check a string represent an integer or not. '''

a = input("enter what you want to : ")

if a.isdigit():
    print("this string is integer .",a)
else:
    print("This string is not integer .",a)