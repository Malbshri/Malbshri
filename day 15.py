Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>  # week 3
>>> # day 15
>>> 
>>> thislist = ["apple", "banana", "cherry"]
>>> print(len(thislist))
3
>>> thislist.append("orange")
>>> print(thislist)
['apple', 'banana', 'cherry', 'orange']
>>> 
>>> thislist.insert(1, "orange")
>>> print(thislist)
['apple', 'orange', 'banana', 'cherry', 'orange']
>>> 
>>> thislist = ["apple", "banana", "cherry"]
>>> thislist.remove("banana")
>>> print(thislist)
['apple', 'cherry']
>>> 
>>> thislist = ["apple", "banana", "cherry"]
>>> thislist.pop()
'cherry'
>>> print(thislist)
['apple', 'banana']
>>> 
>>> thislist = ["apple", "banana", "cherry"]
>>> thislist.clear()
>>> print(thislist)
[]
>>> thislist = ["apple", "banana", "cherry"]
>>> mylist = thislist.copy
>>> print(mylist)
<built-in method copy of list object at 0x00F1AFA8>
>>> thislist = ["apple", "banana", "cherry"]
>>> mylist = thislist.copy()
>>> print(mylist)
['apple', 'banana', 'cherry']
>>> 
>>> 
>>> thislist = ["Ahmad", "Omar", "Khaled"]
>>> mylist = thislist.copy()
>>> thislist.pop(0)
'Ahmad'
>>> print(mylist)
['Ahmad', 'Omar', 'Khaled']
>>> print(thislist)
['Omar', 'Khaled']
>>> 
>>> thislist = ["Ahmad", "Khaled", "Omar"]
>>> mylist = thislist
>>> thislist.pop(0)
'Ahmad'
>>> print(mylist)
['Khaled', 'Omar']
>>> print(thislist)
['Khaled', 'Omar']
>>> 
>>> thislist = ["apple", "banana", "cherry"]
>>> mylist = list(thislist)
>>> print(mylist)
['apple', 'banana', 'cherry']
>>> 
>>> thislist = list(("apple", "banana", "cherry")) # not the double round-brackets
>>> pirnt(thislist)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    pirnt(thislist)
NameError: name 'pirnt' is not defined
>>> print(thislist)
['apple', 'banana', 'cherry']
>>>
