Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # week 5
>>> # day 31
>>> 
>>> def my_function() :
	print("Hello from a function")

	
>>> my_function()
Hello from a function
>>> 
>>> def my_function(fname) :
	print(fname + " Refsens ")

	
>>> my_function("Email")
Email Refsens 
>>> my_function("Tobias")
Tobias Refsens 
>>> my_function("linus")
linus Refsens 
>>> 
>>> def my_function (country = "Norway") :
	print("I am from " + country)

	
>>> my_function("Sweden")
I am from Sweden
>>> my_function("India")
I am from India
>>> my_function()
I am from Norway
>>> my_function("Brazil")
I am from Brazil
>>> 
