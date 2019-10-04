Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # week 7
>>> # day 41
>>> 
>>> class MyClass :
	x = 5

	
>>> print(MyClass)
<class '__main__.MyClass'>
>>> 
>>> class MyClass :
	x = 5

	
>>> p1 = MyClass()
>>> print(p1.x)
5
>>> 
>>> class Person :
	def _init_(self, name, age) :
		self.name = name
		self.age = age

		
>>> p1 = Person("John", 36)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    p1 = Person("John", 36)
TypeError: Person() takes no arguments
>>> class Person :
	def __init__(self, name, age) :
		self.name = name
		self.age = age

		
>>> p1 = Person("John", 36)
>>> print(p1.name)
John
>>> print(p1.age)
36
>>> 
>>> class Person :
	def __init__(mysillyobject, name, age) :
		mysillyobject.name = name
		mysillyobject.age = age
	def myfunc(abc) :
		print("Hello my name is " + abc.name)

		
>>> p1 = Person("John", 36)
>>> p1.myfunc()
Hello my name is John
>>> 
