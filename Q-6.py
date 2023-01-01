'''Write a Python program to count the number of even and odd numbers from a series of numbers'''

l=[]
even = 0
odd = 0
for i in range(1,6):
    i = int(input("enter your number :"))
    l.append(i)
    if i%2==0:
        even+=1
    else:
        odd+=1
print(l,'\n'"No. of even which is present in your list : ",even,'\n'"No.of odd which is present in your list : ",odd)
