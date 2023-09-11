class Solution:
    def minJumps(self, arr: list) -> int:
        from collections import defaultdict
        N = len(arr)  
        if N == 1: 
            return 0
        locs = defaultdict(list)
        for i , n in enumerate(arr): 
            locs[n].append(i)
        visited = {0, N - 1}
        s1, s2 = {0}, {N - 1}
        step = 0
        while s1:
            if len(s1) > len(s2): 
                s1, s2 = s2, s1

            s3 = set()
            while s1:
                i = s1.pop()
                for nb in [i - 1, i + 1] + locs[arr[i]]:
                    if nb in s2: 
                        return step + 1
                    if (nb in visited) or (not 0 <= nb < N): 
                        continue
                    visited.add(nb)
                    s3.add(nb)
                del locs[arr[i]]
            s1 = s3
            if s1: 
                step += 1
        return -1


    
    
s = Solution()
print(s.minJumps(arr = [1,2,2,2,2,2,2,2,2,2,2,2]))