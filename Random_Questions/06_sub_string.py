# 6. WAP to check if a sub string is available in a string. String = "This is python"

string = "This is python"


def sub_string(string, sub_string):
    if sub_string.lower() in string.lower():
        print(f"'{sub_string}' in '{string}'")
    else:
        print(f"'{sub_string}' not in '{string}'")


sub_string(string, "any")
sub_string(string, "is")
sub_string(string, "Python")
