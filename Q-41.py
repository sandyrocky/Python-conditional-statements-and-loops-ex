"""write a python program to get next day of given date."""

year=int(input("enter your year : "))
if year%400==0 or year%100==0 or year%4==0:
    print(year,"it is leap year")

else:
    print("it is not leap year . ")

month=int(input("enter your month in number : "))

if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    day = (input("enter your day in number something like 1 or 2  : "))
    s = str(day[:2])
    d = int(s)

    if d < 31:
        d = d + 1

elif month==2:
    day = (input("enter your day in number something like 1 or 2  : "))
    s = str(day[:2])
    d = int(s)

    if d < 29:
        d = d - 1


elif month==4 or month==6 or month==9 or month==11:
    day = (input("enter your day in number something like 1 or 2  : "))
    s = str(day[:2])
    d = int(s)

    if d > 31:
        d = d - 1


print("the next date is yyyy/mm/day : ",year,"/",month,"/",d)



