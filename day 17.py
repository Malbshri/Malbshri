Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # week 3
>>> # day 17
>>> 
>>> thistuple = ("apple", "banana", "cherry")
>>> if "apple" in thistuple :
	print("Yes, 'apple' is in thw fruits tuple")

	
Yes, 'apple' is in thw fruits tuple
>>> 
>>> thistuple = ("بايثون",)*3
>>> print(thistuple)
('بايثون', 'بايثون', 'بايثون')
>>> 
>>> 
>>> thistuple1 = (1, 2, 3, 4)
>>> thistuple2 = (5, 6)
>>> thistuple = thistuple1 + thistuple2
>>> print(thistuple)
(1, 2, 3, 4, 5, 6)
>>> 
>>> 
>>> thistuple = ("apple", "banana", "cherry")
>>> print(len(thistuple))
3
>>> 
>>> thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
>>> print(thistuple)
('apple', 'banana', 'cherry')
>>> 
>>> thislist = [3, 4, 5, 6, "A", "B"]
>>> thistuple = tuple(thislist)
>>> print(thistuple)
(3, 4, 5, 6, 'A', 'B')
>>> 
>>> # done
