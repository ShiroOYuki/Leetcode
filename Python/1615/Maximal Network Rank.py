class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        connects = [0]*n
        for i, j in roads:
            connects[i] += 1
            connects[j] += 1
            
        sorted_conn = sorted(set(connects), reverse=True)
        for i, j in roads:
            if (connects[i], connects[j]) in [(sorted_conn[0], sorted_conn[1]), (sorted_conn[1], sorted_conn[0])]:
                return sorted_conn[0] + sorted_conn[1] - 1
        print(connects)
        return sorted_conn[0] + sorted_conn[1]
    
print(Solution().maximalNetworkRank(4, [[0,1],[0,3],[1,2],[1,3]]))