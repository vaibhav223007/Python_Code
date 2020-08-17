# Different ways to clear a list in Python

# Method-1 : clear() method

lst = [1, 2, 2, 3, 4, 5]
print(f"List is {lst}")
lst.clear()
print(f"List after using clear() => {lst}")

# Method-2: Using []
lst1 = [1, 2, 3, 4, "vaibhav"]
print(f"List is {lst1}")
lst1 = []
print(f"List after using [] => {lst1}")

# Method-3: Using "*=0"
lst1 = [1, 2, 3, 4, "vaibhav"]
print(f"List is {lst1}")
lst1 *= 0
print(f"List after using *= => {lst1}")

# Method-4: Using "del"
lst1 = [1, 2, 3, 4, "vaibhav"]
print(f"List is {lst1}")
del lst1[:]
print(f"List after using del => {lst1}")

