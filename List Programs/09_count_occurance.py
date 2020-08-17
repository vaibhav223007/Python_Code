# Python | Count occurrences of an element in a list

# Method-1: naive method
print("*" * 30, "Method-1", "*" * 30)


def count_occurance1(lst, element):
    count = 0
    for ele in lst:
        if ele == element:
            count += 1

    return count


result = count_occurance1([15, 6, 7, 10, 12, 20, 10, 28, 10], 10)
print(result)

# Method 2 (Using count())
print("*" * 30, "Method-2", "*" * 30)


def count_occurance2(lst, element):
    return lst.count(element)


result = count_occurance2([15, 6, 7, 10, 12, 20, 10, 28, 10], 10)
print(result)

