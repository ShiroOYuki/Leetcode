from collections import defaultdict

class Solution:
    def minDeletions(self, s: str) -> int:
        d = defaultdict(lambda: 0)
        for letter in s:
            d[letter] += 1
        freq = sorted(list(d.values()), reverse=True)
        res = 0
        n = len(freq)
        if len(set(freq)) != n:
            for i in range(1, n):
                while freq[i] != 0 and freq[i] >= freq[i-1]:
                    freq[i] -= 1
                    res += 1
                    if i != n-1 and freq[i] < freq[i+1]:
                        freq[i], freq[i+1] = freq[i+1], freq[i]
                    
        print(freq)
        return res

print(Solution().minDeletions("bbcebab"))