# LeetCode 1406 – Stone Game III
stoneValue = [1,2,3,7]
def stoneGame(stoneValue):
    n = len(stoneValue)

    dp = [0] * (n + 1)

    for i in range(n - 1, -1, -1):
        take = 0
        dp[i] = float('-inf')

        for k in range(3):
            if i + k < n:
                take += stoneValue[i + k]
                dp[i] = max(dp[i], take - dp[i + k + 1])

   