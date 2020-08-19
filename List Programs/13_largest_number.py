# Python program to find largest number in a list

# Method-1:
def largest_number(lst):

    largest_number = lst[0]
    for ele in lst:
        if ele > largest_number:
            largest_number = ele
    return largest_number


result = largest_number([20, 10, 20, 4, 100])
print(f"Method-1 result => {result}")

# Method-2: Using lst.sort() or sorted(lst)


def largest_number2(lst):
    lst.sort()
    return lst[-1]


result2 = largest_number2([20, 10, 20, 4, 100])
print(f"Method-2 result => {result2}")

# Method-3 using max():


def largest_number3(lst):
    return max(lst)


result3 = largest_number3([20, 10, 20, 4, 100])
print(f"Method-3 result => {result3}")
