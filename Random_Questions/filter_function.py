from functools import reduce


def multiply(num1, num2):
    return num1 * num2


lst = [1, 2, 3, 4]
product = reduce(multiply, lst)
print(product)
