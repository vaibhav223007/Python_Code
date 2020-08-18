# Python program to find smallest number in a list

# method 1: Naive method


def smallest_number1(lst):
    small = lst[0]
    for ele in lst:
        if ele < small:
            small = ele
    return small


result = smallest_number1([22, 33, 11, 55, 9, 66, 12])
print(f"Smallest number is {result}")

# Method-2 : using min()

lst = [100, 11, 1100, 9]
print(f"Using min() =>{min(lst)}")

# Method-3:
lst2 = [123, 234, 543, 22]
lst2.sort()
print(f"Using sort() => {lst2[0]}")
