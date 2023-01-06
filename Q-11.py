'''Write a Python program that prints each item and its corresponding type from the following list.
Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12],
{"class":'V', "section":'A'}]'''

# we are creating here a list and list name is a.

a = [1452,11.23,1+2j,True,'sandeep',(0,-1),[4,8],{'class':'v','section':'A'}]
for x in a:
    print(x,type(x))

'''output -
1452 <class 'int'>
11.23 <class 'float'>
(1+2j) <class 'complex'>
True <class 'bool'>
sandeep <class 'str'>
(0, -1) <class 'tuple'>
[4, 8] <class 'list'>
{'class': 'v', 'section': 'A'} <class 'dict'>
'''