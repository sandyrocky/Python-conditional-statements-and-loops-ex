''' Write a Python program to find the median of three values.'''

a=eval(input("enter your value 1 : "))
b=eval(input("enter your value 2 : "))
c=eval(input("enter your value 3 : "))
if a<b and a<c:
    print("your medain value is ",a)
elif b>c and b>a:
    print("your median value is ",b)
else:
    print("your median value is ",c)