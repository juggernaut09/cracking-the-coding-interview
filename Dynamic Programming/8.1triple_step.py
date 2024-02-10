def countWays(n: int, memo: list[int]) -> int:
    if n < 0: return 0
    if n == 0:return 1
    
    if memo[n] < 0:
        memo[n] = countWays(n-1, memo) + countWays(n-2, memo) + countWays(n-3, memo)
    return memo[n]

n = 3
print(countWays(n, [-1]*(n+1)))