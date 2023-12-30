
# create Quicksort algorithm

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
