'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    # Your code here
    # find length of list
    lsize = len(nums)
    # deal with cases where list or window is small
    if lsize <= 1 or k <= 1:
        return nums
    # storage list for the maxes
    maxes = []
    # determine the number of possible windows given inputs
    windows = lsize-k+1
    # loop through the input list windows finding the max of each
    i = 0
    while i < windows:
        maxes.append(max(nums[i:i+k]))
        i += 1
    return maxes


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(
        f"{arr}\nOutput of sliding_window_max function is: {sliding_window_max(arr, k)}")
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 2
    print(
        f"{arr}\nOutput of sliding_window_max function is: {sliding_window_max(arr, k)}")
    arr = [70, 37, 100, 66, 1, 45, 27, 62, 75, 57, 92, 66, 9, 39, 15, 69, 46, 72, 35, 68, 54, 51, 35, 36, 13, 27, 27, 24, 6, 33, 83, 97, 55, 5, 25, 85, 56, 4, 100, 38, 38, 83, 29, 1, 11, 27, 64, 99, 64,
           29, 41, 95, 59, 46, 75, 67, 40, 49, 62, 30, 56, 88, 71, 77, 43, 79, 27, 65, 24, 18, 74, 50, 23, 47, 45, 60, 62, 84, 53, 2, 90, 29, 99, 75, 59, 44, 71, 7, 59, 59, 27, 72, 6, 89, 90, 40, 51, 45, 43, 86]
    k = 5
    print(
        f"{arr}\nOutput of sliding_window_max function is: {sliding_window_max(arr, k)}")
