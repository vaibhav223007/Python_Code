# Python | Cloning or Copying a list

# 1. Using slicing technique
print("*" * 30, "Method-1", "*" * 30)
list1 = [2, 4, 6, 8, 10]
list2 = list1[:]
print(list2)
list1.append(100)
print(list2)

# 2. Using the extend() method
print("*" * 30, "Method-2", "*" * 30)
list3 = [2, 4, 6, 8, 10]
list4 = []
list4.extend(list1)
print(list4)
list1.append(999)
print(list2)
print(list1)

# 3. Using list()
print("*" * 30, "Method-3", "*" * 30)
list5 = [2, 4, 6, 8, 10]
list6 = list(list5)
print(list6)
list5.append(1234)
print(list6)
print(list5)

# 4.List comprehension
print("*" * 30, "Method-4", "*" * 30)
list7 = [2, 4, 6, 8, 10]
list8 = [i for i in list7]
print(list8)
list7.append(3334)
print(list8)
print(list7)

# Also read copy() and deepcopy() from stackover flow
