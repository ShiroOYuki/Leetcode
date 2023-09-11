class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        ss = ""
        for i in range(len(s)):
            if d.get(s[i]) == None and t[i] not in d.values():
                d[s[i]] = t[i]
            elif d.get(s[i]) == None and t[i] in d.values():
                return False
            ss += d[s[i]]
        print(ss, t)
        return ss == t
    
s = Solution()
print(s.isIsomorphic("badc", "baba"))