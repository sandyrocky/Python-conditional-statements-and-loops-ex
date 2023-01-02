'''Write a Python program which iterates the integers from 1 to 50.
 For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".'''

# we created two variable to variable and assign value Fizz and Buzz
a="Fizz"
b="Buzz"
# then we put for loop here set the range 1 to 50
for i in range(1,50):
    if i%3==0 and i%5==0:# and we applied  condition here if any number which is divisble 3 and 5 then print FizzBuzz.
        print(a+b)
    elif i%3==0:# and if any number wchich is divisible by 3 then print Fizz.
        print(a)
    elif i%5==0:# and if any number which is dividible by 5 then print Buzz.
        print(b)
    else:
        print(i)#otherwise print loops values.

'''output -
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
FizzBuzz
46
47
Fizz
49'''
