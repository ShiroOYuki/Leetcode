# WRONG ANS

from collections import defaultdict

class Solution:
    def minDeletions(self, s: str) -> int:
        d = defaultdict(lambda: 0)
        for letter in s:
            d[letter] += 1
        freq = sorted(list(d.values()), reverse=True)
        res = 0
        n = len(freq)
        queue = []
        if len(set(freq)) != n:
            for i in range(1, n):
                if freq[i] != 0:
                    next = freq[i] - 1
                    if freq[i] == freq[i-1]:
                        queue.append([i, freq[i]])
                        if freq[i+1] != next:
                            j, val = queue.pop(0)
                            res += val - next
                            freq[j], freq[i] = freq[i], next
                    if freq[i-1] == 0:
                        res += freq[i]      
                        freq[i] = 0
        return res

print(Solution().minDeletions("bbcebab"))