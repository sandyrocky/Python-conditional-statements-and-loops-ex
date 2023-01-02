'''Write a Python program to sum of two given integers.
However, if the sum is between 15 to 20 it will return 20.'''

a = int(input("Enter your number first: "))
b = int(input("Enter your number second :"))
c = a+b
d =20
if c>=15 and c<=20:
    print(d)
else:
    print(c)
