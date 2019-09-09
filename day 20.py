Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # week 4
>>> # day 20
>>> 
>>> thisset = {}
>>> print(thisset)
{}
>>> 
>>> thisset = {"apple", "banana", "cherry"}
>>> print(thisset)
{'apple', 'cherry', 'banana'}
>>> 
>>> thisset = {"Ahmad", "Ahmad", 1, 2, 1, 5}
>>> print(thisset)
{1, 2, 5, 'Ahmad'}
>>> 
>>> thisset = {"apple", "banana", "cherry"}
>>> for x in thisset :
	print(x)

	
apple
cherry
banana
>>> 
>>> thisset = {"apple", "banana", "cherry"}
>>> print("banana" in thisset)
True
>>> 
>>> thisset = {"apple", "banana", "cherry"}
>>> thisset.add("orang")
>>> print(thisset)
{'orang', 'apple', 'cherry', 'banana'}
>>> 
>>> thisset = {"apple", "banana", "cherry"}
>>> thisset.update(["orange", "mango", "grapes"])
>>> print(thisset)
{'apple', 'mango', 'grapes', 'orange', 'banana', 'cherry'}
>>> 
