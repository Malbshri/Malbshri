Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # week 3
>>> # day 18 - 19
>>> 
>>> Team = ["Ahmad", "Saad", "Omar"]
>>> Team.append("Saad")
>>> print(Team)
['Ahmad', 'Saad', 'Omar', 'Saad']
>>> 
>>> Team = ["Ahmad", "Saad", "Omar"]
>>> Team.clear("Saad")
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    Team.clear("Saad")
TypeError: clear() takes no arguments (1 given)
>>> Team = ["Ahmad", "Saad", "Omar"]
>>> Team.clear()
>>> print(Team)
[]
>>> Team = ["Ahmad", "Saad", "Omar"]
>>> Team.remove("Omar")
>>> print(Team)
['Ahmad', 'Saad']
>>> 
>>> Team = ["Ahmad", "Saad", "Omar"]
>>> Team.sort()
>>> print(Team)
['Ahmad', 'Omar', 'Saad']
>>> 
>>> tuple=("java", "python", "swift")
>>> if "python" in (tuple)
SyntaxError: invalid syntax
>>> if "python" in (tuple) :
	print("python exists")

	
python exists
>>> 
