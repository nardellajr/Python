# create Quicksort algorithm
import random


# Not choosing the correct pivot point effects Time complexity
# And the "height of the call stack" size
# Best case for the call stack  O(log n) and worse case O(n)
# We have to touch every element when sorting so O(n)
# Know take O(n) * O(log n) = O(n log n)  -- Best
# and       O(n) * O(n)     = O(n**2)     -- Worst

# Choosing a random element for the pivot, will get you O(log n)
def quicksort(arr):
    # base case, nothing to sort
    if len(arr) < 2:
        return arr
    else:
        # pivot = arr[0]
        # less = [i for i in arr[1:] if i < pivot]
        # greater = [i for i in arr[1:] if i > pivot]

        pivot = random.choice(arr)
        equal = [i for i in arr if i == pivot]
        less = [i for i in arr if i < pivot]
        greater = [i for i in arr if i > pivot]

        # return quicksort(less) + [pivot] + quicksort(greater)
        return quicksort(less) + equal + quicksort(greater)


if __name__ == '__main__':
    arr = [10, 5, 2, 3]
    print(quicksort(arr))
