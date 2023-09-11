from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: list) -> int:
        
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append((v, 1)) # u to v
            graph[v].append((u, 0)) # v is from u
        visited = {0}
        self.res = 0
        
        def dfs(u):
            visited.add(u)
            for v,c in graph[u]:
                if v not in visited:
                    self.res+=c
                    dfs(v)
        dfs(0)
        
        return self.res


s = Solution()
print(s.minReorder(n = 6, connections = [[0,1],[1,3],[2,3],[4,5],[4,0]]))