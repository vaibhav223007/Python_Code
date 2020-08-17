# Check if element exists in list in Python

# Method-1: Naive method

lst = ["vaibhav", 22, 12.30, "vishal"]


def finding1(lst, word_to_find):
    for ele in lst:
        if word_to_find == ele:
            print(f"{word_to_find} is in the list")
            break
    else:
        print(f"{word_to_find} not in the list")


finding1(lst, "hello")
finding1(lst, "vaibhav")

# Method-2: using "in"


def finding2(lst, word_to_find):
    return word_to_find in lst


print(finding2(lst, "vaibhav"))
print(finding2(lst, "hello"))
