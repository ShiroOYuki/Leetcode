class Solution:
    def makeConnected(self, n: int, connections: list) -> int:
        if n > len(connections)+1:
            return -1
        computers = list(range(0, n))

        def find(n):
            if computers[n] == n:
                return n
            computers[n] = find(computers[n]) # 路徑壓縮 (這樣就直接把 computers[n] 接到他的 root 了)
            return computers[n]
            """沒有路徑壓縮的版本
            return find(computers[n])
            """
        
        def union(a, b):
            computers[find(b)] = find(a)
        
        for wire in connections:
            if find(wire[0]) != find(wire[1]):
                union(wire[0], wire[1])
        
        c = 0
        main_group = find(0)
        for cpu in computers:
            if find(cpu) != main_group:
                c += 1
                union(main_group, find(cpu))
        return c
        