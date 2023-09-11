class Solution:
    def __init__(self):
        self.t = [float("inf")]*1000
        
    def minCostClimbingStairs(self, cost) -> int:
        self.t[0] = cost[0]
        for i in len(cost):
            self.t[i] = min(cost[i-1], cost[i-2])
        
        
            