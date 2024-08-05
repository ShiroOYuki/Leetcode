class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        dist = dict()
        for i in range(len(arr)):
            if dist.get(arr[i]) is None:
                dist[arr[i]] = 1
            else:
                dist[arr[i]] += 1
        dl = [x for x in dist if dist.get(x) < 2]
        return dl[k-1] if k <= len(dl) else ""
    
s = Solution()
print(s.kthDistinct(arr = ["d","b","c","b","c","a"], k = 2))