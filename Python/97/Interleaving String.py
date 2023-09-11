class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        
        if n < m:
            s1, s2 = s2, s1
        
        if s1 == s3 and not s2:
            return True
        
        if (n + m) != len(s3):
            return False
        
        dp = [[False for i in range(n+1)] for j in range(m+1)]
        dp[0][0] = True
        
        for i in range(n):
            for j in range(m):
                if dp[i][j]:
                    if s1[i] == s3[i+j]:
                        dp[i+1][j] = True
                    if s2[j] == s3[i+j]:
                        dp[i][j+1] = True            
        return dp[n-1][m-1]
    
print(Solution().isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"))
                    