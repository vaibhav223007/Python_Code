# Python program to swap two elements in a list

# Examples:

# Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# Output : [19, 65, 23, 90]

# Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
# Output : [1, 5, 3, 4, 2]

# Method 1: Simple Swapping
def swapping(lst, pos1, pos2):
    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
    return lst


print(swapping([11, 22, 33, 44, 55, 66], 1, 4))

# Method2:Tuple packing and Unpacking


def swapping2(lst, pos1, pos2):
    get = lst[pos1], lst[pos2]
    lst[pos2], lst[pos1] = get
    return lst


print(swapping2([1, 2, 3, 4, 5, 6], 3, 5))

# Method3: Using pop()
# This only works when we give position in ascending order like swapping3(lst,2,4)
# not when swapping3(lst,4,2)


def swapping3(lst, pos1, pos2):
    first_element = lst.pop(pos1)
    second_element = lst.pop(pos2 - 1)

    lst.insert(pos1, second_element)
    lst.insert(pos2, first_element)

    return lst


print(swapping3([99, 100, 101, 102, 103], 1, 4))
