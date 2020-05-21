'''
Input: a List of integers
Returns: a List of integers
'''
import math


def product_of_all_other_numbers(arr):
    # Your code here
    mult_list = []
#    print("length of original list: ", len(arr))
#    print(arr, "\n", arr[:-1])
    for i in range(len(arr)):
        # product when at the start of list
        if i == 0:
            mult_list.append(math.prod(arr[1:]))
        # product when at the end of list
        elif i == (len(arr)-1):
            mult_list.append(math.prod(arr[:-1]))
        # product when in the middle of the list
        else:
            mult_list.append(math.prod(arr[:i]+arr[i+1:]))
    return mult_list


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
    #        9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]
    # arr = [7, 9, 1, 8, 6, 7, 8, 8, 7, 10]
    # arr = [7, 9, 1, 8, 6, 0, 7, 8, 8, 7, 10]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
