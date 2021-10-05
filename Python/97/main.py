class Solution:
    def isInterleave(self, s1, s2, s3):
        from functools import lru_cache

        # https://iter01.com/567029.html
        @lru_cache(None)
        def dp(i, j):
            if i == -1 and j == -1:  # s1 = "",s2 = "" s3 = ""
                return True
            #print(i, j, s1[i], s2[j], s3[i+j+1])
            return (i >= 0 and dp(i-1, j) and s1[i] == s3[i+j+1]) or (j >= 0 and dp(i, j-1) and s2[j] == s3[i+j+1])

        return len(s1) + len(s2) == len(s3) and dp(len(s1) - 1, len(s2) - 1)


s = Solution()
print(s.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))
