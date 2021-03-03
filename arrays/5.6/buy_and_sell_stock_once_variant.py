from typing import List
import random

# TODO: Write Test Cases

A = [1, 2, 2, 1, 3, 1, 3, 3, 4, 1, 1, 1, 3]

# Time Complexity: O(n)
# Space Complexity: O(1)


def variant(A: List[int]) -> int:
    count, longest_equal_subarray = 1, 0
    start, end = 0, 1
    while end < len(A):
        if A[end] == A[start]:
            count, end, start = count + 1, end + 1, start + 1
            longest_equal_subarray = max(longest_equal_subarray, count)
        else:
            count = 1
            start, end = start + 1, end + 1

    return longest_equal_subarray



def input():
    for i in range(20):    
        x = [random.randint(1,3) for x in range(1, random.randrange(1,20))]
        print(x)
        print(variant(x))


     
input()
