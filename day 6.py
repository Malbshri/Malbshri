Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>   # week 2
>>> # day 6
>>> 
>>> x = int(1)    # x will be 1
>>> y = int(2.8)  # y will be 2
>>> z = int("3")  # z will be 3
>>> pirnt(x)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    pirnt(x)
NameError: name 'pirnt' is not defined
>>> print(x)
1
>>> print(y)
2
>>> print(z)
3
>>> 
>>> 
>>> x = float(1)      # x will be 1.0
>>> y = float(2.8)    # y will be 2.8
>>> z = float("3")    # z will be 3.0
>>> w = float(("4.2") # w will be 4.2
>>> print(x)
	  
SyntaxError: invalid syntax
>>> print(x)
1.0
>>> print(y)
2.8
>>> print(z)
3.0
>>> print(w)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(w)
NameError: name 'w' is not defined
>>> print(w)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(w)
NameError: name 'w' is not defined
>>> w = float("4.2")
>>> print(w)
4.2
>>> 
>>> 
>>> x = str("s1")       # x will be 's1'
>>> y = str(2)          # y will be '2'
>>> z = str(3.0)        # z will be '3.0'
>>> print(x)
s1
>>> print(y)
2
>>> print(z)
3.0
>>> # done
