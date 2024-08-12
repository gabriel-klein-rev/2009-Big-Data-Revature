'''
W7 Python Activity

Complete the following functions. Once complete, send your solution to gabriel.klein@revature.com

'''


# 1) Write a function that returns the most common element in a list. If there are multiple, return the largest element
def most_common(lst:int) -> int:
    # Write your code here:

    return -999


# 2) Write a function that returns a list of dictionary values from a given dictionary in a sorted descending order
def sort_values_desc(dct:dict[str,int]) -> list[int]:
    # Write your code here:

    return [-999]

# 3) Write a function that prints the union and intersection between two sets, and also prints the elements unique to each.
def sets(set1:set[int], set2:set[int]) -> None:
    # Write your code here:

    return

# 4) Write a function that takes a dictionary and returns a list of tuples representing the key-value pairs, sorted by key
def to_tup_list(dct:dict[int,int]) -> list[(int, int)]:
    # Write your code here:

    return[(-999,-999)]




#################################################
########### Don't change code below #############
#################################################

# Test 1
print(most_common([1, 2, 3, 4, 2, 3, 4, 3, 4, 3, 2, 3, 4, 4]))

# Test 2
print(sort_values_desc({"a":2, "b":4, "c":1, "aa":-5, "ab":10, "ac":6, "ba":3, "bb":5, "bc":6, "ca":0}))

# Test 3
sets({2, 4, 5, 6, 7, 8, 10}, {1, 5, 6, 7, 9})

# Test 4
print(to_tup_list({"a":2, "b":4, "c":1, "aa":-5, "ab":10, "ac":6, "ba":3, "bb":5, "bc":6, "ca":0}))