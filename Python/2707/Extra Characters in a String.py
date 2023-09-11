class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        n = len(s)
        f = [0]*(n+1)
        d = set(dictionary)
        for i in range(1, n+1):
            
            


print(Solution().minExtraChar(s = "leetscode", dictionary = ["leet","code","leetcode"]))
print(Solution().minExtraChar(s = "sayhelloworld", dictionary = ["hello","world"]))
print(Solution().minExtraChar(s = "dwmodizxvvbosxxw", dictionary = ["ox","lb","diz","gu","v","ksv","o","nuq","r","txhe","e","wmo","cehy","tskz","ds","kzbu"]))