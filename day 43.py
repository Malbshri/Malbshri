Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # week 7
>>> # day 43
>>> 
>>> class Person :
	def __init__(self, fname, lname) :
		self.firstname = fname
		self.lastname = lname
	def printname(self) :
		print(self.firstname, self.lastname)

		
>>> # Use the Person class to creat an object , and then excute the printname metyod :
>>> x = Person("John", "Doe")
>>> x.printname()
John Doe
>>> 
>>> class Person :
	def __init__(self, fname, lname) :
		self.firstname = fname
		self.lastname = lname
	def printname(self) :
		print(self.firstname, self.lastname)

		
>>> class Student(Person) :
	pass

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
		Person.__init__(self, fname, lname)

		
>>> x = Student("Mike", "Olsen")
>>> x.printname()
Mike Olsen
>>> 
