# Adding the element at new list by adding the list at same inde of other two list

a = [10, 20, 30, 40]
b = [100, 200, 300, 400]
c = []

index = 0
while index < min(len(a), len(b)):
    summ = a[index] + b[index]
    c.append(summ)
    index += 1

print(c)
