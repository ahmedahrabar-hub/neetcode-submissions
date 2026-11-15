class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # work backwards from 3rd last to beginning
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        
        # start from index 0 or 1, pick cheaper
        return min(cost[0], cost[1])