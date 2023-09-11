from collections import defaultdict

class Solution:
    def countPairs(self, n: int, edges: list) -> int:
        if not edges:
            return n * (n-1) // 2
        
        conn = list(range(n))
        
        def find(i):
            if conn[i] == i:
                return i
            conn[i] = find(conn[i])
            return conn[i]
        
        def union(a, b):
            if find(a) != find(b):
                conn[find(b)] = find(conn[a])
        
        for a, b in edges:
            union(a, b)
        
        res = 0
        err = 0
        length = len(conn)
        d = defaultdict(int)
        for id in range(length):
            d[find(id)] += 1
        for v in d.values():
            err += v
            res += v * (length - err)
        return res
        
s = Solution()
print(s.countPairs(n = 5, edges = [[1,0],[3,1],[0,4],[2,1]]))