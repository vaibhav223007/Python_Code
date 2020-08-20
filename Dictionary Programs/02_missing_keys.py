# Handling missing keys in Python dictionaries

# In python, dictionaries are containers which map one key to its
#  value with access time complexity to be O(1). But in many applications,
#  the user doesn’t know all the keys present in the dictionaries.
# In such instances, if user tries to access a missing key, an error is popped indicating missing keys.

# Method-1: using get()

# get(key,def_val) method is useful when we have to check for the key.
# If the key is present, value associated with the key is printed,
#  else the def_value passed in arguments is returned.

dictionary1 = {1: "vaibhav", 3: "vishal", 5: "himesh", 2: "rahul", 4: "durga"}

# print(dictionary1[100])
print(dictionary1.get(100, "key not present"))

# method-2: setdefault()

# Method 2 : Using setdefault()
# setdefault(key, def_value) works in a similar way as get(),
# but the difference is that each time a key is absent,
# a new key is created with the def_value associated to the key passed in arguments.

print(dictionary1.setdefault(100, "new value added"))
print(dictionary1)


# Method-3: defaultdict()
# “defaultdict” is a container that is defined in module named “collections“
# The implementation of defaultdict is faster than get() or setdefault().
import collections

dictionary2 = collections.defaultdict(lambda: "Key not found")

dictionary2[1] = "hello"
dictionary2[2] = "world"

print(dictionary2["abcd"])
