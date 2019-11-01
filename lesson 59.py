import  re
#Replace all white-space charactor with the digit "9":
str = "The rsin in Spain"
x = re.sub("\s", "9", str)
print(x)

import re
#Replace the first two occurrence of white-space charactor with the digit 9"

str = "The rain in Spain"
x = re.sub("\s", "9", str, 2)
print(x)

import re
#The search() function returns a Mach object:

str = "The rain in Sapin"
x = re.search("ai", str)
print(x)

import re
#Search for an upper case "S" character in the beginning of a word, and print its position:

str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.span())

import re
#The string property returns the search string:

str = "Thr rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.string)

import re
#Search for an upper case "S" character in the beginning of a word, and print the word:
str = "Thr rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.group())
