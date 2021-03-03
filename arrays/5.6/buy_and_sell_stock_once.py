from typing import List




# Brute Force
# Time Complexity: O(n**2) 
# Space Complexity: O(1)?
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

def buy_sell_once_optimized(A: List[float]) -> float:
    min_price_so_far, max_profit = float('inf'), 0.0
    for price in A:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit

print("Optimized :")
print(buy_sell_once_optimized(A))
