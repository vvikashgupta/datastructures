def minCostClimbingStairs(cost):
    total_steps = len(cost)+1
    dp = [0] * total_steps
    min_cost = 0
    dp[0] = 0
    dp[1] = 0
    for i in range(2,total_steps):
        dp[i] = min((dp[i-2] + cost[i-2]),(dp[i-1] + cost[i-1]))
    return dp[-1]
