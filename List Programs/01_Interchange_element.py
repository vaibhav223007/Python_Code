# Q.1 Python program to interchange first and last elements in a list

# Examples:

# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

# Input : [1, 2, 3]
# Output : [3, 2, 1]

# method-1: Traditional method
def interchange(lst):
    temp = lst[0]
    lst[0] = lst[-1]
    lst[-1] = temp

    return lst


print(interchange([1, 2, 3, 4, 5]))

# method-2: Simple Swapping
def interchange2(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst


print(interchange2([2, 3, 4, 5, 6]))


# Method-3: Packing and Unpacking in Tuple


def interchange3(lst):
    swapping = lst[0], lst[-1]
    lst[-1], lst[0] = swapping
    return lst


print(interchange3([10, 11, 12, 13]))


# Approach #4: Using * operand.

# some basing about "*"

listing = [10, 20, 30, 40, 50]

a, *b, c = listing
print(f"a is {a}")
print(f"b* is {b}")
print(f"c is {c}")


def interchange4(lst):
    start, *middle, end = lst
    lst = [end, *middle, start]
    return lst


print(f"Result os 4th method {interchange4([55,66,77,88])}")

# Approach 4: using pop and append()


def interchange5(lst):
    first = lst.pop(0)
    last = lst.pop()

    lst.insert(0, last)
    lst.append(first)
    return lst


print(f"Output of 5th method {interchange5([100,200,300,400,500])}")
