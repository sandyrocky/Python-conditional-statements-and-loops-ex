'''Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as
 its input
and print the
numbers that are divisible by 5 in a comma separated sequence.'''

l = []
a = input("enter your number")
for i in a:
    s = int(i)
    print(s)
    if s % 5 == 0:
        b = bin(s)
        l.append(b)

print(l)

'''output -
enter your number55
5
5
['0b101', '0b101']
'''