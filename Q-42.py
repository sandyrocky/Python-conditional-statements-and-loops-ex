'''Write a Python program to calculate the sum and average of n integer numbers (input from the user).
 Input 0 to finish'''

n = int(input("enter your number  : "))

sum = 0# we initial this variable to add the  n number integer sum here.
av=0# this variable give us averge of n integer number.
for i in range(1,n+1):# we strating here range from 1 to n+1. if remove the 1 form starting values it gives us error that error is division by zero.
    print(i,end=" ")
    sum+=i# when the loop iterate its number that number will add here and store in this variable .
    av=sum/n#when you have sum of total number then divided the sum by n. n is number when we ask you from input function.

print(" ")
print("sum of n integer number is  ",sum)
print("Average of n number is ",av)


'''output -
enter your number  : 10
1 2 3 4 5 6 7 8 9 10  
sum of n integer number is   55
Average of n number is  5.5
'''