'''Write a Python program to check a triangle is equilateral, isosceles or scalene.
Note :
An equilateral triangle is a triangle in which all three sides are equal.
A scalene triangle is a triangle that has three unequal sides.
An isosceles triangle is a triangle with (at least) two equal sides.'''

# we are asking here three sides of triangle which tell us it is equilateral,isosceles or scalene.
a = int(input("enter your first side : "))
b = int(input("enter your second side : "))
c = int(input("enter your third side : "))

if a==b and b==c and c==a:# we are here equalling three sides of equilateral triangle.
    print("it is a equilateral triangle .")
elif a==b or b==c or c==a:#we are equalling here two sides here.and a is b either b is equall c or c is quall a.
    print("it is a isoscles triangle . ")
else:
    print("it is scalene triangle .")# here now both three side are not equall to each other.

'''output -
enter your first side : 2
enter your second side : 3
enter your third side : 2
it is a isoscles triangle . 
'''