Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # week 7
>>> # day 42
>>> 
>>> class Person :
	def __init__(self, name, age ) :
		self.name = name
		self.age = age
	def myfunc(self) :
		print("Hello my name is" + self.name)

		
>>> p1 = Person("John", 36)
>>> p1.myfunc()
Hello my name isJohn
>>> 
>>> p1.age = 40
>>> print(pq.age)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(pq.age)
NameError: name 'pq' is not defined
>>> print(p1.age)
40
>>> 
>>> class Person :
	def __init__(self, name, age ) :
		self.name = name
		self.age = age
	def myfunc(self) :
		print("Hello my name is" + self.name)

		
>>> p1 = Person("John", 36)
>>> del p1.age
>>> print(p1.age)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print(p1.age)
AttributeError: 'Person' object has no attribute 'age'
>>> 
>>> class Person :
	def __init__(self, name, age ) :
		self.name = name
		self.age = age
	def myfunc(self) :
		print("Hello my name is" + self.name)

	
>>> p1 = Person("John", 36)
>>> del p1
>>> print(p1)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(p1)
NameError: name 'p1' is not defined
>>> 
