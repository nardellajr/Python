# create Quicksort algorithm


# Not choosing the correct pivot point effects Time complexity
# In the "height of the call stack" size
# Best case for the call stack  O(log n) and worse case O(n)
# We have to touch every element so O(n)
# Know take O(n) * O(log n) = O(n log n)  -- Best
# and       O(n) * O(n)     = O(n**2)     -- Worst
def quicksort(arr):
    # base case, nothing to sort
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i < pivot]
        greater = [i for i in arr[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == '__main__':
    arr = [10, 5, 2, 3]
    print(quicksort(arr))
