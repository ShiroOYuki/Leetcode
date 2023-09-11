class Solution:
    def compress(self, chars: list) -> int:
        times = 1
        pre = None
        index = 0
        for c in chars:
            if pre == c:
                times += 1
            else:
                if pre:
                    chars[index] = pre
                    index += 1
                if times > 1:
                    for i in list(str(times)):
                        chars[index] = i
                        index += 1
                times = 1
                pre = c
        if pre:
            chars[index] = pre
            index += 1
        if times > 1:
            for i in list(str(times)):
                chars[index] = i
                index += 1
        chars = chars[:index]
        return len(chars)

s = Solution()
print(s.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))

                
                