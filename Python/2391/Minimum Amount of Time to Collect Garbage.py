class Solution:
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        goal = [0, 0, 0]
        amount = 0
        for i in range(len(garbage)):
            if 'G' in garbage[i]:
                goal[0] = i
            if 'P' in garbage[i]:
                goal[1] = i
            if 'M' in garbage[i]:
                goal[2] = i
            amount += len(garbage[i])
        amount += sum(travel[:goal[0]])
        amount += sum(travel[:goal[1]])
        amount += sum(travel[:goal[2]])
        return amount

print(Solution().garbageCollection(garbage = ["G","P","GP","GG"], travel = [2,4,3]))