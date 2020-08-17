# Python program to find sum of elements in list

# Method-1: Naive mwthod
print("*" * 30, "Method-1", "*" * 30)


def sum_list(lst):
    summ = 0
    for ele in lst:
        summ += ele
    return summ


result = sum_list([12, 15, 3, 10])
print(result)

# Method-2: Using sum() method
print("*" * 30, "Method-2", "*" * 30)


def sum_list2(lst):
    return sum(lst)


result = sum_list2([12, 15, 3, 10, 10])
print(result)

# Method-3 : Using while loop
print("*" * 30, "Method-3", "*" * 30)
lis = [12, 15, 3, 10]
index = 0
summ = 0

while index < len(lis):
    summ += lis[index]
    index += 1

print(f"Sum is {summ}")
