Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>   #week 3
>>> # day16
>>> 
>>> thistuple = ("apple ", "banana", "cherry")
>>> print(thistuple)
('apple ', 'banana', 'cherry')
>>> 
>>> thistuple = ()
>>> print(thistuple)
()
>>> thistuple = (3,)
>>> print(thistuple)
(3,)
>>> 
>>> thistuple = (3, 1.3, 4.1, 7)
>>> print(thistuple)
(3, 1.3, 4.1, 7)
>>> 
>>> thistuple = ("Ahmad", 1.1, 4, "بايثون")
>>> print(thistuple)
('Ahmad', 1.1, 4, 'بايثون')
>>> 
>>> thistuple = ("apple ", "banana", "cherry")
>>> print(thistuple[1])
banana
>>> thistuple = ("apple ", "banana", "cherry")
>>> for x in thistuple :
	print(x)

	
apple 
banana
cherry
>>> 
>>> thistuple = ("apple ", "banana", "cherry")
>>> thistuple[3] = "orange" # this will raise an error
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    thistuple[3] = "orange" # this will raise an error
TypeError: 'tuple' object does not support item assignment
>>> print(thistuple)
('apple ', 'banana', 'cherry')
>>> 
>>> thistuple = ("apple ", "banana", "cherry")
>>> del thistuple
>>> print(thstiple) # this will raise an error because the tuple no longer exists
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    print(thstiple) # this will raise an error because the tuple no longer exists
NameError: name 'thstiple' is not defined
>>> 
>>> thistuple = ("apple ", "banana", "cherry", "orange")
>>> print(thistuple[0:3])
('apple ', 'banana', 'cherry')
>>> 
 
