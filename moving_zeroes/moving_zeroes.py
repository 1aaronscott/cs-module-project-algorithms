'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here
    # for each item pop and append to list if it is 0
    print("start list: ", arr)
    print("list length: ", len(arr))
    # for i in range(len(arr)):
    #     print("loop value: ", i)
    #     print("current list: ", arr)
    #     if arr[arr[i] == 0:
    #         arr.append(arr.pop(i))
    #         print("a change was made: ", arr)
    #     if max(arr[i:]) == 0:
    #         break
    i = 0
    while i < len(arr):
        print("loop value: ", i)
        print("current list: ", arr)
        if max(arr[i:]) == 0 and min(arr[i:]) == 0:
            break
        if arr[i] == 0:
            arr.append(arr.pop(i))
            print("a change was made: ", arr)
            continue
        i += 1

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]
#    arr = [0, 0, 0, 0, 3, 2, 1]
#    arr = [1, 2, 3, 0, 4, 0, 0]
#    arr = [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
