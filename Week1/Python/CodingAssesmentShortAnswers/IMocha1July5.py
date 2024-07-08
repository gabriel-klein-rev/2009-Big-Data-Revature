from collections import Counter


s = [1,1,1,2,2]
a = Counter(s)
#print(a)
#b = [(i, j) for i, j in a.items()]
#print(b)

def min_removals_to_make_frequencies_divisible(A, K):
    from collections import Counter

    # Step 1: Count the frequency of each element in the array
    freq = Counter(A)
    
    # Step 2: Initialize the count of elements to remove
    removals = 0
    
    # Step 3: Iterate through the frequency dictionary
    for count in freq.values():
        # If the frequency is not divisible by K
        if count % K != 0:
            # Calculate the number of removals needed
            removals += count % K
    
    return removals

y=min_removals_to_make_frequencies_divisible(s, 2)
print(y)