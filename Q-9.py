'''Write a Python program to get the Fibonacci series between 0 to 50. '''

# whenever we need to create a fibonacci series that time we need to create two variable .
# and we need to assign the value for first variable is 0 and second variable is 1.
# we should know about the unpacking and packing varible.
# we are taking here two variable which is unpacking variable
a,b=0,1 # assign value for a is 0. and for b assign value is 1
for i in range(0,50): # we use for loop with range function and we are taking range here 0 t0 50.
# then we are not calling here for loop
# a,b = b, b+a means a is variable. it will take the value of b  first then b take the value a+b and so on

    a,b = b, b+ a

    if i<9:# we put here condition if i is less than 9
      print(a,end=" ")#then print here a and our output will come

#output - 1 1 2 3 5 8 13 21 34


