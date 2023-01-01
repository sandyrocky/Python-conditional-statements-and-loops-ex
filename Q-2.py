'''Write a Python program to convert temperatures to and from celsius, fahrenheit.'''

'what is the formula of temperature to change celsius into fahrenheit'
'fahrenheit = celcius*(9/5)+32'
# we created a  variable  to store the temperature value in "a"
a = (input("enter your temperature in celsius : "))
#  a variable  take the value in string format and this format string we need to change in integer
# because our formula take integer value ya phir hum kahe apna math number par kamm karta hai bhai
# baki ka chutiyapa karne ki zarurat nahi ismai.
b = int(a[0:2])# ismai hum b variable mai value store kare gye aur a variable se value ko le gaye
# aur yaha pe humnae a[0:2] matlab agar hum jayada string ke character dalae gayeto ye sirf 2 place ki value lega.
# we creted a varible to store the formula of fahrenheit temp.
f = (b*(9/5))+32
print("")
print("temperature in fahrenheit : ",f)

# output - enter your temperature in celsius : 45
#
# temperature in fahrenheit :  113.0
