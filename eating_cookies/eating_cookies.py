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

# Begin: code from lecture
# # Caching/memoization: Let's save our work so we don't have
# # to recompute it again

# # Need some sort of data structure where we'll save the data
# # arrays and dictionaries
# # If we check our cache and see that the answer we're looking for
# # is already in there, just return that answer
# # What if the cache doesn't have what we're looking for? Or how
# # do we get answers in there?
# # There's going to be a first time for calculating an answer, and we're
# # going to do it the same way we're currently doing it

# # O(n)
# def eating_cookies(n, cache=None):
#     # print(n)
#     # base case: when there are no more cookies
#     if n == 0:
#         return 1
#     # check for negative n values
#     elif n < 0:
#         return 0
#     # init our cache if we don't have it yet
#     # add a case to have us check the cache
#     elif cache and cache[n] > 0:
#         return cache[n]
#     else:
#         if not cache:
#             # cache = {i: 0 for i in range(n+1)}
#             cache = [0 for _ in range(n+1)]
#         # we can go ahead and save our answer to the cache
#         cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
#     return cache[n]
#     # this represents our recursive case where there still some cookies to be eaten
# End: code from lecture


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
