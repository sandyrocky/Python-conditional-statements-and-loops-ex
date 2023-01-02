'''Write a Python program that accepts a string and calculate the number of digits and letters.'''

a = "Hello, bhai mera number hai 6395487543."
digit = 0 # digit is  vatriable ,whcich will store the digit and we use this condition statement.
alpha = 0 # alpha is variable, which will store alphabet and we use this  inside condition statement.
for x in a:
    if x.isdigit():
        digit += 1
    elif x.isalpha():
        alpha+=1
print(digit)
print(alpha)
