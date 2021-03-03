# Invariant Problems: 
from typing import List

A = [3, 1, 2, 2, 1, 3, 2, 3]





# TODO: Return to complete the rest of 5.1 invariants






# Invariant One
# Reorder the array so that all objects with the same key appear together.
# Order does not matter. 
# Constraints O(1) additional space and O(n) time


# Brute Force: Create three lists for each respective key and then write these
#              values back into A.

# Optimized:
# O(n) time complexity and space complexity? O(?) -> O(1) 
# Solved in 2 passes. BONUS: Can we solve in one pass and keep O(n) time?
def invariant_one(A: List[int]) -> List[int]:
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

# print(invariant_one(A))



# Invariant Three
# Given array A of n objects, with boolean valued keys, reorder so that the key
# false appears first. Use O(1) additional space and O(n) time.


def invariant_three(B: List[bool]) -> List[bool]:
    j = 0
    for i in range(j+1, len(B)):
        if B[i] == False:
            B[i], B[j]  = B[j], B[i]
            i, j = i+1, j+1
        else:
            i+=1

    return B

print(invariant_three(B=[1, 0, 1, 0, 0, 1]))
print(invariant_three(B=[1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1]))



