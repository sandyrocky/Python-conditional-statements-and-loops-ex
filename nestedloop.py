''' Write a Python program to construct the following pattern, using a nested for loop.'''

for i in range(1,5):# first we set range which is going to 1to5.first loop gives us row
    for j in range(1,i+1):#second loop gives us column
        print('*',end=" ")
    print()

for i in range(5,0,-1):# we are revesing here loop values
    for j in range(1,i-1):
        print('*',end=" ")
    print()


'''output -
* 
* * 
* * * 
* * * * 
* * * 
* * 
* 
'''