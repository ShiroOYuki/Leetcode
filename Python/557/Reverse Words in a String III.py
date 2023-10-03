class Solution:
    def reverseWords(self, s: str) -> str:
        t = ""
        reversed = ""
        for i in s:
            if i == " ":
                reversed += t + " "
                t = ""
            else:
                t = i + t
        else:
            reversed += t
        return reversed
    
print(Solution().reverseWords("ABC DEF"))
        