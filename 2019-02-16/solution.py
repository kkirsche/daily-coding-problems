# Good morning! Here's your coding interview problem for today.
# This problem was recently asked by Google.
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# bonus: Can you do this in one pass?

from itertools import combinations

def result(k, l):
    l = list(map(sum, combinations(l, 2)))
    if k in l:
        return True
    return False
    
sl = [10, 15, 3, 7]
k = 17

r = result(k, sl)
print(r)
