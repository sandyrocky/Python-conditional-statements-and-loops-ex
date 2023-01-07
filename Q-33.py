'''Write a Python program to convert month name to a number of days.'''

month_name=input("Enter your month : ")

if month_name in ('january','march','may','july','august','october','december'):
    print('day in this month',month_name,'31')
elif month_name in('april','june','september','november'):
    print('day in month',month_name,'30')
else:
    print('day in this month',month_name,'28/29')

'''output -
Enter your month : january
day in this month january 31
'''