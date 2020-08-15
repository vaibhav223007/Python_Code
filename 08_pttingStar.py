# 8. WAP to put 3 "*" on either side of s="Hello World"

# metho-1
s = "Hello World"
print(s.center(17, "*"))

# method-2
def put_star(string, number):
    print("*" * number, end=" ")
    print(string, end=" ")
    print("*" * number)


put_star("Hello Word", 3)
