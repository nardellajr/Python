# create Merge sort method

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        # divide the array into 2 parts
        l = arr[:mid]
        r = arr[mid:]

        mergesort(l)
        mergesort(r)

        i = j = k = 0

        # does this loop while there are elements in both arrays
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[i]
                j += 1
            k += 1

        # does this loop while there are still elements in this array, the r array wouldn't have any elements
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        # does this loop while there are still elements in this array, the l array wouldn't have any elements
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1


if __name__ == '__main__':
    # arr = [12, 11, 13, 5, 6, 7]
    arr = [10, 7, 8, 9, 1, 5]
    mergesort(arr)
    print("Sorted array is:", arr)
