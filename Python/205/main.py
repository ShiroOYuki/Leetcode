class Solution:
    def isIsomorphic(self, s: str, t: str):
        if s == t == "":
            return True
        d = {}
        ind = []
        s2 = ""
        for i in range(len(s)):
            if s[i] not in d:
                if t[i] in ind:
                    return False
                ind.append(t[i])
                d[s[i]] = t[i]
            s2 += d[s[i]]
        print(s2)
        if s2 == t:
            return True
        return False


s = Solution()
print(s.isIsomorphic("badc", "baba"))
