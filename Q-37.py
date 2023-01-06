'''Write a Python program that reads two integers representing a month and day and
 prints the season for that month and day'''
# c is month
c = input("enter your month name : ")
d = c.capitalize()
# if someone write here month name in small letter this method convert in first letter in capital format.

a = str(input("enter your day in number "))
# a is day we are asking here from the users.
g = int(a[0:2])
print(g)


if d in ("Januaury","Feb","March") and g>15 or g<15:
    print("winter season")
elif d in ("April","May","June") and g>15 or g<15:
    print("summer season")
elif d in ("July","August","September") and g>15 or g<15:
    print("raining season")
else:
    print("Autumn")


