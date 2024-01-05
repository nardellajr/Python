# Examples of recursion
# Page 59 grokking algorithms

# Look into Tail Recursion


def factorial(x, stack):
    if x == 1:
        # print(f 'stack: {x}')
        stack.append("stack: " + str(x))
        return 1
    else:
        # print(f 'stack: {x}')
        stack.append("stack: " + str(x))
        return x * factorial(x - 1, stack)


def sum_arr(arr):
    if arr == 0:
        return 0
    else:
        # arr[1:] pops off first element, then passes the remaining elements back into method
        # remember each arr[0] is being saved in the call stack, so when it reaches Base case (starts unrolling)
        # each array element is added to the previous array element
        return arr[0] + sum(arr[1:])


def count_arr(arr):
    if not arr:
        return 0
    else:
        return 1 + count_arr(arr[1:])


def max_number_in_array(arr):
    # if not arr:
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]

    sub_max = max_number_in_array(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max


if __name__ == '__main__':
    stack = []
    print(factorial(5, stack))
    stack.reverse()
    print(f'Call stack before we start popping off items: {stack}')
    print(f'1 gets returned and multiplied * 2 gets returned and multiplied * 3 etc.. * 4 etc... * 5,'
          f' Total equals: {1*2*3*4*5}')

    # remember when you call a function from another function, the calling function is paused in a
    # partially completed state, if in a loop it will return and continue the loop.
    # This allows us to use the call stack to keep track of what still needs to be executed(the state)
    # One problem is each call takes up memory, so you could end up with a "Stack overflow"

    # Think of it as Divide and Conquer - D&C
    arr = [2, 4, 6]
    print()
    print(f'sum of array elements: {sum_arr(arr)}')

    print(f'Number of items in array: {count_arr(arr)}')

    arr = [4, 7, 9, 1, 4, 0]
    print(f'Maximum number in list: {max_number_in_array(arr)}')
