'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
from collections import Counter


def single_number(arr):
    # Your code here
    # convert counter object into a dict
    counts = dict(Counter(arr))
    # loop through dict and find the key with a value of 1
    for key, value in counts.items():
        if value == 1:
            return key


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
