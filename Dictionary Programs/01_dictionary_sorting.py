# Python | Sort Python Dictionaries by Key or Value


# Method-1
dictionary1 = {1: "vaibhav", 3: "vishal", 5: "himesh", 2: "rahul", 4: "durga"}

for i in sorted(dictionary1.keys()):
    print(i)

# Method-2

from collections import OrderedDict

dictionary2 = OrderedDict(sorted(dictionary1.items()))
print(dictionary2)

