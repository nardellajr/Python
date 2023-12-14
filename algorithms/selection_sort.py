# Selection Sort Algorithm
# Big O - Time O(n**2)


# find the smallest value element in the array
def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        # the pop removes the element by index from arr
        new_arr.append((arr.pop(smallest)))  # adds smallest to new array becoming sorted array
    return new_arr


if __name__ == '__main__':
    arr = [5, 3, 6, 2, 10]
    sorted_array = selection_sort(arr)

    print(sorted_array)


