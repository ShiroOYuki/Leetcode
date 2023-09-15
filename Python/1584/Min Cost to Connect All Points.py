class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        inf = float("inf")
        
        # create a graph
        distances = list(list(inf for _ in range(n)) for __ in range(n))
        for i in range(n):
            for j in range(i, n):
                if i != j:
                    distance = abs(points[i][0] - points[j][0]) + abs(points[i][1]-points[j][1])
                    distances[i][j] = distance
                    distances[j][i] = distance
                    
        for i in distances:
            print(i)
            
        # MST
        
                
print(Solution().minCostConnectPoints(points = [[2,-3],[-17,-8],[13,8],[-17,-15]]))