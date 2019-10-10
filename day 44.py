Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # week 7	# day 44
>>> 
>>> class Person :
	def __init__(self, fname, lname) :
		self.firstname = fname
		self lastname = lname
		
SyntaxError: invalid syntax
>>> class Person :
	def __init__(self, fname, lname) :
		self.firstname = fname
		self.lastname = lname
	def printname(self) :
		print(self.firstname, self.lastname)

		
>>> class Student(Person) :
	def __init__(self, fname, lname) :
		super().__init__(fname, lname)

		
>>> x = Student("Mike", "Olsen")
>>> x.printname()
Mike Olsen
>>> 
>>> class Person :
	def __init__(self, fname, lname) :
		self.firstname = fname
		self.lastname = lname
	def printname(self) :
		print(self.firstname, self.lastname)

		
>>> class Student(Person) :
	def __init__(self, fname, lname) :
		super().__init__(fname, lname)
		
SyntaxError: invalid syntax
>>> 
>>> class Person :
	def __init__(self, fname, lname) :
		self.firstname = fname
		self.lastname = lname
	def printname(self) :
		print(self.firstname, self.lastname)

		
>>> class Student(Person) :
	def __init__(self, fname, lname) :
		syper().__init__(fname, lname )
		self.graduationyear = 2019

		
>>> x = Student("Mike", "Olsen")
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    x = Student("Mike", "Olsen")
  File "<pyshell#25>", line 3, in __init__
    syper().__init__(fname, lname )
NameError: name 'syper' is not defined
>>> class Student(Person) :
	def __init__(self, fname, lname) :
		super().__init__(fname, lname )
		self.graduationyear = 2019

		
>>> x = Student("Mike", "Olsen")
>>> print(x.graduationyear)
2019
>>> 
>>> 
>>> 
>>> class Person :
	def __init__(self, fname, lname) :
		self.firstname = fname
		self.lastname = lname
	def printname(self) :
		print(self.firstname, self.lastname)

		
>>> class Student(Person)
SyntaxError: invalid syntax
>>> class StudenT(Person) :
	def __init__(self, fname, lname, year ) :
		super().__init__(fname, lname)
		self.graduationyear = year
	def welcome(self) :
		print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

		
>>> x = Student("Mike", "Olsen", 2019)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    x = Student("Mike", "Olsen", 2019)
TypeError: __init__() takes 3 positional arguments but 4 were given
>>> x = ("Mike", "Olsen", 2019 )
>>> x.welcome()
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    x.welcome()
AttributeError: 'tuple' object has no attribute 'welcome'
>>> x.Wilcome()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    x.Wilcome()
AttributeError: 'tuple' object has no attribute 'Wilcome'
>>> x = Student( "Mike", "Olsen", 2019 )
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    x = Student( "Mike", "Olsen", 2019 )
TypeError: __init__() takes 3 positional arguments but 4 were given
>>> x = Student("Mike", "Olsen", 2019 )
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    x = Student("Mike", "Olsen", 2019 )
TypeError: __init__() takes 3 positional arguments but 4 were given
>>> x = Student("Mike", "Olsen", 2019)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    x = Student("Mike", "Olsen", 2019)
TypeError: __init__() takes 3 positional arguments but 4 were given
>>> print(x)
('Mike', 'Olsen', 2019)
>>> x.graduation()
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    x.graduation()
AttributeError: 'tuple' object has no attribute 'graduation'
>>> 
>>> 
>>> 
>>> class Person :
	def __iniy__(self, fname, lname) :
		self.firstname = fname
		self.lastname = lname
	def printname(self) :
		print(self.firstname, self.lastname)

		
>>> class Student(Person) :
	def __init__(self, fname, lname, year) :
		super().__init__(fname, lname)
		self.graduationyear = year
	def welcome(self) :
		print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

		
>>> x = Student("Mike", "Olsen", 2019)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    x = Student("Mike", "Olsen", 2019)
  File "<pyshell#70>", line 3, in __init__
    super().__init__(fname, lname)
TypeError: object.__init__() takes exactly one argument (the instance to initialize)
>>> x.welcome()
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    x.welcome()
AttributeError: 'tuple' object has no attribute 'welcome'
>>> 
>>> 
>>> class Person :
	def __init__(self, fname, lname) :
		self.firstname = fname
		self.lastname = lname
	def printname(self) :
		print(self.firstname, self.lastname)

		
>>> class Student(Person) :
	def __init__(self, fname, lname, year) :
		super().__init__(fname, lname)
		self.graduationyear = year
	def welcome(self) :
		print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

		
>>> x = Student("Mike","Olsen", 2019)
>>> x.welcome()
Welcome Mike Olsen to the class of 2019
>>> 
