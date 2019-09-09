Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>   # week 2
>>> # day 9
>>> 
>>> age = 36
>>> txt = " My name is John, I am " + age
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    txt = " My name is John, I am " + age
TypeError: can only concatenate str (not "int") to str
>>> txt = " My name is John, I am  {} "
>>> print(age)
36
>>> 
>>> quantity = 3
>>> itemno = 567
>>> price = 49.95
>>> myorder = " I want {} pieces of item {} for {} dollars. "
>>> print(myorder.forms(quantitiy, itemno, price))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(myorder.forms(quantitiy, itemno, price))
AttributeError: 'str' object has no attribute 'forms'
>>> myorder = " I want to pay {2} dollars for {0} pieces of item {1}. "
>>> print(myorder.format(quantity, itemno, price))
 I want to pay 49.95 dollars for 3 pieces of item 567. 
>>> 
