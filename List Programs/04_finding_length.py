# Python | Ways to find length of list

# Method 1: Naive method

lst = [1, 2, 3, 4, 5, 6, 100]
count = 0

for ele in lst:
    count += 1
print(f"Total element are {count}")

# Method 2: Using len()

print(f"Using len method length is {len(lst)}")

# Method 3: Using lenght_hint()
from operator import length_hint

length = length_hint(lst)

print(f"Length using length_hint() is {length}")

# Analysis b/w len() and length_hint()
print("*" * 30, "Analysis", "*" * 30)
from operator import length_hint
import time

test_list = [1, 2, 3, 4, 5]

print(f"Test list is {test_list}")

start_time = time.time()

# checking time for naive method i.e. method 1

count = 0
for ele in test_list:
    count += 1

end_time = time.time() - start_time
print("Time taken by for loop is ", end_time)

# After using same method to calculate time for all method it is found that
#  Naive method >> length_hint() >> len()
# Hence len() is the best method to use while calculating length.

