Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # week 4
>>> # day 25 & 26
>>> 
>>> #PART 1
>>> 
>>> box = {1, 3, 5, 7, 8}
>>> box.update([1,2,3])
>>> print(box)
{1, 2, 3, 5, 7, 8}
>>> box.remove(8)
>>> print(box)
{1, 2, 3, 5, 7}
>>> box.clear()
>>> print(box)
set()
>>> 
>>> 
>>> 
>>> #PART 2
>>> x = {'name' : 'pigeon' , 'type' : 'bird' , 'skin cover ' : ' feathers'}
>>> print(x['type'])
bird
>>> x['skin cover '] = 'ubuntu'
>>> print(x['skin cover'])
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print(x['skin cover'])
KeyError: 'skin cover'
>>> print(x['skin cover '])
ubuntu
>>> 
