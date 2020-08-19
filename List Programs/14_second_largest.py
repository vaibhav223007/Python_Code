# Python program to find second largest number in a list

# Method-1: Using sort()


def second_largest(lst):
    lst.sort()
    return lst[-2]


result = second_largest([70, 11, 20, 4, 100])
print(f"Method-1 result => {result}")

# Method-2: removing max element


def second_largest2(lst):
    new_list = set(lst)
    max_element = max(new_list)
    new_list.remove(max_element)
    return max(new_list)


result2 = second_largest2([70, 11, 20, 4, 100])
print(f"Method-2 result => {result2}")

# Mthod-3: Naive method

list1 = [10, 20, 4, 45, 99]

mx = max(list1[0], list1[1])
secondmax = min(list1[0], list1[1])
n = len(list1)
for i in range(2, n):
    if list1[i] > mx:
        secondmax = mx
        mx = list1[i]
    elif list1[i] > secondmax and mx != list1[i]:
        secondmax = list1[i]

print("Second highest number is : ", str(secondmax))

