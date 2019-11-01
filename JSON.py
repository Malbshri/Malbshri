import json
# some JSON:
x = '{ "name" : "John", "age" : 30, "city" : "Newyork"}'
# parse x:
y = json.loads(x)

# the resolt is a Python dictionary:
print(y["age"])

import json
# a Python object (dict):
x = {
    "name" : "John",
    "age" : 30,
    "city" : "Newyork"
}
# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

import json
x = {
    "name" : "John",
    "age" : 30,
    "married" : True,
    "divorced" : False,
    "children" : ("Ann", "Billy"),
    "pets" : None,
    "cars" : [
        {"model" : "BMW 230", "mpg" : 27.5 },
        {"model" : "Ford Edge", "mpg" : 24.1 }
    ]
}

# convert into JSON:
y = json.dumps(x)

# the resolt is a JSON string:
print(y)

import json
x = {
    "name" : "John",
    "age" : 30,
    "married" : True,
    "divorced" : False,
    "children" : ("Ann", "Billy"),
    "pets" : None,
    "cars" : [
        {"model" : "BMW 230", "mpg" : 27.5 },
        {"model" : "Ford Edge", "mpg" : 24.1 }
    ]
}
# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))

import json
x = {
    "name" : "John",
    "age" : 30,
    "married" : True,
    "divorced" : False,
    "children" : ("Ann", "Billy"),
    "pets" : None,
    "cars" : [
        {"model" : "BMW 230", "mpg" : 27.5 },
        {"model" : "Ford Edge", "mpg" : 24.1 }
    ]
}
# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4, separators=(". ", " = ")))

import json
x = {
    "name" : "John",
    "age" : 30,
    "married" : True,
    "divorced" : False,
    "children" : ("Ann", "Billy"),
    "pets" : None,
    "cars" : [
        {"model" : "BMW 230", "mpg" : 27.5 },
        {"model" : "Ford Edge", "mpg" : 24.1 }
    ]
}
# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4, sort_keys=True))