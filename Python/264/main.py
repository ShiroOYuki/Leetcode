class Solution:
    def nthUglyNumber(self, n: int) -> int:
        u = [2, 3, 5]
        d = [[2], [3], [5]]
        dd = [0]*n
        dd[0] = 1
        i = 0
        
        for i in range(n-1):
            t = [
                max(dd[i]*2, d[0][-1]), 
                max(dd[i]*3, d[1][-1]), 
                max(dd[i]*5, d[2][-1])
            ]
            
            num = min(t)
            dd[i+1] = num
            
            idx = t.index(num)
            d[idx].append(num)
            print(t, d, dd)

        return dd[n-1]

s = Solution()
print(s.nthUglyNumber(10))