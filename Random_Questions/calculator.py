def add(num1, num2):
    return num1 + num2


def substract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


print(
    """Press:
      1.add
      2.substract 
      3.Multiply 
      4.divide"""
)

user_input = int(input("Enter your choice: "))
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

if user_input == 1:
    print(add(num1, num2))

elif user_input == 2:
    print(substract(num1, num2))

elif user_input == 3:
    print(multiply(num1, num2))

elif user_input == 4:
    print(division(num1, num2))

else:
    print("Invalid Input")

