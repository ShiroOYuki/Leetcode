class Solution:
    def climbStairs(self, n: int) -> int:
        return self.dp(n,0,0,[None]*n) if n != 0 else 0
    
    def dp(self,n,sol,add,catch):
        print(n)
        n-=add
        if catch[n-1]:
            return sol+catch[n-1]
        if n > 0:
            if n >= 2:
                sol=self.dp(n,sol,2,catch)
            if n >= 1:
                sol=self.dp(n,sol,1,catch)
        if n == 0:
            sol+=1
        if n != 0:
            catch[n-1] = sol
        return sol
    
s = Solution()
print(s.climbStairs(45))