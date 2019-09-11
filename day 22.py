Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # week 4
>>> # day 22
>>> 
>>> thisdict = {}
>>> print(thisdict)
{}
>>> 
>>> thisdict = {
	"brand" : "Ford",
	"model" : "Mostang",
	"year" : 1964
	}
>>> print(thisdict)
{'brand': 'Ford', 'model': 'Mostang', 'year': 1964}
>>> 
>>> thisdict = {
	"brand" : "Ford",
	"model" : "Mostang",
	"year" : 1964
	}
>>> x = thisdict["model"]
>>> print(x)
Mostang
>>> 
>>> thisdict = {
	"brand" : "Ford",
	"model" : "Mostang",
	"year" : 1964
	}
>>> x = thisdict.get("model")
>>> print(x)
Mostang
>>> 
>>> thisdict = {
	"brand" : "Ford",
	"model" : "Mostang",
	"year" : 1964
	}
>>> thisdict ["year"] = 2018
>>> print(thisdict)
{'brand': 'Ford', 'model': 'Mostang', 'year': 2018}
>>> 
>>> thisdict = {
	"brand" : "Ford",
	"model" : "Mostang",
	"year" : 1964
	}
>>> for x in thisdict :
	print(x)

	
brand
model
year
>>> 
>>> thisdict = {
	"brand" : "Ford",
	"model" : "Mostang",
	"year" : 1964
	}
>>> for x in thisdict :
	print(thisdict[x])

	
Ford
Mostang
1964
>>> 
>>> thisdict = {
	"brand" : "Ford",
	"model" : "Mostang",
	"year" : 1964
	}
>>> for x in thisdict.values() :
	print(X)

	
Traceback (most recent call last):
  File "<pyshell#39>", line 2, in <module>
    print(X)
NameError: name 'X' is not defined
>>> print(x)
Ford
>>> 
>>> thisdict = {"brand" : "Ford", "model" : "Mustang", "year" : 1964}
>>> print(thisdict.values())
dict_values(['Ford', 'Mustang', 1964])
>>> 
>>> 
>>> thisdict = {
	"brand" : "Ford",
	"model" : "Mostang",
	"year" : 1964
	}
>>> for x in thisdict.items() :
	print(x, y)

	
Traceback (most recent call last):
  File "<pyshell#49>", line 2, in <module>
    print(x, y)
NameError: name 'y' is not defined
>>> 
>>> thisdict = {
	"brand" : "Ford",
	"model" : "Mostang",
	"year" : 1964
	}
>>> for x in thisdict.items ( ) :
	print(x, y)

	
Traceback (most recent call last):
  File "<pyshell#54>", line 2, in <module>
    print(x, y)
NameError: name 'y' is not defined
>>> 
>>> thisdict = {
	"brand" : "Ford",
	"model" : "Mostang",
	"year" : 1964
	}
>>> for x, yin thisdict.items ( ) :
	
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> hisdict = {
	"brand" : "Ford",
	"model" : "Mostang",
	"year" : 1964
	}
>>> for x, y in thisdict.items ( ) :
	print(x, y )

	
brand Ford
model Mostang
year 1964
>>> 
>>> thisdict = {"brand" : "Ford", "model" : "Mustang", "year" : 1964}
>>> print(thisdict.items())
dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
>>> 
