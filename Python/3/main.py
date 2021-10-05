# Sliding Window
# 將軼代到的字元加入至temp 若重複就將temp中該重複字元之前的值全刪除,並將過程中temp最長的值記錄下來
# Ex. temp = [sadfg],字元=d --> temp = [dfg]

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        temp = []
        for i in range(len(s)):
            if s[i] in temp:
                temp = temp[temp.index(s[i])+1:]
            temp.append(s[i])
            ans = max(ans, len(temp))
        return ans


d = Solution()
print(d.lengthOfLongestSubstring("dvdf"))
