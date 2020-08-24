def positive_number(num):
    if num > 0:
        return num


find_postitive = list(filter(positive_number, [-2, 1, -3, 4, 5, -6, -100],))
print(f"positive numbers are {find_postitive}")


# odd_number


def odd_number(num):
    if num % 2 != 0:
        return num


num_list = range(-10, 10)
odd = list(filter(odd_number, num_list))
print(f"odd numbers are {odd}")

# prime_number


def prime_number(num):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        return num


prime_filter = range(2, 30)
prime = list(filter(prime_number, prime_filter))
print(prime)


# armtrong number


def armstrong_num(num):

    total = 0
    length = len(str(num))
    for i in str(num):
        total += pow(int(i), length)
    if total == num:
        return num


armstrong = [153, 22, 371, 33, 123]
armstrong_filter = list(filter(armstrong_num, armstrong))
print(f"From {armstrong} these are armstong numbers: {armstrong_filter}")
