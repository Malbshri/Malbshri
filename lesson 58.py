import re
#Return all list containing every occurrence of "ai":

str = "The rain in Spain"
x = re.findall("ai", str)
print(x)

import re
str = "The rain in Spain"
#Chick if "Portygal" is in the string:
x = re.findall("Portugal", str)
print(x)

if (x):
    print("Yes, there is at least one match!")
else:
    print("No match")

import re
str = "The rain in Spain"
x = re.search("\s", str)
print("the first white-space charcter is located in position:", x.start())

import re
str = "The rain in Spain"
x = re.search("Portugal", str)
print(x)

import re
#Split the string at every white-space charactor:
str = "The rain in Spain"
x = re.split("\s", str)
print(x)
