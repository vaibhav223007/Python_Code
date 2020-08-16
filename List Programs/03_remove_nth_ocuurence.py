# Python program to remove Nth occurrence of the given word

# Examples:

# Input: list - ["geeks", "for", "geeks"]
#        word = geeks, N = 2
# Output: list - ["geeks", "for"]

# Input: list - ["can", "you",  "can", "a", "can" "?"]
#        word = can, N = 1
# Output: list - ["you",  "can", "a", "can" "?"]


def removing_element(lst, word, occurance):
    occured = 0

    for i in range(len(lst)):
        if lst[i] == word:
            occured += 1
            if occured == occurance:
                del lst[i]
                print("Word found!")
                break

    else:
        print("Word not found")

    return lst


print(removing_element(["geeks", "for", "geeks"], "geeks", 2))

