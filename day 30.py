Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # week 5
>>> # day 30
>>> 
>>> for x in range (6) :
	print(x)

	
0
1
2
3
4
5
>>> 
>>> for x in range (2, 6) :
	print(x)

	
2
3
4
5
>>> 
>>> for x in range (2, 30, 3) :
	print(x)

	
2
5
8
11
14
17
20
23
26
29
>>> 
>>> for x in range (6) :
	print(x)
else :
	print("Finally finished!")

	
0
1
2
3
4
5
Finally finished!
>>> 
>>> adj = ["red", "big", "tasty"]
>>> fruits = ["apple", "banana", "cherry"]
>>> for x in adj :
	for y in fruits :
		print(x, y)

		
red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry
>>> 
>>> 
