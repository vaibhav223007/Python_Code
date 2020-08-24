num = [1, 2, 3, 4, 5]


def square(num):
    return num ** 2


squaring = list(map(square, num))
print(f"square is {squaring}")
