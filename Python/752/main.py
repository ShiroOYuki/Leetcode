class Solution:
    def openLock(self, deadends: list, target: str):
        for i in range(len(deadends)):
            deadends[i] = [int(j) for j in deadends[i]]
        target = [int(i) for i in target]
        print(deadends, target)


s = Solution()
s.openLock(deadends=["0201", "0101", "0102", "1212", "2002"], target="0202")


0, 1, 2, 3, 4, 5, 6, 7, 8, 9
