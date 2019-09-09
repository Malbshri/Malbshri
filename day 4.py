Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>  # week 1
>>> # day 4
>>> 
>>> x = 1      # int
>>> y = 2.8    # float
>>> z= 1j      # complex
>>> print(tpye(x))
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    print(tpye(x))
NameError: name 'tpye' is not defined
>>> print(type(x))
<class 'int'>
>>> print(type(y))
<class 'float'>
>>> print(type(z))
<class 'complex'>
>>> 
>>> 
>>> x = 1
>>> y = 236485676445
>>> z = -22345432
>>> print(type(x))
<class 'int'>
>>> print(type(y))
<class 'int'>
>>> print(type(z))
<class 'int'>
>>> 
>>> x = 1.10
>>> y = 1.0
>>> z = -35.59
>>> 
>>> print(type(x))
<class 'float'>
>>> print(type(y))
<class 'float'>
>>> print(type(z))
<class 'float'>
>>> 
>>> x = 45e3
>>> y = 12E4
>>> z = -87.7e100
>>> print(type(x))
<class 'float'>
>>> print(type(y))
<class 'float'>
>>> print(type(z))
<class 'float'>
>>> 
>>> x = 3+5j
>>> y = 5j
>>> z = -5j
>>> print(type(x))
<class 'complex'>
>>> print(type(y))
<class 'complex'>
>>>  print(type(z))
 
SyntaxError: unexpected indent
>>> print(type(z))
<class 'complex'>
>>> 
>>> 
>>> 
>>> x = 1    # int
>>> y = 2.8  # float
>>> z= 1j    # complex
>>> #convert frome int to float:
>>> a = float(x)
>>> #convert from cfloat to int:
>>> b = int(y)
>>> #convert from int to complex:
>>> c = complex(x)
>>> 
>>> print(a)
1.0
>>> print(b)
2
>>> print(c)
(1+0j)
>>> 
>>> print(type(a))
<class 'float'>
>>> print(type(b))
<class 'int'>
>>> print(type(c))
<class 'complex'>
>>> 
>>> 
>>> impoort random
SyntaxError: invalid syntax
>>> import random
>>> print(random.randrang(1,10))
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    print(random.randrang(1,10))
AttributeError: module 'random' has no attribute 'randrang'
>>> print(random.randrang(1,10))
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    print(random.randrang(1,10))
AttributeError: module 'random' has no attribute 'randrang'
>>> 
>>> import random
>>> print(random.randrange(1,10))
9
>>> 
>>> # done
