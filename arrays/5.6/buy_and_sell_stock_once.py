from typing import List





# Brute Force

def buy_sell_once(A: List[float]) -> float:
    d, max_d = 0, 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            d = A[j] - A[i]
            if d > max_d:
                max_d = d
    if max_d > 0:
        return max_d


A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
print(buy_sell_once(A))



