'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n):
    # Your code here
    # base case is if there is one cookie he can only eat one way,
    # 2 ways to eat 2, 4 ways to eat three
    if n >= 4:
        return eating_cookies(n-3)+eating_cookies(n-2)+eating_cookies(n-1)
    elif n == 3:
        return 4
    elif n == 2:
        return 2
    elif n <= 1:  # one way to eat zero cookies per test file
        return 1
    else:
        return 0


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
