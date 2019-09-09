Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # week 4
>>> # day 21
>>> 
>>> thisset = {"apple", "banana", "cherry"}
>>> print(len(thisset))
3
>>> 
>>> thisset = {"apple", "banana", "cherry"}
>>> thisset.remove("banana")
>>> print(thisset)
{'apple', 'cherry'}
>>> 
>>> thisset = {"apple", "banana", "cherry"}
>>> thisset.descard("banana")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    thisset.descard("banana")
AttributeError: 'set' object has no attribute 'descard'
>>> thisset.discard("banana")
>>> print(thisset)
{'apple', 'cherry'}
>>> 
>>> thisset = {"apple", "banana", "cherry"}
>>> x = thisset.pop()
>>> print(x)
apple
>>> print(thisset)
{'banana', 'cherry'}
>>> 
>>> thisset = {"apple", "banana", "cherry"}
>>> thisset.clear()
>>> print(thisset)
set()
>>> 
>>> thisset = {"apple", "banana", "cherry"}
>>> del thisset
>>> print(thisset)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(thisset)
NameError: name 'thisset' is not defined
>>> 
>>> thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
>>> print(thisset)
{'apple', 'banana', 'cherry'}
>>> 
