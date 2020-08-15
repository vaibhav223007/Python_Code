# 9. WAP to hide 12 starting digit of a 16 digit account number----print (12*" " +p[::-4])


def hidding_number(number):
    star = "*" * 16
    print(f"{star}{str(number)[-4:]}")


hidding_number(1234567891122334)
