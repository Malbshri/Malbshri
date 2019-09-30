Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # week 6
>>> # day 36
>>> 
>>> def myfunc (n) :
	return lambda a : b * n

>>> mydoubler = myfunc (2)
>>> print(myfunc(11))
<function myfunc.<locals>.<lambda> at 0x03539CD8>
>>> 
>>> def myfunc (n) :
	return lambda a : b * n
mydoubler = myfunc (2)
SyntaxError: invalid syntax
>>> 
>>> def myfunc (n) :
	return lambda a : a * n

>>> mydoubler = myfunc(2)
>>> print(mydoubler(11))
22
>>> mytripler = myfunc(3)
>>> print( mytripler(11))
33
>>> 
>>> def myfunc (n) :
	return lambda a : a* n

>>> mydoubler = myfunc(2)
>>> mytripler = myfunc(3)
>>> print(mydoubler(11))
22
>>> print(mytripler(11))
33
>>> 
