Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # week 4
>>> # day 23
>>> 
>>> thisdict = {
	"brand" : "Ford",
	"model" :"Mustang",
	"year" : 1964
	}
>>> if "model" in thisdict :
	print("Yes, 'model' is one of the keys in the thisdict dictionary")

	
Yes, 'model' is one of the keys in the thisdict dictionary
>>> 
>>> thisdict = {
	"brand" : "Ford",
	"model" :"Mustang",
	"year" : 1964
	}
>>> print(len(thisdict))
3
>>> 
>>> thisdict = {
	"brand" : "Ford",
	"model" :"Mustang",
	"year" : 1964
	}
>>> thisdict["color"] = "red"
>>> print(thisdict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
>>> 
>>> thisdict = {
	"brand" : "Ford",
	"model" :"Mustang",
	"year" : 1964
	}
>>> thisdict.pop("model")
'Mustang'
>>> print(thisdict)
{'brand': 'Ford', 'year': 1964}
>>> 
>>> thisdict = {
	"brand" : "Ford",
	"model" :"Mustang",
	"year" : 1964
	}
>>> thisdict.opoitem()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    thisdict.opoitem()
AttributeError: 'dict' object has no attribute 'opoitem'
>>> thisdict.popitem()
('year', 1964)
>>> print(thisdict)
{'brand': 'Ford', 'model': 'Mustang'}
>>> 
>>> thisdict = {
	"brand" : "Ford",
	"model" :"Mustang",
	"year" : 1964
	}
>>> del thisdict["model"]
>>> print(thisdict)
{'brand': 'Ford', 'year': 1964}
>>> 
>>> thisdict = {
	"brand" : "Ford",
	"model" :"Mustang",
	"year" : 1964
	}
>>> del thisdict
>>> print(thisdic) # this will cause an error because "thisdict" no longer exists.
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print(thisdic) # this will cause an error because "thisdict" no longer exists.
NameError: name 'thisdic' is not defined
>>> 
>>> thisdict = {
	"brand" : "Ford",
	"model" :"Mustang",
	"year" : 1964
	}
>>> thisdict.clear()
>>> print(thisdict)
{}
>>> # done
