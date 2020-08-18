# Python | Multiply all numbers in the list (4 different ways)

# Method-1:

print("*" * 30, "Method-1", "*" * 30)


def product1(lst):
    mult = 1
    for ele in lst:
        mult *= ele
    return mult


result = product1([1, 2, 3, 4, 5])
print(f"Product 1 product {result}")

# Method-2: Using reduce
print("*" * 30, "Method-2", "*" * 30)
from functools import reduce

lst = [1, 2, 3, 4, 5]
result2 = reduce(lambda x, y: x * y, lst)
print(f"result using reduce {result2}")

# can also use numpy.prod() for that you have to import numpy

