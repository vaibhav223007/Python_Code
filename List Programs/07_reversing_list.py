# Python | Reversing a List

# Method-1: reversed() and reverse()

lst = [10, 11, 12, 13, 14, 15]
reversed_lst = []

for ele in reversed(lst):
    reversed_lst.append(ele)

print(reversed_lst)

print(reversed_lst.reverse())

# Method-2: [::-1]
lst = [10, 11, 12, 13, 14, 15]
new_list = lst[::-1]
print("Reversed list", new_list)

