from typing import List


def dutch_flag_bruteForce(pivot_index: int, A: List[int]) -> List[int]:
    pivot = A[pivot_index]
    # Group elements < pivot
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break

    # Group elements > pivot
    for i in reversed(range(len(A))):
        # Look for larger; stop when elem < pivot since pivot went to the start
        # of A
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break
    return A



print(dutch_flag_bruteForce(3, A=[5, 4, 1, 2, 2]))
