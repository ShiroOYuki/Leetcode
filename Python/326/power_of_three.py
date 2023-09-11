import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        try:
            if (math.log10(n)/math.log10(3)) % 1 == 0:
                return True
        except:
            pass
        return False
    
s = Solution()
print(s.isPowerOfThree(243))