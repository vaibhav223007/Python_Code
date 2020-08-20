# Python program to find N largest elements from a list

# Examples :

# Input : [4, 5, 1, 2, 9]
#         N = 2
# Output :  [9, 5]

# Input : [81, 52, 45, 10, 3, 2, 96]
#         N = 3
# Output : [81, 96, 52]

# Method-1:


def n_largest(lst, n):
    new_list = []
    sorted_list = sorted(lst, reverse=True)
    for i in range(n):
        new_list.append(sorted_list[i])
    return new_list


result1 = n_largest([81, 52, 45, 10, 3, 2, 96], 3)
print(f"Method-1 result => {result1}")

# Method-2: sort() and slicing


def n_largest2(lst, n):
    lst.sort()
    return lst[-n:]


result2 = n_largest2([81, 52, 45, 10, 3, 2, 96], 3)
print(f"Method-2 result => {result2}")

# Method-3: Naive method

