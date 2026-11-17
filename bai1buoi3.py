import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    k = int(data[1])
    

    dp = [0] * k
    dp[0] = 1  
    
    for _ in range(n):
        new_dp = [0] * k
        new_dp[0] = sum(dp)
        for j in range(1, k):
            new_dp[j] = dp[j - 1]
        dp = new_dp
        
    print(sum(dp))

if __name__ == '__main__':
    solve()