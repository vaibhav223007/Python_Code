# Python – Remove Tuples of Length K

# Input : test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)], K = 2
# Output : [(4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
# Explanation : (4, 5) of len = 2 is removed

# Method-1:


def removing_tuple1(lst, length):
    index = 0
    list_length = len(lst)
    while index <= list_length:
        if len(lst[index]) == length:
            del lst[index]

        index += 1
    return lst


result = removing_tuple1(
    [(4, 5), (4,), (8, 6, 7), (1,), (3, 4, 6, 7), (9, 9), (1, 2, 3)], 2
)
print(f"Result of Method-1 => {result}")

