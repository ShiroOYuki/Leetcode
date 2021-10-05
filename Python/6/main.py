class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s or s.replace(s[0], "") == "" or numRows == 1:
            return s
        flag = 1
        group = 0
        temp = []
        for _ in range(numRows):
            temp.append([])
        for i in s:
            temp[group].append(i)
            if group == numRows-1:
                flag = -1
            elif group == 0:
                flag = 1
            group += flag
        s = ""
        for i in range(numRows):
            s += "".join(temp[i])
        return s


s = Solution()
print(s.convert("PAYPALISHIRING", 4))
