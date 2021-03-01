# Invariant Problems: 
from typing import List

A = [3, 1, 2, 2, 1, 3, 2, 3]

# Invariant One
# Reorder the array so that all objects with the same key appear together.
# Order does not matter. 
# Constraints O(1) additional space and O(n) time


# Brute Force
# O(n) time complexity and space complexity? O(?) -> O(1) 
def invariantOne(A: List[int]) -> List[int]:
    i = 0
    for j in range(i+1, len(A)):
        if A[j] == A[i]:
            A[i+1], A[j] = A[j], A[i+1]
            j+=1
            i+=1
        else:
            j+=1
    
    k = len(A) - 1
    for j in reversed(range(len(A)-1)):
        print(j)
        if A[j] == A[k]:
            A[k-1], A[j] = A[j], A[k-1]
            j-=1
            k-=1
        else:
            j-=1

    return A



print(invariantOne(A))
