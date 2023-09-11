class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        # sorted with pairs[n][1]
        n = len(pairs)
        for i in range(n):
            for j in range(i):
                if i != j and pairs[i][1] < pairs[j][1]:
                    pairs[i], pairs[j] = pairs[j], pairs[i]
                    
        # greedy
        curr_tail = pairs[0][1]
        ans = 1
        for pair in pairs:
            if pair[0] > curr_tail:
                curr_tail = pair[1]
                ans += 1
        return ans
        
        
        
print(Solution().findLongestChain([[1,2],[7,8],[4,5]]))