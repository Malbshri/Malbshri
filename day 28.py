Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # week 5
>>> # day 28
>>> 
>>> i = 1
>>> while i < 6 :
	print(i)
	i += 1

	
1
2
3
4
5
>>> 
>>> i = 1
>>> while i < 6 :
	print(i)
	if i == 3 :
		break
	i += 1

	
1
2
3
>>> 
>>> 
>>> i = 0
>>> while i < 6 :
	i +=1
	if i == 3 :
		continue
	print(i)

	
1
2
4
5
6
>>> 
>>> 
>>> i = 1
>>> while i < 6 :
	print(i)
	i += 1
	else :
		
SyntaxError: invalid syntax
>>> 
>>> i = 1
>>> while i < 6 :
	print(i)
	i += 1
else :
	print(" i is no longer less than 6 ")

	
1
2
3
4
5
 i is no longer less than 6 
>>> 
