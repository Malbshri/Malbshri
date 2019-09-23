Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # week 5
>>> # day 29
>>> 
>>> fruits = ["apple",  "banana", "cherry"]
>>> for x in fruits :
	print(x)

	
apple
banana
cherry
>>> 
>>> for x in "banana" :
	print(x)

	
b
a
n
a
n
a
>>> 
>>> fruits = ["apple",  "banana", "cherry"]
>>> for x in fruits :
	print(x)
	if x == "banana" :
		break

	
apple
banana
>>> 
>>> fruits = ["apple",  "banana", "cherry"]
>>> for x in fruits :
	if x == "banana" :
		break
	print(x)

	
apple
>>> 
>>> fruits = ["apple",  "banana", "cherry"]
>>> for x in fruits :
	if x == "banana" :
		continue
	print(x)

	
apple
cherry
>>> 
