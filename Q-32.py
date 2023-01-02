'''Write a Python program to check whether an alphabet is a vowel or consonant.'''

a = input("Enter your alphabet : ")
vowel= "a","i","o","u","e"
if a in vowel  :
    print("This alphabet is",a ,",is vowel.")
else:
    print("This is ",a,"consonant.")

