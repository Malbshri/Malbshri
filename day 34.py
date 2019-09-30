Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # week 6
>>> # day 34
>>> 
>>> def my_function(food) :
	for x in food :
		print(x)

		
>>> fruits = ["apple", "banana", "cherry"]
>>> my_function(fruits)
apple
banana
cherry
>>> 
>>> def my_function(x) :
	return 5 * x
print(my_function(3))
SyntaxError: invalid syntax
>>> print (my_function(3))
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print (my_function(3))
  File "<pyshell#6>", line 2, in my_function
    for x in food :
TypeError: 'int' object is not iterable
>>> 
>>> def my_function(x) :
	return 5*x

>>> print(my_function(3))
15
>>> print(my_function(5))
25
>>> print(my_function(9))
45
>>> 
>>> def my_function(child3, child2, child1) :
	print("The youngest child is "+ child3 )

	
>>> my_function(child1 = "Email", child2 = "Tobias", child3 = "Linus")
The youngest child is Linus
>>> 
>>> def my_function(*kids) :
	print("The youngest child is " + kids[2])

	
>>> my_function("Email", "Tobias", "linus")
The youngest child is linus
>>> 
>>> def tri_recursion(k) :
	if (k>0) :
		result = k+tri_recursion(k-1)
		print(result)
	else :
		results = 0
	return result
print("\n\nRecursion Example  Results")
SyntaxError: invalid syntax
>>> print("\n\nRecursion Example  Results")


Recursion Example  Results
>>> tri_recursion(6)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    tri_recursion(6)
NameError: name 'tri_recursion' is not defined
>>> tri_recursion (6)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    tri_recursion (6)
NameError: name 'tri_recursion' is not defined
>>> 
>>> def tri_recursion (k) :
	if (k > 0) :
		result = k+rti_recursion (k-1)
		print(result)
	else :
		result = 0
	return result

>>> print("\n\nRecursion Example Results")


Recursion Example Results
>>> tri_recursion (6)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    tri_recursion (6)
  File "<pyshell#51>", line 3, in tri_recursion
    result = k+rti_recursion (k-1)
NameError: name 'rti_recursion' is not defined
>>> 6
6
>>> 7
7
>>> 15
15
>>> 
