def hcf(number1, number2):
    num = min(number1, number2)
    new_number = 1
    for i in range(2, num + 1):
        if number1 % i == 0 and number2 % i == 0:
            new_number = i

    return new_number


print(hcf(13, 26))

