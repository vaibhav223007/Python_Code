# Python program to sort a list of tuples by second Item

# Examples:

# Input : [('for', 24), ('Geeks', 8), ('Geeks', 30)]
# Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]

# Input : [('452', 10), ('256', 5), ('100', 20), ('135', 15)]
# Output : [('256', 5), ('452', 10), ('135', 15), ('100', 20)]

# Method-1: Using lst.sort()


def sort_tuple(lst):
    lst.sort(key=lambda x: x[1])
    return lst


tup = [("rishav", 10), ("akash", 5), ("ram", 20), ("gaurav", 15)]
print(f"Method-1: {sort_tuple(tup)}")

# Method-2: sorted(lst)


def sort_tuple2(lst):
    sorted_list = sorted(lst, key=lambda x: x[1])
    return sorted_list


tup2 = [("rishav", 10), ("akash", 5), ("ram", 20), ("gaurav", 15)]
print(f"Method-2: {sort_tuple2(tup2)}")
