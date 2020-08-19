# Python program to create a list of tuples from given list having number and its cube in each tuple

# Example:
# Input: list = [1, 2, 3]
# Output: [(1, 1), (2, 8), (3, 27)]

# Input: list = [9, 5, 6]
# Output: [(9, 729), (5, 125), (6, 216)]


# Method-1:

list1 = [1, 2, 3]
new_list = []
for ele in list1:
    new_list.append((ele, ele ** 3))

print(f"Method-1 result {new_list}")

# Method-2 : Using list comprehension
new_list2 = [(ele, pow(ele, 3)) for ele in list1]
print(f"Method-2 result {new_list2}")

# Method-3 Using map and lambda

new_list3 = list(map(lambda x: (x, x ** 3), list1))
print(f"Method-3 reult {new_list3}")

