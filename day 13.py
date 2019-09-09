Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>  # week 3
>>> # day 13
>>> # Create a List
>>> 
>>> s=[]
>>> print(s)
[]
>>> 
>>> numbers = [1, 2, 3, 4, 5]
>>> print(numbers)
[1, 2, 3, 4, 5]
>>> 
>>> thislist = ["aplle", "banana", "cherry"]
>>> print(thislist)
['aplle', 'banana', 'cherry']
>>> thislist = ["apple", "banana", "cherry", 1, 2, 3]
>>> print(thislist)
['apple', 'banana', 'cherry', 1, 2, 3]
>>> 
>>> # Access Items
>>> 
>>> thislist = ["aplle", "banana", "cherry"]
>>> print(thislist[1])
banana
>>> thislist = ["aplle", "banana", "cherry"]
>>> for x in thislist :
	print(x)

	
aplle
banana
cherry
>>> # Chang Iteam Value
>>> 
>>> thislist = ["apple", "banana", "cherry"]
>>> thislist[1] = "blackcurrant"
>>> print(thislist)
['apple', 'blackcurrant', 'cherry']
>>> 
>>> thislist = ["apple", "banana", "cherry"]
>>> del thislist[0]
>>> print(thislist)
['banana', 'cherry']
>>> dil thislist
SyntaxError: invalid syntax
>>> 
>>> 
>>> thislist = ["A", "B", "C", "D", "E"]
>>> del thislist[0]
>>> print(thislist)
['B', 'C', 'D', 'E']
>>> del thislist[0]
>>> del thislist[1]
>>> print(thislist)
['C', 'E']
>>> #done
SyntaxError: invalid syntax
>>> 
