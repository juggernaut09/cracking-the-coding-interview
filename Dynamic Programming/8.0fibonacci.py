# Top-Down Dynamic programming Approach (Memoization)
def fib(n, memo):
    if n == 0 or n == 1: return n
    
    if memo[n] == None:
        memo[n] = fib(n-1, memo) + fib(n-2, memo) 
    return memo[n]

n = 100
memo = [None] * (n+1)
print("Top-Down Dynamic programming Approach", fib(n, memo))

# Bottom up approach 
def fib_bottom_up(n):
    if n == 0 or n == 1: return n
    memo = [None] * (n+1)
    memo[0] = 0
    memo[1] = 1
    for i in range(2, n):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n-1] + memo[n-2]
print("fib_bottom_up", fib_bottom_up(100))

# Bottom up approach without using array
def fib_bottom_up2(n):
    if n == 0 and n == 1: return n
    a = 0
    b = 1
    for i in range(2, n):
        c = a + b
        a = b
        b = c
    return a+b
print("Bottom up approach without using array : ",fib_bottom_up2(100))
    
