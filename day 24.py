Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # week 4
>>> # day 24
>>> 
>>> thisdict = {
	"brand" : "Ford",
	"model" :"Mustang",
	"year" : 1964
	}
>>> mydict = thisdict.copy()
>>> print(thisdict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
>>> 
>>> print(mydict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
>>> 
>>> thisdict = {
	"brand" : "Ford",
	"model" :"Mustang",
	"year" : 1964
	}
>>> mydict = dict(thisdict)
>>> print(mydict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
>>> 
>>> 
>>> myfamily = {
	"child1" : {
		"name" : "Email",
		"year" : 2004
		},
	"child2" : {
		"name" : "Tobias",
		"year" : 2007
		},
	"child3" : {
		"name" : "Linus",
		"year" : 2011
		}
	}
>>> print(myfamily)
{'child1': {'name': 'Email', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}
>>> 
>>> 
>>> child1 = {
	"name" : "Email",
	"year" : 2004
	}
>>> child2 = {
	"name" : "Tobias",
	"year" : 2007
	}
>>> child3 = {
	"name" : "linus",
	"year" : 2011
	}
>>> myfamily = {
	"child1" : child1,
	"child2" : child2,
	"child3" : child3
	}
>>> print(myfamily)
{'child1': {'name': 'Email', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'linus', 'year': 2011}}
>>> 
>>> thisdict = dict(brand="Ford", model="Mustang", year=1964)
>>> # note that keywords are not string literals
>>> # note the use of equals rather than colon for the assignment
>>> print(thisdict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
>>> 
