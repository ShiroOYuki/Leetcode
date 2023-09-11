# class Solution:
#     def minScore(self, n: int, roads: list) -> int:
#         cities = []
#         for _ in range(n):
#             cities.append([float("inf")]*n)
#         for road in roads:
#             cities[road[0]-1][road[1]-1] = cities[road[1]-1][road[0]-1] = road[2]
        
#         # check avaliable
#         m = float("inf")
#         checked = [n-1]
#         stack = []
#         for i in range(len(cities[n-1])):
#             if cities[n-1][i] != float("inf") and i not in checked:
#                 m = min(m, cities[n-1][i])
#                 stack.append(i)
                
                
#         while stack:
#             city = stack.pop(0)
#             if city not in checked:
#                 checked.append(city)
#                 for i in range(len(cities[city])):
#                     if cities[city][i] != float("inf") and i not in checked:
#                         stack.append(i)
#                 m = min([m] + cities[city])
#         return m

# class Solution:
#     def minScore(self, n: int, roads: list) -> int:
#         cities = {}
#         m = [float("inf")] * n
#         res = m.copy()
#         for road in roads:
#             if cities.get(road[0]):
#                 cities[road[0]].append(road[1])
#             else:
#                 cities[road[0]] = [road[1]]
#             if cities.get(road[1]):
#                 cities[road[1]].append(road[0])
#             else:
#                 cities[road[1]] = [road[0]]
#             m[road[0]-1] = min(m[road[0]-1], road[2])
        
#         checked = []
#         stack = set([n])
#         while stack:
#             city = stack.pop()
#             if city not in checked:
#                 res[city-1] = m[city-1]
#                 stack.update(cities[city])
#                 checked.append(city)
#         return min(res)
        
# union search
class Solution:
    def minScore(self, n: int, roads: list) -> int:
        root = [i for i in range(n+1)]

        def find(a):
            if root[a] == a:
                return a
            root[a] = find(root[a]) # path compression  
            return root[a]

        def union(a, b):
            a = find(a)
            b = find(b)
            root[a] = b

        for a, b, _ in roads:
            union(a,b)

        return min(d for a,b,d in roads if find(n) == find(a))
            
[1,2],[3,4],[2,5]
[1,2,3,4,5]
[2,2,4,4,5]
s = Solution()
print(s.minScore(n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7],[1,2,9]]))