# Python – Remove Tuples of Length K

# Input : test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)], K = 2
# Output : [(4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
# Explanation : (4, 5) of len = 2 is removed

# Method-1:


def removing_tuple(input_list, length):
    index = 0
    l = len(input_list)
    while index < l:
        if len(input_list[index]) == length:
            del input_list[index]
            l -= 1
        index += 1
    return input_list


result = removing_tuple([(4, 5), (4,), (8, 6, 7), (1,), (3, 4, 6, 7), (9, 8)], 2)
print(f"Method-1 result => {result}")

# While solving this problem i found that i cannot change the range() in for loop and due to which
# i was getting "Index out of range" error. So after that i used while and it worked
# Use while whenever you are uncertain how many times should loop work or
# when you have to change the number of iteration while running the loop

# Method-2: List comprehention


def removing_tuple2(input_list, length):
    new_list = [ele for ele in input_list if len(ele) != length]
    return new_list


result2 = removing_tuple2([(4, 5), (4,), (8, 6, 7), (1,), (3, 4, 6, 7), (9, 9)], 2)
print(f"Method-2 result => {result2}")

# Method-3: lambda & filter

list3 = [(4, 5), (4,), (8, 6, 7), (1,), (3, 4, 6, 7), (9, 9)]
K = 2
new_list = list(filter(lambda x: len(x) != K, list3))
print(f"Method-3 result => {new_list}")
