class Solution:
    def rangeBitwiseAnd(self, left: int, right: int):
        if right >= left*2:
            return 0
        i = 0
        while right != left:
            right >>= 1
            left >>= 1
            i += 1
        return right << i


s = Solution()
print(s.rangeBitwiseAnd(left=9, right=11))

"""main.py
9,11

1001 >>=1 : 100 10 1000

1011 >>=1 : 101 10 1000

1001


"""
