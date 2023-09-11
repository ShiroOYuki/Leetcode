class Solution:
    def longestCycle(self, edges: list) -> int:
        nodes = [0] * len(edges)
        n = len(edges)
        for i in range(n):
            if edges[i] != -1:
                nodes[edges[i]] += 1
                
        visited = [0]*n
        q = []
        
        for i in range(len(nodes)):
            if nodes[i] == 0:
                q.append(i)
                visited[i] = 1
                
        while q:
            i = q.pop()
            next_node = edges[i]
            if next_node != -1:
                nodes[next_node] -= 1
                if nodes[next_node] == 0:
                    q.append(next_node)
                    visited[next_node] = 1
                
        res = -1
        for i in range(n):
            if visited[i] == 1:
                continue
            step = 0
            j = i
            visited[j] = 1
            while edges[j] != -1 and visited[edges[j]] == 0:
                j = edges[j]
                visited[j] = 1
                step += 1
            if step > 0:
                res = max(res, step+1)
        return res
            
        
s = Solution()
# [49,29,24,24,-1,-1,-1,2,23,-1,44,47,52,49,9,31,40,34,-1,53,33,-1,2,-1,18,31,0,9,47,35,-1,-1,-1,-1,4,12,14,19,-1,4,4,43,25,11,54,-1,25,39,17,-1,22,44,-1,44,29,50,-1,-1]
print(s.longestCycle(edges = [-1,2,1]))


